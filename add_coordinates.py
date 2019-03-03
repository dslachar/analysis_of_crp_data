# pip install uszipcode
import pandas as pd
from uszipcode import SearchEngine
search = SearchEngine(simple_zipcode=False)

def add_coordinates(df):
    '''Input: a pandas dataframe which includes a 'Zip' field representing a
       US zip code.
       Output: dataframe with 'lat' and 'lng' fields added which represent
       latitude and longitude

    '''
    df['lat'] = df['Zip'].apply(lambda x: pd.Series(search.by_zipcode(x).lat))
    df['lng'] = df['Zip'].apply(lambda x: pd.Series(search.by_zipcode(x).lng))
