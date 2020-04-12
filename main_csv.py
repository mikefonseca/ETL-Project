import os
os.chdir("C:\Users\mikef\Documents\GitHub\ETL-Project") # set working directory
import pandas as pd

# list of columns to keep
used_cars_cols = ["year","manufacturer","model","condition","odometer","title_status","type"]
keep_cols = ["docid","overall_rating"]

##Functions
def check_cols_from_file(pth):
    """
    get the column names of a file
    ::arg(pth)= path to csv file (string)
    """
    df=pd.read_csv(pth,nrows=1,header=0)
    return [x.strip() for x in df.columns.tolist()]

def clean_docid(dfx):
	"""
	clean up the docid column to extract mfg, model etc
	"""
    yr_df = dfx[["overall_rating"]]
    docid = dfx.docid.str.split("_",expand=True)
    docid = docid.iloc[0:docid.shape[0],0:3]
    docid.columns = ["year","manufacturer","model"]
    docid["overall_rating"]= yr_df.overall_rating.tolist()
    return docid

def subset_csv_from_lis(csvpth,lis,dcid=False):
    """
    subset a csv from a list of columns of interest
    """
    col_names = check_cols_from_file(csvpth)
    keepers = [x for x in col_names if x in lis]
    if dcid==True:
        df=pd.read_csv(csvpth,usecols=keepers,low_memory=False)
        return(clean_docid(df))
    else:
        return(pd.read_csv(csvpth,usecols=keepers,low_memory=False))


if __name__ == '__main__':
	df1=subset_csv_from_lis("Used Vehicles.csv",used_cars_cols)
	df1["year"]= df1.year.fillna(0.0).astype(int)
	df1["year"]=df1.year.replace(0,"NULL")
	df1.to_csv("C:\\tmp\\Used_Vehicles_cleaned.csv",index=True,na_rep="NULL")
	df2=subset_csv_from_lis("2008.csv",keep_cols,True)
	df2.to_csv("C:\\temp\\Ratings_2008_cleaned.csv",index=F)
	print("Finished Cleaning Files")

	
