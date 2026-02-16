import matplotlib.pyplot as plt

# Sample data

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# 1️ Line Plot

plt.plot(x, y, marker='o', color='blue')
plt.title("Line Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# Output Description:
# Line chart shows trend of y vs x. Points connected by line with markers.

# 2️ Bar Chart

plt.bar(x, y, color='green')
plt.title("Bar Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# Output Description:
# Bar chart represents y values for each x category as vertical bars.

# 3️ Scatter Plot

plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# Output Description:
# Scatter plot shows relationship between x and y with individual points.

# 4️ Pie Chart

labels = ["A", "B", "C", "D"]
data = [30, 25, 25, 20]

plt.pie(data, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()

# Output Description:
# Pie chart shows percentage distribution of each category.

# 5️ Histogram

ages = [22, 25, 22, 30, 25, 28, 22, 30]
plt.hist(ages, bins=5, color='purple', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Age bins")
plt.ylabel("Frequency")
plt.show()

# Output Description:
# Histogram shows frequency distribution of ages across bins.

print("\n--- Day 14 Data Visualization Complete ---")
