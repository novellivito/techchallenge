import pandas as pd


class DataService():
    file_csv = '' 
    #cache objects
    df = pd.DataFrame()
    product_day = pd.DataFrame()
    product_day_std = pd.DataFrame()
    product_month = pd.DataFrame()
    product_year = pd.DataFrame()
    file_loaded = False

    def __init__(self,path_file_csv):
        self.file_csv = path_file_csv

    def load_data(self, force_load = False):
        print(f'File data : {self.file_csv}')
 
        if force_load == True :
            print(f'File data : {self.file_csv} reload')
            self.df = pd.DataFrame()
            self.file_loaded = False
            self.product_day = pd.DataFrame()
            self.product_day_std = pd.DataFrame()
            self.product_month = pd.DataFrame()
            self.product_year = pd.DataFrame()

        if self.file_loaded == False: 
            try:
                self.df = pd.read_csv(self.file_csv)
                self.df['date'] = pd.to_datetime(self.df['date']) #cast date into datetime
                self.df['year'] = self.df['date'].dt.year
                self.df['month'] = self.df['date'].dt.month 
                self.df['day'] = self.df['date'].dt.day 
                self.file_loaded = True
            except Exception as e :
                self.file_loaded = False
            
    def calc_products_day_count(self):

        if self.file_loaded == False :  
            self.load_data()
        
        if self.product_day.size == 0:
            self.product_day = self.df.groupby(['factory','area','product_code','year','month','day','date']).size().reset_index(name='count')
            print("function calc_products_day_count executed")
        return self.product_day

    def calc_products_std_day(self):
        if self.file_loaded == False:
            self.load_data()
        product_day = self.calc_products_day_count()
        if product_day.size > 0 :
            if self.product_day_std.size == 0:
                self.product_day_std = product_day.groupby(['factory','area','product_code'])['count'].std().reset_index(name='std')
                print("function calc_products_std_day executed")
            return self.product_day_std

    def calc_products_month(self):
        
        #option using to_period
        #product_month = product_day.groupby(['area','product_code', pd.to_datetime(product_day['date']).dt.to_period('M') ]) ['count'].mean().reset_index(name='avg')
        if self.file_loaded == False:
            self.load_data()

        product_day = self.calc_products_day_count() 
        if product_day.size > 0 :  
            if self.product_month.size == 0:
                self.product_month = product_day.groupby(['factory','area','product_code','year','month' ]) ['count'].mean().reset_index(name='avg')
                print("function calc_products_month executed")
            return self.product_month

    def calc_products_year(self):
        
        #option using to_period
        #product_year = product_month.groupby(['area','product_code', product_month['date'].dt.year ]) ['avg'].mean().reset_index(name='avg')
        if self.file_loaded == False:
            self.load_data()
        
        product_month = self.calc_products_month()
        if product_month.size > 0 : 
            if self.product_year.size == 0:
                product_year = product_month.groupby(['factory','area','product_code', 'year' ]) ['avg'].mean().reset_index(name='avg')
                print("function calc_products_year executed")
            return product_year