from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import os

file_path = "./statistics/abortion rate by state"
isExist = os.path.exists(file_path)
if not isExist:
    os.makedirs(file_path)

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

url = "http://www.johnstonsarchive.net/policy/abortion/"
req = Request(url)
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")

# https://stackoverflow.com/a/68426172
# Find links that direct to each state, and declare it as a set to remove any duplicates.
# links = {i["href"] for i in soup.select("[href^='usa/']")}
# links = list(links)
# links.sort()

# Other method. Remove {url} in for loop to use.
links = [f"http://www.johnstonsarchive.net/policy/abortion/usa/ab-usa-{state}.html" for state in states]

# Turn the states and links to a dict.
states_and_links = {states[i]: links[i] for i in range(len(states))}

for key, value in states_and_links.items():
    print(key, ":", value)

i = 0
for key, value in states_and_links.items():
    # remove if to get all states
    # if int(i) >= 0 and int(i) <= 9 and key != "DC":
    table = pd.read_html(f"{value}")
    table = table[0]

    # Get the columns from the table and rename them.
    table = table[["year", "abortion rate, merged"]]
    table.columns = ["Year", "Abortion Rate (Guttmacher)"]

    # Change the format of the table.
    table.insert(0, "State", key)

    # Replace any brackets in the column.
    table["Abortion Rate (Guttmacher)"] = table["Abortion Rate (Guttmacher)"].astype(
        str).replace(r"[()]+", "", regex=True)

    # Drop the last two rows as they are irrelevant.
    table = table.iloc[:-2]
    table.to_csv(f"{file_path}/{key}.csv", index=False)
    print("Downloaded:", key)
    # i = i + 1
