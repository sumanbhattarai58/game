import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
df=pd.read_csv(r"C:\Users\acer\python workspace\authors_listing.csv")
#print(df)
#print(df.columns)
#print(df[['daily_read','percentage']].corr())
#sns.regplot(x="daily_read",y="percentage",data=df)
#sns.boxplot(x="daily_read",y="percentage",data=df)
#sns.barplot(x="daily_read",y="percentage",data=df)
#plt.show()
#print(df.describe())
#print(df["percentage"].value_counts())
group = df[["authors","daily_read"]]
group1= group.groupby(["authors","daily_read"]).mean()
print(group1)
#pivotex = df.pivot(index="daily_read", columns="percentage")
#print(pivotex)
#pearson_coef, p_value = stats.pearsonr(df['daily_read'], df['percentage'])
#print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value) 