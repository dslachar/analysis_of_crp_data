# Clean up for CRP Data
import pandas as pd

def clean_candidates(file):
    '''Cleans candidates text file. Outputs dataframe'''
    # read in text file to a dataframe
    cands_df = pd.read_csv(file,sep='\|,\|',header=None, engine='python')

    # creates the columns for candidates data
    cands_df.columns = ["Cycle", "FECTransID", "ContribID", "Contrib","RecipID",
    "Orgname","UltOrg","RealCode","Date","CRPICO","RecipCode","NoPacs"]

    # removes extra symbols
    cands_df['Cycle'] = cands_df['Cycle'].map(lambda x: x.strip('|'))
    cands_df["NoPacs"] = cands_df["NoPacs"].str.replace('|','')

    return cands_df

def clean_individuals(file):
    '''Cleans individuals text file. Outputs dataframe'''
    # read in text file to a dataframe
    indivs_df = pd.read_csv(file,sep='\|,\|',header=None,engine='python')

    # create the columns for individuals data
    indivs_df.columns = ["Cycle", "FECTransID", "ContribID", "Contrib","RecipID",
    "Orgname","UltOrg","RealCode","City","State","Zip","RecipCode","Type","CmteID",
    "OtherID","Gender","Microfilm","Occupation","Employer","Source"]

    # pull out only the C0 individuals
    df = indivs_df.loc[indivs_df['State'] == 'CO']

    # removes extra symbols
    df['Cycle'] = df['Cycle'].map(lambda x: x.strip('|'))
    df["Source"] = df["Source"].str.replace('|','')

    # creates a new dataframe with RealCode, Data, Amount columns
    real_df = df['RealCode'].apply(lambda x: pd.Series(str(x).split(',')))
    real_df[0] = real_df[0].map(lambda x: x.strip('|'))
    real_df.columns= ['RealCode','Date','Amount','NA']
    # inserts new dataframe into individuals dataframe
    df['RealCode'] = real_df['RealCode'].values
    df.insert(8,'Date',real_df['Date'])
    df.insert(9,'Amount',real_df['Amount'])

    return df

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
