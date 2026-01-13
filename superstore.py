import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\sahil\Downloads\archive\Sample - Superstore.csv", encoding='latin-1')

# Basic info
print(df.head())
print(df.info())

# Cleaning column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Check missing values
print(df.isnull().sum())

# Sales statistics
print("Mean Sales:", df['sales'].mean())
print("Variance of Sales:", df['sales'].var())

# Top 10 products by sales
top_products = df.groupby('product_name')['sales'].sum().sort_values(ascending=False).head(10)

plt.figure()
top_products.plot(kind='bar')
plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")
plt.xticks(rotation=75)
plt.show()

# Monthly sales trend
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.month

monthly_sales = df.groupby('month')['sales'].sum()

plt.figure()
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Outlier detection using IQR
Q1 = df['sales'].quantile(0.25)
Q3 = df['sales'].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df['sales'] < Q1 - 1.5 * IQR) | (df['sales'] > Q3 + 1.5 * IQR)]
print("Number of outliers:", outliers.shape[0])
