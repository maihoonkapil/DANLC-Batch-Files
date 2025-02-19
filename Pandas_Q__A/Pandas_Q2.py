import pandas as pd
import matplotlib.pyplot as plt

# URL of the CSV file
url = "C:\\Users\\Prashant Khatri\\OneDrive\\Desktop\\DANLC recording classes\\Python\\customer_data.csv"

# Read the CSV file
data = pd.read_csv(url)

# Check the contents of the DataFrame
print(data)

# Prepare the data for the pie chart
marital_counts = data['Marital_status'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(marital_counts, labels=marital_counts.index, autopct='%1.1f%%', startangle=140, colors=['#1f77b4', '#ff7f0e'])

# Add a title
plt.title('Marital Status Wise Customer Count')

# Show the chart
plt.show()