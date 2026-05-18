
import pandas as pd
import numpy as np

df = pd.read_csv("swiggy_zomato_data.csv")


print(df.head())

print("\nNull Values Before Cleaning:\n")
print(df.isnull().sum())


amount_order_columns = [
    "amount",
    "total_amount",
    "order_amount",
    "orders",
    "no_of_orders"
]


for col in amount_order_columns:

    if col in df.columns:

        avg_value = df[col].mean()

        df[col].fillna(avg_value, inplace=True)



print("\nNull Values After Cleaning:\n")
print(df.isnull().sum())


print("\nCleaned Dataset:\n")
print(df.head())



df.to_csv("cleaned_shopping_data.csv", index=False)

print("\nDataset cleaned and saved successfully.")