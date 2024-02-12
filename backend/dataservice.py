import pandas as pd


class DataService():
    """
    DataService: Class for managing and analyzing data from a CSV file using pandas.

    Attributes:
    - file_csv (str): Path to the CSV file.
    - df (pd.DataFrame): DataFrame for storing loaded data.
    - product_day (pd.DataFrame): DataFrame for daily product counts.
    - product_month (pd.DataFrame): DataFrame for monthly average product counts.
    - product_year (pd.DataFrame): DataFrame for yearly average product counts.
    - file_loaded (bool): Flag indicating whether the data has been loaded.

    Methods:
    - __init__(self, path_file_csv): Constructor method to initialize the DataService object with the CSV file path.
    - load_data(self, force_load=False): Method to load data from the CSV file into the DataFrame.
    - calc_products_day_count(self): Method to calculate daily product counts.
    - calc_products_month(self): Method to calculate monthly average product counts.
    - calc_products_year(self): Method to calculate yearly average product counts.

    """

    file_csv = '' 
    #cache objects
    df = pd.DataFrame()
    product_day = pd.DataFrame()
    product_month = pd.DataFrame()
    product_year = pd.DataFrame()
    file_loaded = False

    def __init__(self,path_file_csv):
        self.file_csv = path_file_csv

    def load_data(self, force_load = False):
        """
        Method to load data from the CSV file into the DataFrame.

        Parameters:
        - force_load (bool): If True, forces reloading the data even if it has been loaded before.

        """

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
        """
        Method to calculate daily product counts.

        Returns:
        - pd.DataFrame: DataFrame with daily product counts.

        """

        if self.file_loaded == False :  
            self.load_data()
        
        if self.product_day.size == 0:
            count = self.df.groupby(['factory','area','year','month','day','date','product_code']).size().reset_index(name='count')
            self.product_day = count.groupby(['factory','area','year','month','day','date']).size().reset_index(name='products_day')
            print("function calc_products_day_count executed")

        return self.product_day

    def calc_products_month(self):
        """
        Method to calculate monthly average product counts.

        Returns:
        - pd.DataFrame: DataFrame with monthly average product counts.

        """
        #option using to_period
        #product_month = product_day.groupby(['area','product_code', pd.to_datetime(product_day['date']).dt.to_period('M') ]) ['count'].mean().reset_index(name='avg')
        if self.file_loaded == False:
            self.load_data()

        product_day = self.calc_products_day_count() 
        if product_day.size > 0 :  
            if self.product_month.size == 0:
                self.product_month = product_day.groupby(['factory','area','year','month' ]) ['products_day'].mean().reset_index(name='avg_month')
                print("function calc_products_month executed")
            self.product_month['avg_month'] = self.product_month['avg_month'].round(2)
            return self.product_month

    def calc_products_year(self):
        """
        Method to calculate yearly average product counts.

        Returns:
        - pd.DataFrame: DataFrame with yearly average product counts.

        """

        #option using to_period
        #product_year = product_month.groupby(['area','product_code', product_month['date'].dt.year ]) ['avg'].mean().reset_index(name='avg')
        if self.file_loaded == False:
            self.load_data()
        
        product_month = self.calc_products_month()
        if product_month.size > 0 : 
            if self.product_year.size == 0:
                product_year = product_month.groupby(['factory','area', 'year' ]) ['avg_month'].mean().reset_index(name='avg_year')
                print("function calc_products_year executed")
            product_year['avg_year'] = product_year['avg_year'].round(2)
            return product_year

    class FilterBuilder():
        """
        A sub class for building filter conditions based on specified parameters.

        Attributes:
        - factory (str): Filter condition for the factory.
        - area (str): Filter condition for the area.
        - year (int): Filter condition for the year.
        - month (int): Filter condition for the month.
        - day (int): Filter condition for the day.

        Methods:
        - __init__(self, factory='', area='', year=0, month=0, day=0): Constructor to initialize the FilterBuilder.
        - build(self): Builds the filter string based on specified parameters.

        """

        def __init__(self,factory : str ='', area : str = '', year : int = 0, month : int = 0, day : int = 0 ):
            self.factory = factory
            self.area = area
            self.year = year
            self.month = month
            self.day = day

        def build(self):
            """
            Builds the filter string based on specified parameters.

            Returns:
            - str: The constructed filter string.

            """
            filter = []

            if self.factory != "":
                filter.append("factory == @factory") 
            if self.area != "":
                filter.append( "area == @area")
            if self.year > 0 :
                filter.append("year == @year")
            if self.month > 0:
                filter.append("month == @month")
            if self.day > 0:
                filter.append("day == @day")
        

            if filter.__len__() > 0:
                filter_str = " and ".join(filter)    
                return filter_str
            return ''
        