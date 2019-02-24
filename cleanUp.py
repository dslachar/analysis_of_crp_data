# Clean up for CRP Data

<<<<<<< HEAD
def clean_pac_to_pac(data_file):
    """input: Center For Responsive Politics pac_2_pac text file
       output: cleaned dataframe containing text file data
     """

    df = pd.read_csv(data_file,sep="\|*,\|", header=None)
    df.columns = ['Cycle','FECRecNo','Filerid','DonorCmte','ContribLendTrans','City','State','Zip',
                  'FECOccEmp','Primcode','Date,Amount,RecipID','Party','Otherid','RecipCode',
                  'RecipPrimcode','Amend','Report','PG','Microfilm','Type','RealCode','Source']
    return df
=======
import pandas as pd

def clean_candidates(file):
    # read in text file to a dataframe
    cands_df = pd.read_csv(file,sep='\|,\|',header=None)

    # creates the columns for candidates data
    cands_df.columns = ["Cycle", "FECTransID", "ContribID", "Contrib","RecipID",
    "Orgname","UltOrg","RealCode","Date","CRPICO","RecipCode","NoPacs"]

    # take out the extra symbols
    cands_df['Cycle'] = cands_df['Cycle'].map(lambda x: x.strip('|'))
    cands_df["NoPacs"] = cands_df["NoPacs"].str.replace('|','')

    return cands_df

def clean_individuals(file):
    # read in txt file to a dataframe
    indivs_df = pd.read_csv(file,sep='\|,\|',header=None)

    # create the columns for individuals data
    indivs_df.columns = ["Cycle", "FECTransID", "ContribID", "Contrib","RecipID",
    "Orgname","UltOrg","RealCode","City","State","Zip","RecipCode","Type","CmteID",
    "OtherID","Gender","Microfilm","Occupation","Employer","Source"]

    # take out the extra symbols
    indivs_df['Cycle'] = indivs_df['Cycle'].map(lambda x: x.strip('|'))
    indivs_df["Source"] = indivs_df["Source"].str.replace('|','')

    # create a new dataframe from RealCode column with RealCode,Date,Amount
    real_df = indivs_df['RealCode'].apply(lambda x: pd.Series(str(x).split(',')))
    real_df[0] = real_df[0].map(lambda x: x.strip('|'))
    real_df.columns= ['RealCode','Date','Amount','NA']
    # insert the real dataframe back into the individuals dataframe
    indivs_df['RealCode'] = real_df['RealCode'].values
    indivs_df.insert(8,'Date',real_df['Date'])
    indivs_df.insert(9,'Amount',real_df['Amount'])

    return indivs_df
>>>>>>> cleanup_samantha
