import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the dataset into a Pandas DataFrame
df = pd.read_csv("CSV Files/weather_data.csv")

# Use the describe() method to get basic statistics about the data
print(df.describe())

# Use the groupby() method to group the data by a specific column
grouped_data = df.groupby("Date").mean()
print(grouped_data)

# Use the pivot_table() method to create a pivot table
pivot_table = df.pivot_table(values="Temperature", index="Humidity", columns="Wind Speed")
print(pivot_table)

# Use the plot() method to create a line plot
df.plot(x="Date", y="Temperature", kind="line")
plt.show()

# Use the hist() method to create a histogram
df["Temperature"].hist()
plt.show()

# Use the scatter() method to create a scatter plot
plt.scatter(df["Humidity"], df["Wind Speed"])
plt.show()
