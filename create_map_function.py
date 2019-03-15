import pandas as pd
import numpy as np
import folium
import json
import add_coordinates
from folium.plugins import FastMarkerCluster
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)

def create_map(pickle_file):

    df_indivs = pd.read_pickle(pickle_file)

    #Convert Amoung to ineteger
    df_indivs.Amount = df_indivs.Amount.astype(int)

    # Add Party Column
    df_indivs['Party'] = df_indivs['RecipCode'].str[0]

    #Create Democrat and Republican Tables
    df_indivs_Rep = df_indivs[df_indivs['Party'] == 'R']
    df_indivs_Dem = df_indivs[df_indivs['Party'] == 'D']

    #Group By ZipCode
    df_indivs_Rep_by_zip = df_indivs_Rep.groupby(['Zip']).sum()
    df_indivs_Dem_by_zip = df_indivs_Dem.groupby(['Zip']).sum()

    #add zip code column for group by
    df_indivs_Rep_by_zip['Zip'] = df_indivs_Rep_by_zip.index
    df_indivs_Dem_by_zip['Zip'] = df_indivs_Dem_by_zip.index

    #add geographic coordinates
    add_coordinates.add_coordinates(df_indivs_Rep_by_zip)
    add_coordinates.add_coordinates(df_indivs_Dem_by_zip)

    #drop na, get final
    rep_final = df_indivs_Rep_by_zip.dropna(subset=['lat'])
    dem_final = df_indivs_Dem_by_zip.dropna(subset=['lat'])



    #initialize colorado map
    colorado_lat = [37,41]
    colorado_lng = [-102, -109]
    colorado_map = folium.Map(location=[np.mean(colorado_lat),
                           np.mean(colorado_lng)],
                           zoom_start=7)

    for row in dem_final.itertuples():
        colorado_map.add_child(folium.CircleMarker(location=[row.lat, row.lng], fill_color = "blue" ))

    for row in rep_final.itertuples():
        colorado_map.add_child(folium.CircleMarker(location=[row.lat, row.lng], fill_color = "red" ))

    return map_plot














