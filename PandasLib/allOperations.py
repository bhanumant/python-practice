
import pandas as pd

# View Data

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

print(df.head())        # First 5 rows
print(df.tail())        # Last 5 rows
print(df.info())        # Summary
print(df.describe())    # Stats summary
print(df.shape)         # Rows, columns



# Read Data
# df6 = pd.read_csv('data1.csv')         # Read CSV file
# df7 = pd.read_excel('output.xlsx')      # Read Excel file


data2 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df2 = pd.DataFrame(data2)
print(df2)



# Accessing coloumn and rows

print(df["Name"])
print(df[[ "Name", "Age", "City"]])
print(df.loc[0])
print(df.iloc[0])



# Filtering Data

print(df[df['Age'] > 30])
print(df[df['Age'] < 30])
print(df[(df['Age'] > 25) & (df['Name'] != 'Bob')])




# Sorting
print(df.sort_values( by='Age', ascending=True))
