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
def get_products_day_count(factory : str = "", area : str = "", product_code : int=0, 
                           year : int = 0, month : int = 0, day : int = 0,
                           skip: int = 0, limit: int = 10):
    
    filter = []

    if factory != "":
        filter.append("factory == @factory") 
    if area != "":
        filter.append( "area == @area")
    if product_code > 0 :
       filter.append("product_code == @product_code")
    if year > 0 :
        filter.append("year == @year")
    if month > 0:
        filter.append("month == @month")
    if day > 0:
        filter.append("day == @day")
 

    if filter.__len__() > 0:
        filter_str = " and ".join(filter)
        result = service.calc_products_day_count().iloc[skip:(skip+limit)].query(filter_str).to_dict(orient='records')
    else:
        result = service.calc_products_day_count().iloc[skip:(skip+limit)].to_dict(orient='records')
    return result

@app.get("/products_std_day")
def get_products_std_day(factory : str = "", area : str = "", product_code : int =0, 
                         year : int = 0, month : int = 0, day : int = 0,
                         skip: int = 0, limit: int = 10):
    
    filter = []

    if factory != "":
        filter.append("factory == @factory") 
    if area != "":
        filter.append( "area == @area")
    if product_code > 0 :
       filter.append("product_code == @product_code")
    if year > 0 :
        filter.append("year == @year")
    if month > 0:
        filter.append("month == @month")
    if day > 0:
        filter.append("day == @day")

    if filter.__len__() > 0:
        filter_str = " and ".join(filter)
        result = service.calc_products_std_day().query(filter_str).iloc[skip:(skip+limit)].to_dict(orient='records')
    else:
        result = service.calc_products_std_day().iloc[skip:(skip+limit)].to_dict(orient='records')
    return result

@app.get("/products_avg_month")
def get_products_month(factory : str = "", area : str = "", product_code : int=0, 
                       year : int = 0, month : int = 0,
                       skip: int = 0, limit: int = 10):
    

    filter = []

    if factory != "":
        filter.append("factory == @factory") 
    if area != "":
        filter.append( "area == @area")
    if product_code > 0 :
       filter.append("product_code == @product_code")
    if year > 0 :
        filter.append("year == @year")
    if month > 0:
        filter.append("month == @month")
     

    if filter.__len__() > 0:
        filter_str = " and ".join(filter)
        result = service.calc_products_month().query(filter_str).iloc[skip:(skip+limit)].to_dict(orient='records')
    else:
        result = service.calc_products_month().iloc[skip:(skip+limit)].to_dict(orient='records')
    return result

@app.get("/products_avg_year")
def get_products_year(factory : str = "", area : str = "", product_code : int=0, 
                      year : int = 0,
                      skip: int = 0, limit: int = 10):
    
    filter = []

    if factory != "":
        filter.append("factory == @factory") 
    if area != "":
        filter.append( "area == @area")
    if product_code > 0 :
       filter.append("product_code == @product_code")
    if year > 0 :
        filter.append("year == @year")


    if filter.__len__() > 0 :
        filter_str = " and ".join(filter)
        result = service.calc_products_year().query(filter_str).iloc[skip:(skip+limit)].to_dict(orient='records')
    else:
        result = service.calc_products_year().iloc[skip:(skip+limit)].to_dict(orient='records')
    return result



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

 