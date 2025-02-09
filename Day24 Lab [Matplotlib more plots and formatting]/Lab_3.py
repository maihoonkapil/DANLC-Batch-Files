import matplotlib.pyplot as plt

# Data
segments = ['Product A', 'Product B', 'Services', 'Licensing']
revenue_percentages = [45, 25, 15, 15]

# Create the pie chart
plt.pie(revenue_percentages, labels=segments, autopct='%1.1f%%', startangle=90)

# Add a title
plt.title("Distribution of Company Revenue by Business Segment")

# Ensure the circle's proportion
plt.axis('equal')

# Display the chart
plt.show()