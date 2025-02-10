import pandas as pd
import matplotlib.pyplot as plt

sales_data = [
    {'customer_name': 'Mayank', 'product_name': 'Laptop', 'quantity': 1, 'price': 1000, 'date': '2022-01-01'},
    {'customer_name': 'Ravi', 'product_name': 'Smartphone', 'quantity': 2, 'price': 500, 'date': '2022-01-02 '},
    {'customer_name': 'Jitender', 'product_name': 'Laptop', 'quantity': 1, 'price': 1000, 'date': '2022-01-03'},
    {'customer_name': 'Himanshu', 'product_name': 'Tablet', 'quantity': 3, 'price': 200, 'date': '2022-01-04'},
    {'customer_name': 'Naresh', 'product_name': 'Laptop', 'quantity': 2, 'price': 1000, 'date': '2022-01-05'}
]

# Convert to DataFrame
df = pd.DataFrame(sales_data)

# Calculate total revenue
df['total_revenue'] = df['quantity'] * df['price']
total_revenue = df['total_revenue'].sum()

# Calculate average revenue per sale
average_revenue_per_sale = df['total_revenue'].mean()

# Identify the best-selling product
best_selling_product = df.groupby('product_name')['quantity'].sum().idxmax()

# Identify the date with the highest total revenue
date_with_highest_revenue = df.groupby('date')['total_revenue'].sum().idxmax()

# Generate bar chart for sales by product
product_sales = df.groupby('product_name')['quantity'].sum()
plt.figure(figsize=(10, 5))
product_sales.plot(kind='bar', title='Sales by Product')
plt.xlabel('Product Name')
plt.ylabel('Quantity Sold')
plt.show()

# Generate bar chart for total sales by date
date_sales = df.groupby('date')['total_revenue'].sum()
plt.figure(figsize=(10, 5))
date_sales.plot(kind='bar', title='Total Sales by Date')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.show()

# Insights
insights = {
    'Total Revenue': total_revenue,
    'Average Revenue per Sale': average_revenue_per_sale,
    'Best Selling Product': best_selling_product,
    'Date with Highest Revenue': date_with_highest_revenue
}


print(insights)