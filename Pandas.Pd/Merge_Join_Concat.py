"""  Merge, Join & Concat  """

import pandas as pd
import numpy as np

df1=pd.read_csv(r"D:\Smpl Data Pd\LOTR.csv")
df1

df2=pd.read_csv(r"D:\Smpl Data Pd\LOTR 2.csv")
df2

'''     Merge    '''
df1.merge(df2)   # merges the data which matches the column in both datasets(like inner-join)

df1.merge(df2, how="left")  # left merge
df1.merge(df2, how="right")  # right merge
df1.merge(df2, how="inner")   # inner merge
df1.merge(df2, how="outer")   # outer merge
df1.merge(df2, how="cross")   # data from df1 will cross merges with all the datas in the df2

df1.merge(df2, how="inner", on=["FellowshipID","FirstName"])   # merges the data with the given column
df1.merge(df2, how="outer")

'''     Replacing 'Nan'     '''

merge=df1.merge(df2, how="outer")
merge

merge.replace({np.nan:' ---MISSING--- '})

'''     JOINS       '''
df1.join(df2, how="outer", on='FellowshipID', lsuffix='_Left', rsuffix='_Right')

# outer join
# better version of join (easy to understand)
df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), how='outer', lsuffix='_Left', rsuffix='_Right')
df4.replace({np.nan:"__Missing__"})

# inner join
df7 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'),how='inner', lsuffix='_Left', rsuffix='_Right')
df7

# left join
df5 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), how='left', lsuffix='_Left', rsuffix='_Right')
df5.replace({np.nan:"__Missing__"})

# right join
df6 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), how='right', lsuffix='_Left', rsuffix='_Right')
df6.replace({np.nan:"__Missing__"})

'''    Concat        '''
# even though there is common data/column in the tables, it concat 'df1' under 'df2' table (one on top of the other)
pd.concat([df1,df2])   # basically outer concat

# concats with the common col in both the tables
pd.concat([df1,df2], join="inner")

# axis = 0 ---> row(top-bottom) it's default
# axis = 1 ---> column(left-right)

pd.concat([df1,df2], join="outer", axis=1)  # concats based on index(0,1,2,3..)


