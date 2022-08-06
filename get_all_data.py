from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import os
import time
start_time = time.time()

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
states.sort()

file_path ="./statistics/"
req = Request("https://www.johnstonsarchive.net/policy/abortion/")
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")

# https://stackoverflow.com/a/68426172
links = {i["href"] for i in soup.select("[href^='usa/']")}
links = list(links)
links.sort()

# print(links[0][-7:-5])
# print(links[0])
# print(links)

res = {states[i]: links[i] for i in range(len(states))}

for key, value in res.items():
    print(key, ' : ', value)

isExist = os.path.exists(file_path)
if not isExist:
    os.makedirs(file_path)
    

url = "http://www.johnstonsarchive.net/policy/abortion/"
i = 0
for key, value in res.items():
    # remove to get all states
    if int(i) >= 0 and int(i)<=10:
        table=pd.read_html(f"{url}{value}")
        table = table[0]
        table = table[["year","abortionrate,residents","abortion rate, merged"]]
        table.columns = ['Year',  'Abortion rate', 'Abortion rate (Guttmacher)']
        table["Abortion rate"]=table["Abortion rate"].astype(str).replace(r'[()]+', '', regex=True)
        table["Abortion rate (Guttmacher)"]=table["Abortion rate (Guttmacher)"].astype(str).replace(r'[()]+', '', regex=True)
        table = table.iloc[:-2]
        table.to_csv(f"statistics/{key}.csv", index=False)
    i = i+1
    

print("Time: %s seconds" % (time.time() - start_time))
