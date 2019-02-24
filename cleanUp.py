# Clean up for CRP Data
import pandas as pd

def cleanPac(filename):
    '''Cleans pacs txt file
        Parameters: 1) filename: txt file from CRP
        Returns: 1) Pandas dataframe of cleaned data '''
    # read in file and add column names
    pac = pd.read_csv(filename, sep='\|,\|', header=None,engine='python')
    pac.columns = ["Cycle", "FECRecNo","PACID","CID","Type","DI","FECCandID"]
    # Clean cid, amount, date, realcode
    df = pac['CID'].apply(lambda x: pd.Series(str(x).split(',')))
    pac['CID'] = df[0]
    pac.insert(4,'Amount',df[1])    
    pac.insert(5,'Date',df[2])
    pac.insert(6, 'RealCode',df[3])
    # Remove vertical bars
    pac['Cycle'] = pac['Cycle'].str.replace('|','')
    pac['CID'] = pac['CID'].str.replace('|','')
    pac['RealCode'] = pac['RealCode'].str.replace('|','')
    pac['FECCandID'] = pac['FECCandID'].str.replace('|','')
    return pac

def clean_pac_to_pac(data_file):
    """input: Center For Responsive Politics pac_2_pac text file
       output: cleaned dataframe containing text file data
     """

    df = pd.read_csv(data_file,sep="\|*,\|", header=None)
    df.columns = ['Cycle','FECRecNo','Filerid','DonorCmte','ContribLendTrans','City','State','Zip',
                  'FECOccEmp','Primcode','Date,Amount,RecipID','Party','Otherid','RecipCode',
                  'RecipPrimcode','Amend','Report','PG','Microfilm','Type','RealCode','Source']
    return df
>>>>>>> 33ef3965bbef52a39290ee9f3cc6f92c17a982ba
>>>>>>> b5109476eaabb71ba663d215902595fb890a0d60
