import matplotlib.pyplot as plt

# Q1: Create a line chart for x=[1,2,3,4] and y=[10,20,15,25]

x = [1,2,3,4]
y = [10,20,15,25]
plt.plot(x,y, marker='o')
plt.title("Q1 Line Chart")
plt.show()

# Output: Line connecting points (1,10),(2,20),(3,15),(4,25)

# Q2: Create a bar chart for same data

plt.bar(x,y, color='orange')
plt.title("Q2 Bar Chart")
plt.show()

# Output: Vertical bars for each x value

# Q3: Create a scatter plot

plt.scatter(x,y, color='red')
plt.title("Q3 Scatter Plot")
plt.show()

# Output: Points plotted individually showing relationship

# Q4: Create a pie chart for data=[40,30,20,10]

data = [40,30,20,10]
labels = ["W","X","Y","Z"]
plt.pie(data, labels=labels, autopct="%1.1f%%")
plt.title("Q4 Pie Chart")
plt.show()

# Output: Pie showing percentage distribution of 4 categories

# Q5: Create histogram for ages=[22,25,22,30,25,28,22,30]

ages = [22,25,22,30,25,28,22,30]
plt.hist(ages, bins=5, color='cyan', edgecolor='black')
plt.title("Q5 Histogram")
plt.show()

# Output: Histogram showing frequency of ages in bins
