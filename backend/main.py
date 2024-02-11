from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dataservice import DataService
import uvicorn

from typing import Annotated

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200"  # Angular app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


service = DataService('data.csv')

@app.get('/')
def read_root():
    return "root"


@app.get("/products_day_count")
def get_products_day_count(factory : str = "", area : str = "",
                           year : int = 0, month : int = 0, day : int = 0,
                           skip: int = 0, limit: int = 10):
     

    filter = DataService.FilterBuilder(factory=factory,area=area,year=year,month=month,day=day).build()

    result = []

    if filter != '':
        result = service.calc_products_day_count().query(filter).iloc[skip:(skip+limit)].to_dict(orient='records')
    else:
        result = service.calc_products_day_count().iloc[skip:(skip+limit)].to_dict(orient='records')
    
    return result



@app.get("/products_avg_month")
def get_products_month(factory : str = "", area : str = "",
                       year : int = 0, month : int = 0,
                       skip: int = 0, limit: int = 10):
    

    filter = DataService.FilterBuilder(factory=factory,area=area,year=year,month=month).build()

    result =[] 

    if filter != '':
        result = service.calc_products_month().query(filter).iloc[skip:(skip+limit)].to_dict(orient='records')
    else:
        result = service.calc_products_month().iloc[skip:(skip+limit)].to_dict(orient='records')
    return result

@app.get("/products_avg_year")
def get_products_year(factory : str = "", area : str = "", product_code : int=0, 
                      year : int = 0,
                      skip: int = 0, limit: int = 10):
    
    
    filter = DataService.FilterBuilder(factory = factory, area=area, year=year).build()

    result = []

    if filter != '':
        result = service.calc_products_year().query(filter).iloc[skip:(skip+limit)].to_dict(orient='records')
    else:
        result = service.calc_products_year().iloc[skip:(skip+limit)].to_dict(orient='records')
    return result



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

 