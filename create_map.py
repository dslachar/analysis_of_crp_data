import pandas as pd
import plotly
plotly.tools.set_credentials_file(username='dslachar', api_key='mH9X56yYS27X1dcOQ1Um')
plotly.__version__
import add_coordinates
import numpy as np
import colorlover as cl
from IPython.display import HTML
import plotly.plotly as py
import plotly.figure_factory as ff

def plot_map(pickle_file):
    df_indivs = pd.read_pickle(pickle_file)

    #Convert Amount to ineteger
    df_indivs.Amount = df_indivs.Amount.astype(int)

    #add party column
    df_indivs['Party'] = df_indivs['RecipCode'].str[0]

    #group by party
    df_indivs_Rep = df_indivs[df_indivs['Party'] == 'R']
    df_indivs_Dem = df_indivs[df_indivs['Party'] == 'D']

    #group by zip code
    df_indivs_Rep_by_zip = df_indivs_Rep.groupby(['Zip']).sum()
    df_indivs_Dem_by_zip = df_indivs_Dem.groupby(['Zip']).sum()

    #add zip column
    df_indivs_Rep_by_zip['Zip'] = df_indivs_Rep_by_zip.index
    df_indivs_Dem_by_zip['Zip'] = df_indivs_Dem_by_zip.index

    #add county fip codes
    col_Rep = add_coordinates.add_fips(df_indivs_Rep_by_zip)
    col_Dem = add_coordinates.add_fips(df_indivs_Dem_by_zip)

    #group parties by county fip code, sum amounts
    col_Rep_by_county = col_Rep.groupby(['fip']).sum()
    col_Dem_by_county = col_Dem.groupby(['fip']).sum()

    #add fip column
    col_Rep_by_county['fip_col'] = col_Rep_by_county.index
    col_Dem_by_county['fip_col'] = col_Dem_by_county.index

    #add_party_contributions
    col_Rep_by_county['rep_contributions'] = col_Rep_by_county['Amount']
    col_Dem_by_county['dem_contributions'] = col_Dem_by_county['Amount']

    #drop uneeded columns
    df_rep_final = col_Rep_by_county.drop(['Amount', 'FECTransID'], axis=1)
    df_dem_final = col_Dem_by_county.drop(['Amount', 'FECTransID'], axis=1)

    #merge democrat and republican maps
    df_merge = pd.merge(df_dem_final, df_rep_final, on='fip_col', how='outer')
    df_final = df_merge.fillna(value = 0)

    #get final processed dataframe
    df_final['dem_minus_rep_contrib'] = df_final['dem_contributions'] - df_final['rep_contributions']

    #get max value
    maximum = df_final.dem_minus_rep_contrib.max()

    fips = df_final['fip_col'].tolist()

    values = (df_final['dem_minus_rep_contrib'].tolist())

    colorscale=['rgb(165,0,38)', 'rgb(215,48,39)', 'rgb(244,109,67)', 'rgb(253,174,97)', 'rgb(254,224,144)',  'rgb(224,243,248)',
             'rgb(171,217,233)', 'rgb(116,173,209)',  'rgb(69,117,180)','rgb(49,54,149)']

    endpts = list(np.linspace(-maximum, maximum , len(colorscale) - 1))

    scope = ['COLORADO']
    fig = ff.create_choropleth(fips=fips,
                               binning_endpoints = endpts, colorscale = colorscale,
                               county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
                               values=values,
                               scope = scope)
    py.iplot(fig, filename='choropleth of political contributions by party and county in Colorado')

