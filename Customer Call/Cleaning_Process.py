import pandas as pd

df=pd.read_excel(r"D:\Smpl Data Pd\Data Clean\Uncleaned Customer Call List.xlsx")
df

# Drop duplicate values
df=df.drop_duplicates()
df

# to drop the column(unwanted col)
df=df.drop(columns='Not_Useful_Column')
df

'''        Name         '''
# lstrip() -> removes the given left value from the col
# rstrip() -> removes the given right value from the col

df['Last_Name']=df['Last_Name'].str.lstrip('...')
df['Last_Name']=df['Last_Name'].str.lstrip('/')
df['Last_Name']=df['Last_Name'].str.rstrip('_')
df

# alternate way, by specifying the characters to be removed inside the strip
df['Last_Name']=df['Last_Name'].str.strip('123._/')
df

'''         Phone Number        '''
# [^a-zA-Z0-9] -->Regex (Regular Expression).all non-alphanumeric characters are removed from the phone numbers.
#                 if the col with these kind of values it will be replaced using replace()

# Step 1: Remove the special characters in ph-no
df["Phone_Number"]=df["Phone_Number"].str.replace('[^a-zA-Z0-9]','',regex=True)
df

# Step 2: Convert the datatype to 'str' bcoz of the values like 'Na,NaN...' this will rise an error while performing operations
df['Phone_Number']= df['Phone_Number'].apply(lambda x: str(x))
df

# Step 3: Format the col a/c to the need
df['Phone_Number']=df['Phone_Number'].apply(lambda x: x[0:3]+"-"+x[3:6]+"-"+x[6:10])
df

# Step 4: Replace NULL values ie 'Nan,Na,NAN...' with blank
df['Phone_Number']=df['Phone_Number'].str.replace("nan--","")
df['Phone_Number']=df['Phone_Number'].str.replace("Na--","")
df

'''         Address         '''
# separate the address col with the delimeter ','
df[['Street_name','City','Zip_code']]=df["Address"].str.split(',',expand=True)
df

# not needed anymore
df=df.drop(columns='Address')
df


''''        Paying Customer & Do Not Contact        '''
# replacing the values of both th col bcoz of containing same type of values

df[['Paying Customer','Do_Not_Contact']]=df[['Paying Customer','Do_Not_Contact']].replace('N','No')
df[['Paying Customer','Do_Not_Contact']]=df[['Paying Customer','Do_Not_Contact']].replace('Y','Yes')
df

# fills the null values with blank
df=df.fillna("")
df

# drops the record, if 'do_not_contact' == 'Yes' (no need to contact, useless)
for x in df.index:
    if df.loc[x,'Do_Not_Contact']=='Yes':
        df.drop(x,inplace=True)
df

# drops the index, if the value is null

# 1st way
for x in df.index:
    if df.loc[x,'Phone_Number']=='':
        df.drop(x,inplace=True)
df

# 2nd way

'''
df=df.dropna(subset='Phone_Number', inplace=True)
df
'''

# resets the index values in 0,1,2.... [bcz the index values are not continuous due to droping of the unwanted rows]
df=df.reset_index(drop=True)
df

df.to_csv(r"D:\Smpl Data Pd\Data Clean\Cleaned Customer Call List.csv",index=False)

