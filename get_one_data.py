import pandas as pd
import os

file_path = "./statistics/"
url = "https://www.johnstonsarchive.net/policy/abortion/usa/ab-usa-AL.html"
table = pd.read_html(url)
table = table[0]

table = table[["year",  "abortionrate,residents", "abortion rate, merged"]]
table.columns = ["Year", "Abortion rate", "Abortion Rate (Guttmacher)"]

# https://stackoverflow.com/a/20895818
table["Abortion rate"] = table["Abortion rate"].astype(
    str).replace(r'[()]+', '', regex=True)
table["Abortion Rate (Guttmacher)"] = table["Abortion Rate (Guttmacher)"].astype(
    str).replace(r'[()]+', '', regex=True)

print(table)
table = table.iloc[:-2]

isExist = os.path.exists(file_path)
if not isExist:
    os.makedirs(file_path)

table.to_csv(file_path+"AL.csv", index=False)
