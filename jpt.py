import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
apple = yf.Ticker("AAPL")
print(apple)
print(apple.info["country"])
spd= apple.history()
#print(spd)
spd_max= apple.history(period="max")
#print(spd_max)
#print(spd_max.head())
#print(apple.actions)
#print(apple.dividends)
plt.plot(spd)
plt.xlabel("Date")
plt.ylabel("Open")
plt.show()







