# Clean up for CRP Data

def clean_pac_to_pac(data_file):
    """input: Center For Responsive Politics pac_2_pac text file
       output: cleaned dataframe containing text file data
     """

    df = pd.read_csv(data_file,sep="\|*,\|", header=None)
    df.columns = ['Cycle','FECRecNo','Filerid','DonorCmte','ContribLendTrans','City','State','Zip',
                  'FECOccEmp','Primcode','Date,Amount,RecipID','Party','Otherid','RecipCode',
                  'RecipPrimcode','Amend','Report','PG','Microfilm','Type','RealCode','Source']
    return df
