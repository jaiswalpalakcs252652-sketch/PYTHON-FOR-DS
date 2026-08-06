import matplotlib.pyplot as plt
import numpy as np

# Question 1: Line Plot Basics
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(6, 4))
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("Numbers")
plt.ylabel("Doubles")
plt.show()

# Question 2: Customize a Line Plot
plt.figure(figsize=(6, 4))
plt.plot(x, y, color="red", linestyle="--", marker="o")
plt.title("Customized Line Plot")
plt.xlabel("Numbers")
plt.ylabel("Doubles")
plt.show()

# Question 3: Bar Chart
categories = ["Data Structures", "Scala for DS", "Operating System", "Python for DS"]
scores = [65, 70, 74, 60]

plt.figure(figsize=(8, 5))
plt.bar(categories, scores)
plt.title("Student Scores")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.show()

# Question 4: Horizontal Bar Chart
plt.figure(figsize=(8, 5))
plt.barh(categories, scores)
plt.title("Student Scores")
plt.xlabel("Scores")
plt.ylabel("Subjects")
plt.show()

# Question 5: Pie Chart
explode = (0, 0, 0, 0.1)

plt.figure(figsize=(6, 6))
plt.pie(scores, labels=categories, autopct="%1.1f%%", explode=explode)
plt.title("Student Scores Distribution")
plt.show()

# Question 6: Scatter Plot
x = [5, 7, 8, 7, 6, 9, 5]
y = [99, 86, 87, 88, 100, 86, 103]

plt.figure(figsize=(6, 4))
plt.scatter(x, y, color="green", s=100)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# Question 7: Histogram
data = np.random.normal(0, 1, 100)

plt.figure(figsize=(6, 4))
plt.hist(data, bins=20)
plt.grid(True)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Question 8: Four Subplots (2x2 Grid)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

axs[0, 0].plot(x, y)
axs[0, 0].set_title("Line Plot")

categories = ["DS", "Scala", "OS", "Python"]
scores = [65, 70, 74, 60]

axs[0, 1].bar(categories, scores)
axs[0, 1].set_title("Bar Chart")

x_scatter = [5, 7, 8, 7, 6, 9, 5]
y_scatter = [99, 86, 87, 88, 100, 86, 103]

axs[1, 0].scatter(x_scatter, y_scatter, color="green")
axs[1, 0].set_title("Scatter Plot")

data = np.random.normal(0, 1, 100)

axs[1, 1].hist(data, bins=20)
axs[1, 1].grid(True)
axs[1, 1].set_title("Histogram")

plt.tight_layout()
plt.show()

# Question 9: Monthly Sales Comparison (2023 vs 2024)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_2023 = [150, 200, 250, 300, 280, 350]
sales_2024 = [180, 220, 270, 320, 300, 400]

plt.figure(figsize=(8, 5))

plt.plot(
    months,
    sales_2023,
    color="blue",
    linestyle="--",
    marker="o",
    label="Sales 2023"
)

plt.plot(
    months,
    sales_2024,
    color="green",
    linestyle="-",
    marker="s",
    label="Sales 2024"
)

highest = max(sales_2024)
index = sales_2024.index(highest)

plt.annotate(
    "Highest Sales",
    xy=(months[index], highest),
    xytext=(months[index], highest + 30),
    arrowprops=dict(arrowstyle="->")
)

plt.title("Monthly Sales Comparison (2023 vs 2024)")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()

plt.savefig("sales_comparison.png")
plt.show()
