import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
lm=LinearRegression()
df=pd.read_csv(r"C:\Users\acer\python workspace\authors_listing.csv")
#print(df)
#X=df[["daily_read","efficiency"]]
X=df[["daily_read"]]
Y=df["percentage"]
lm.fit(X,Y)
print("intercept=",lm.intercept_)
print("coefficient=",lm.coef_)
yhat= lm.predict(X)
#print(yhat[:])
#sns.regplot(x='daily_read',y='percentage',data=df)
#sns.residplot(x='daily_read',y='percentage',data=df)
ax1 = sns.distplot(df['percentage'], hist=False, color="r", label="Actual Value")
sns.distplot(yhat, hist=False, color="b", label="Fitted Values" , ax=ax1)
plt.legend()
plt.show()

