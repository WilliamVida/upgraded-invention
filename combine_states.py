import os
import glob
from traceback import print_tb
import pandas as pd

os.chdir("./statistics/by state")
extension = "csv"

# https://stackoverflow.com/a/46751737
all_states = [i for i in glob.glob("*.{}".format(extension))]
l = []

# Get all CSV files.
for file_ in all_states:
    df = pd.read_csv(file_, index_col=None, header=0)
    l.append(df)

# Combine all the states.
df = pd.concat(l, ignore_index=True, sort=False)

# Do not include rows containing not a number.
df = df[df["Abortion rate (Guttmacher)"].notna()]

# Output to a CSV.
df.to_csv("../all states/All States Abortion Rate.csv",
          index=False, encoding="utf-8-sig")
