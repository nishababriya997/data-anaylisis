import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales.csv")

print("Original Data:")
print(df)

grouped_data = df.groupby("Department")["Sales"].sum()

print("\nTotal Sales by Department:")
print(grouped_data)

grouped_data.plot(kind="bar")

plt.title("Total Sales by Department")
plt.xlabel("Department")
plt.ylabel("Total Sales")
plt.show()