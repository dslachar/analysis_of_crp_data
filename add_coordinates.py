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

    df['county'] = df['Zip'].apply(lambda x: pd.Series(search.by_zipcode(x).county))

def add_fips(df):
    '''Input: a pandas dataframe which includes a 'Zip' field representing a
       US zip code.
       Output: dataframe with 'lat' and 'lng' fields added which represent
       latitude and longitude

    '''

    colorado_fips = ['08001', '08003', '08005', '08007', '08009', '08011', '08013', '08014', '08015', '08017', '08019',
                    '08021', '08023', '08025', '08027', '08029', '08031', '08033', '08035', '08037', '08039', '08041',
                    '08043', '08045', '08047', '08049', '08051', '08053', '08055', '08057', '08059', '08061', '08063',
                    '08065', '08067', '08069', '08071', '08073', '08075', '08077', '08079', '08081', '08083', '08085',
                    '08087', '08089', '08091', '08093', '08095', '08097', '08099', '08101', '08103', '08105', '08107',
                    '08109', '08111', '08113', '08115', '08117', '08119', '08121', '08123', '08125']

    colorado_counties = ['Adams County', 'Alamosa County', 'Arapahoe County', 'Archuleta County', 'Baca County', 'Bent County', 'Boulder County', 'Broomfield County',
                         'Chaffee County', 'Cheyenne County', 'Clear Creek County', 'Conejos County', 'Costilla County', 'Crowley County', 'Custer County',
                         'Delta County', 'Denver County', 'Dolores County', 'Douglas County', 'Eagle County', 'Elbert County', 'El Paso County', 'Fremont County',
                         'Garfield County', 'Gilpin County', 'Grand County', 'Gunnison County', 'Hinsdale County', 'Huerfano County', 'Jackson County', 'Jefferson County',
                         'Kiowa County', 'Kit Carson County', 'Lake County', 'La Plata County', 'Larimer County', 'Las Animas County',  'Lincoln County', 'Logan County',
                         'Mesa County', 'Mineral County', 'Moffat County', 'Montezuma County', 'Montrose County', 'Morgan County', 'Otero County', 'Ouray County',
                         'Park County', 'Phillips County', 'Pitkin County', 'Prowers County',  'Pueblo County', 'Rio Blanco County', 'Rio Grande County','Routt County',
                         'Saguache County', 'San Juan County', 'San Miguel County', 'Sedgwick County', 'Summit County', 'Teller County', 'Washington County',
                         'Weld County', 'Yuma County']


    counties_fips_dict = dict(zip(colorado_counties, colorado_fips))

    df['county'] = df['Zip'].apply(lambda x: pd.Series(search.by_zipcode(x).county))
    col_only_df = df[df['county'].isin(colorado_counties)]
    col_only_df['fip'] = col_only_df['county'].apply(lambda x: counties_fips_dict[x])
    return col_only_df










