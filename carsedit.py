import pandas as pd
df=pd.read_excel(r"C:\Users\acer\python workspace\cars.xlsx")
df["place"]=["ktm","bkt","ltr","uda","dha"]
df.loc[len(df)] = ["honda","white", 28,'John', 'Nepal']
df.index=["a","b","c","d","e","f"]
print(df.iloc[4,3])
print(df.loc["a","price"])
df.iloc[4,2]=24
print(df)