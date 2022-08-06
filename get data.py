import pandas as pd

url = "https://www.johnstonsarchive.net/policy/abortion/usa/ab-usa-AL.html"

table = pd.read_html(url)

table = table[0]

table = table[["year", "live births","abortionrate,residents", "abortion rate, merged"]]
table.columns = ['Year', 'Live births','Abortion rate', 'Abortion rate (Guttmacher)']

table = table.iloc[:-2]

table.to_csv("Alabama.csv", index=False)
