import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data =requests.get(url).text
#print(data)
soup=BeautifulSoup(data,"html5lib")
netflix_data =pd.DataFrame(columns=["Date","Open","High","Low"])
for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text  
    netflix_data = pd.concat([netflix_data,pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low]})], ignore_index=True)
print(netflix_data.head())                                                 