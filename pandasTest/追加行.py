import pandas as pd


a=pd.Series([1,2,4,"hh"])
df=pd.DataFrame()
print(df.append(a,ignore_index=True))
