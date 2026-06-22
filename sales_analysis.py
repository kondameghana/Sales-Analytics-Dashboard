import pandas as pd

df = pd.read_csv("sales.csv")

# Check missing values
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')

# Fill missing postal codes
df['Postal Code'] = df['Postal Code'].fillna(0)

print("\nDataset Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)
print(df.columns.tolist())
# Total Sales
print("Total Sales:", df['Sales'].sum())

# Sales by Region
print("\nSales by Region")
print(df.groupby('Region')['Sales'].sum())

# Sales by Category
print("\nSales by Category")
print(df.groupby('Category')['Sales'].sum())

# Top 10 Products
print("\nTop 10 Products")
print(
    df.groupby('Product Name')['Sales']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)
df['Month'] = df['Order Date'].dt.month_name()
df['Year'] = df['Order Date'].dt.year
df.to_csv("clean_sales_data.csv", index=False)

print("File exported successfully!")