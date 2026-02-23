



import pandas as pd

# head(), tail(n)


df = pd.read_csv("output.csv")
print(df)

df1 = df.head(2)
print(df1)


df2 = df.tail(2)
print(df2)

print(df2.shape)

print("Describe",df2.describe())


# We know cloumns , rows,   What type of data , missing data , datatypes, cloumn name, Memary usage of dataframe


dff= pd.read_csv("peopleData.csv")
print("Displaying the data sets")
print(dff.info())




data1 = {
    'CustomerID': [101, 102, 103, 104, 105],
    'Name': ['Alice Smith', 'Bob Johnson', 'Charlie Lee', 'Diana King', 'Evan Kim'],
    'Age': [25, 34, 29, 42, 31],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'PurchaseAmount': [250.75, 489.50, 330.00, 120.99, 560.40],
    'Membership': ['Gold', 'Silver', 'Gold', 'Platinum', 'Silver']
}


df9 = pd.DataFrame(data1)
print("My data sets is with all info",df9.info())

print("Describe",df9.describe())
print(df2.shape)
