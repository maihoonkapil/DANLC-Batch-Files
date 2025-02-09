import numpy as np
import matplotlib.pyplot as plt

# Input Data
months = np.arange(1, 13)
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Plotting
plt.figure(figsize=(10, 6)) 
plt.suptitle('Sales Performance by Product Categories', fontsize=16)

# Electronics
plt.subplot(2, 2, 1)
plt.plot(months, electronics_sales, marker='o', color='blue')
plt.title('Electronics')
plt .xlabel('Month')
plt.ylabel('Sales Amount')

# Clothing
plt.subplot(2, 2, 2)
plt.plot(months, clothing_sales, marker='o', color='green')
plt.title('Clothing')
plt.xlabel('Month')
plt.ylabel('Sales Amount')

# Home & Garden
plt.subplot(2, 2, 3)
plt.plot(months, home_garden_sales, marker='o', color='red')
plt.title('Home & Garden')
plt.xlabel('Month')
plt.ylabel('Sales Amount')

# Sports & Outdoors
plt.subplot(2, 2, 4)
plt.plot(months, sports_outdoors_sales, marker='o', color='purple')
plt.title('Sports & Outdoors')
plt.xlabel('Month')
plt.ylabel('Sales Amount')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Leave space for the main title

# Show the plots
plt.show()