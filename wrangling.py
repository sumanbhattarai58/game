import pandas as pd
import numpy as np
url=" https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df=pd.read_csv(url)
headers=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
df=pd.read_csv(url,names=headers) #header=None pani rakhna milxa
df.replace("?",np.nan, inplace=True)
#miss=df.isnull()
#print(miss.head())
newloss=df["b"].astype("float").mean(axis=0)
df["b"].replace(np.nan, newloss, inplace=True)
print(df.head())