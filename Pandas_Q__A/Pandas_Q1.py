import pandas as pd
import matplotlib.pyplot as plt

# URL of the CSV file
url = "C:\\Users\\Prashant Khatri\\OneDrive\\Desktop\\DANLC recording classes\\Python\\student_data.csv"

# Read the CSV file
data = pd.read_csv(url)

# Display the DataFrame (optional)
print("City-wise Student Count:")
print(data)

# Count the occurrences of each major (or another column based on your needs)
major_counts = data['Major'].value_counts()

# Plotting the data
plt.figure(figsize=(8, 8))
plt.pie(major_counts, labels=major_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Students by Major")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the plot
plt.show()
