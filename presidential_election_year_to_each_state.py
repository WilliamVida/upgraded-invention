import pandas as pd
from os import listdir
from os.path import isfile, join
import os.path

folder = "./statistics/presidential election by year/"
# https://stackoverflow.com/a/3207973
election_year_files = [f for f in listdir(folder) if isfile(join(folder, f))]

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

state_election_folder = "./statistics/presidential election by state/"
isExist = os.path.exists(state_election_folder)
if not isExist:
    os.makedirs(state_election_folder)

# Create a list containing a DataFrame for each election year.
dfs = []
for file in election_year_files:
    df = pd.read_csv(folder + file, header=0)
    dfs.append(df)

# Combine all the DataFrames.
df = pd.concat((pd.read_csv(folder+f)
               for f in election_year_files), ignore_index=True)

# Sort the values.
df = df.sort_values(["State", "Year"])

# Output the DataFrame to a CSV.
df.to_csv(f"./statistics/all states/All States Presidential Election Results.csv",
          index=False, header=True)

# Create a CSV file for each state and its presidential election results.
for state in states:
    df.loc[df["State"] == state].to_csv(
        f"{state_election_folder}{state}.csv", index=False, header=True)
