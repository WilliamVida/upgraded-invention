import pandas as pd

# Read the CSVs.
csv1 = pd.read_csv("./statistics/all states/All States Abortion Rate.csv")
csv2 = pd.read_csv(
    "./statistics/all states/All States Presidential Election Results.csv")

# Merge the CSVs.
new_csv = csv1.merge(csv2, on=["State", "Year"])

# Output the combined DataFrame to a CSV.
new_csv.to_csv(
    "./statistics/all states/All States Abortion Rate and Presidential Election Results.csv", index=False)
