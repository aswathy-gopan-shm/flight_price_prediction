import sys
import numpy as np
import pandas as pd


df = pd.read_csv("data/flight_dataset.csv")

print(df["source_city"].unique())
print(df["destination_city"].unique())
print(df["class"].unique())
flight = df["flight"].unique()
print(np.size(flight))
