



# Pandas for data anlysis and data manupulation 
# Pandas is an open-source data analysis and manipulation library for Python.
# It's widely used in data science, machine learning
# Real life use- Finance , Healthcare, Retails
import pandas as pd

list = [1,2,3,4,5,6,7,8,9]



# Read Data from csv file into a dataframe
df = pd.read_csv("/Users/hanumantbhojane/Desktop/pythonPractice/data1.csv")
print(df)



data = {
    'CustomerID': [101, 102, 103, 104, 105],
    'Name': ['Alice Smith', 'Bob Johnson', 'Charlie Lee', 'Diana King', 'Evan Kim'],
    'Age': [25, 34, 29, 42, 31],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'PurchaseAmount': [250.75, 489.50, 330.00, 120.99, 560.40],
    'Membership': ['Gold', 'Silver', 'Gold', 'Platinum', 'Silver']
}

df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.describe())


df.to_csv("output1.csv", index=False)
df.to_excel("output1.xlsx", index=False)
df.to_json("output1.json", index=False)



