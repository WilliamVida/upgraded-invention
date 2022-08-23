import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from urllib.request import urlopen
import re

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

folder = "./statistics/presidential election by year/"
isExist = os.path.exists(folder)
if not isExist:
    os.makedirs(folder)

url = "https://en.wikipedia.org/wiki/List_of_United_States_presidential_election_results_by_state"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.select("a")
election_years = set()

# Get the presidential election years.
for link in links:
    if link.get("href") != None and "_United_States_presidential_election" in link.get("href"):
        a = link.text
        if a.isdigit() is True:
            election_years.add(a)

election_years = list(election_years)

# Keep elections after a certain year.
election_years_used = [i for i in election_years if i >= "1972"]
election_years_used.sort()

wiki_elections = [
    f"https://en.wikipedia.org/wiki/{year}_United_States_presidential_election" for year in election_years_used]
wiki_elections.sort()

for count, link in enumerate(wiki_elections):
    # Get the current link.
    soup = BeautifulSoup(urlopen(link), "lxml")

    # Find all tables with a certain class.
    tables = soup.find_all("table", class_="wikitable sortable")

    for table in tables:
        if table.findParent("table") is None:
            temp_table = pd.read_html(str(table))[0]
            # -------------- !!! Use a better way to check for the correct table. !!! --------------
            # Maybe find "Results by state" in page?
            # If the table is the correct one, then use it.
            if temp_table.iloc[:, 0].str.contains("D.C.").any() or temp_table.iloc[:, 0].str.contains("District of Columbia").any():
                table = pd.read_html(str(table))[0]
                table = pd.DataFrame(table)
                table.iloc[:, list(range(8))]

                # Join the first and second row.
                table.columns = table.columns.map("_".join).astype(str)

                # Rename the first column.
                table.rename(columns={table.columns[0]: "State"}, inplace=True)

                # Rename the columns.
                # https://stackoverflow.com/a/65332240
                table = table.rename(
                    columns=lambda c: "Democratic Vote" if c.endswith("Democratic_%") else c)
                table = table.rename(
                    columns=lambda c: "Republican Vote" if c.endswith("Republican_%") else c)
                table = table[["State", "Democratic Vote", "Republican Vote"]]

                # Remove square brackets and their contents.
                # https://stackoverflow.com/a/42324475
                table["State"] = [re.sub(r"\[[^]]*\]", "", str(x))
                                  for x in table["State"]]

                # Remove not a number rows.
                table = table[table["Democratic Vote"].notna()]

                # Remove certain rows as they contain the districts.
                # https://www.geeksforgeeks.org/how-to-drop-rows-that-contain-a-specific-string-in-pandas/
                table = table[table["State"].str.contains(
                    "1|2|3|4|5") == False]

                # Remove percentage sign.
                table["Democratic Vote"] = table["Democratic Vote"].astype(
                    str).str.replace("%", "")
                table["Republican Vote"] = table["Republican Vote"].astype(
                    str).str.replace("%", "")

                # Keep the headers and all 50 + 1 states and delete everything after that.
                table = table.iloc[:51]

                # table["State"] = table["State"].str.replace("District of Columbia", "D.C.")

                # Rename the states.
                table["State"] = states
                
                # Insert the year.
                table.insert(1, "Year", election_years_used[count])

                table.to_csv(
                    f"{folder}{election_years_used[count]}.csv", index=False)
