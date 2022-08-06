from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import requests
import time
start_time = time.time()

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
states.sort()

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


# https://www.johnstonsarchive.net/policy/abortion/usa/ab-usa-AL.html
url = "http://www.johnstonsarchive.net/policy/abortion/"
i = 0
for key, value in res.items():
    # remove to get al states
    if int(i) >= 0 and int(i) <=10:
        table=pd.read_html(f"http://www.johnstonsarchive.net/policy/abortion/{value}")
        table = table[0]
        table = table[["year","live births","abortionrate,residents","abortion rate, merged"]]
        table.columns = ['Year', 'Live births', 'Abortion rate', 'Abortion rate (Guttmacher)']
        table["Abortion rate"]=table["Abortion rate"].astype(str).replace(r'[()]+', '', regex=True)
        table["Abortion rate (Guttmacher)"]=table["Abortion rate (Guttmacher)"].astype(str).replace(r'[()]+', '', regex=True)
        table = table.iloc[:-2]
        table.to_csv(f"statistics/{key}.csv", index=False)
    i = i+1


table.to_csv("test.csv", index=False)


# table = table[0]
# table = table[["year","live births","abortionrate,residents","abortion rate, merged"]]
# table.columns = ['Year', 'Live births', 'Abortion rate', 'Abortion rate (Guttmacher)']
# table = table.iloc[:-2]
# table.to_csv("statistics/Alabama.csv", index=False)


print("Time: %s seconds" % (time.time() - start_time))


# test = dict.fromkeys(links, states)
# res = {states[i]: links[i] for i in range(len(links))}
# print(test)
