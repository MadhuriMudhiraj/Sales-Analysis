import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Load dataset
df = pd.read_csv("train.csv", encoding="latin1")

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
print("=" * 50)
print("TOTAL SALES")
print("=" * 50)

total_sales = df["Sales"].sum()
print(f"Total Sales: ${total_sales:,.2f}")

# -----------------------------
# Sales by Region
# -----------------------------
region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region")
print(region_sales)

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/sales_by_region.png")
plt.close()

# -----------------------------
# Sales by Category
# -----------------------------
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category")
print(category_sales)

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/sales_by_category.png")
plt.close()

# -----------------------------
# Top 10 Products
# -----------------------------
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Products")
print(top_products)

plt.figure(figsize=(10,6))
top_products.plot(kind="bar")
plt.title("Top 10 Products")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/top_products.png")
plt.close()

# -----------------------------
# Top 10 Customers
# -----------------------------
top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Customers")
print(top_customers)

plt.figure(figsize=(10,6))
top_customers.plot(kind="bar")
plt.title("Top 10 Customers")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/top_customers.png")
plt.close()

# -----------------------------
# Monthly Sales Trend
# -----------------------------
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12,6))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/monthly_sales_trend.png")
plt.close()

print("\nAnalysis Completed!")
print("Charts saved inside charts folder.")