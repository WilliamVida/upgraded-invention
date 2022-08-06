import pandas as pd

url = "https://www.johnstonsarchive.net/policy/abortion/usa/ab-usa-AL.html"
table = pd.read_html(url)
table = table[0]

table = table[["year", "live births","abortionrate,residents", "abortion rate, merged"]]
table.columns = ["Year", "Live births","Abortion rate", "Abortion rate (Guttmacher)"]

# https://stackoverflow.com/a/20895818
table["Abortion rate"]=table["Abortion rate"].astype(str).replace(r'[()]+', '', regex=True)
table["Abortion rate (Guttmacher)"]=table["Abortion rate (Guttmacher)"].astype(str).replace(r'[()]+', '', regex=True)

print(table)

table = table.iloc[:-2]
table.to_csv("test.csv", index=False)
