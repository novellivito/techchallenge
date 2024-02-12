from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dataservice import DataService
import uvicorn
from typing import Annotated

BASE_URL = '/api/v1'

app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:4200'  # Angular app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Initialize DataService with the CSV file path
service = DataService('data.csv')

@app.get(f'{BASE_URL}/')
def read_root():
    return 'root'


@app.get(f'{BASE_URL}/products_day')
def get_products_day(factory : str = '', area : str = '',
                           year : int = 0, month : int = 0, day : int = 0,
                           skip: int = 0, limit: int = 10):
    """
    Endpoint to get daily product counts with filtering, pagination, and limits.

    Parameters:
    - factory (str): Filter for the factory.
    - area (str): Filter for the area.
    - year (int): Filter for the year.
    - month (int): Filter for the month.
    - day (int): Filter for the day.
    - skip (int): Number of items to skip for pagination.
    - limit (int): Maximum number of items to return.

    Returns:
    - List of dictionaries representing the obtained results.
    """

    filter = DataService.FilterBuilder(factory=factory,area=area,year=year,month=month,day=day).build()

    result = []

    if filter != '':
        result = service.calc_products_day_count().query(filter).iloc[skip:(skip+limit)].to_dict(orient='records')
    else:
        result = service.calc_products_day_count().iloc[skip:(skip+limit)].to_dict(orient='records')
    
    return result



@app.get(f'{BASE_URL}/products_avg_month')
def get_products_month(factory : str = '', area : str = '',
                       year : int = 0, month : int = 0,
                       skip: int = 0, limit: int = 10):
    
    """
    Endpoint to get monthly average product counts with filtering, pagination, and limits.

    Parameters:
    - factory (str): Filter for the factory.
    - area (str): Filter for the area.
    - year (int): Filter for the year.
    - month (int): Filter for the month.
    - skip (int): Number of items to skip for pagination.
    - limit (int): Maximum number of items to return.

    Returns:
    - List of dictionaries representing the obtained results.
    """

    filter = DataService.FilterBuilder(factory=factory,area=area,year=year,month=month).build()

    result = [] 

    if filter != '':
        result = service.calc_products_month().query(filter).iloc[skip:(skip+limit)].to_dict(orient='records')
    else:
        result = service.calc_products_month().iloc[skip:(skip+limit)].to_dict(orient='records')
    return result

@app.get(f'{BASE_URL}/products_avg_year')
def get_products_year(factory : str = '', area : str = '', product_code : int=0, 
                      year : int = 0,
                      skip: int = 0, limit: int = 10):
    """
    Endpoint to get yearly average product counts with filtering, pagination, and limits.

    Parameters:
    - factory (str): Filter for the factory.
    - area (str): Filter for the area.
    - product_code (int): Filter for the product code.
    - year (int): Filter for the year.
    - skip (int): Number of items to skip for pagination.
    - limit (int): Maximum number of items to return.

    Returns:
    - List of dictionaries representing the obtained results.
    """
    
    filter = DataService.FilterBuilder(factory = factory, area=area, year=year).build()

    result = []

    if filter != '':
        result = service.calc_products_year().query(filter).iloc[skip:(skip+limit)].to_dict(orient='records')
    else:
        result = service.calc_products_year().iloc[skip:(skip+limit)].to_dict(orient='records')
    return result



if __name__ == '__main__':
    # Start the FastAPI application using Uvicorn on http://127.0.0.1:8000
    uvicorn.run(app, host = '127.0.0.1', port = 8000)

 