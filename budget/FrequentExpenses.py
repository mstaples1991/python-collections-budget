from . import Expense
import collections
import matplotlib.pyplot as plt

# Call the Expenses constructor
expenses = Expense.Expenses()

# Call read_expenses and pass in the name of the file
expenses.read_expenses("data/spending_data.csv")

# Create an empty list
spending_categories = []

# Create a for loop that loops through expenses.list
# Inside the loop, append expense category to spending_categories list
for expense in expenses.list:
    spending_categories.append(expense.category)

# We want to use Counter() to count which categories had the most purchases
spending_counter = collections.Counter(spending_categories)

print(spending_counter)

# Get the Top 5 Categories
top5 = spending_counter.most_common(5)

# Convert top5 list into 2 lists
# Using zip(*top5) separates the keys and values of the top5 list into 2 separate lists
# Then we store the results in two variables
categories, count = zip(*top5)

# Initialize fig as the Figure (top level container for our graph)
# Initialize ax as the Axes (contains the actual figure elements)
fig, ax = plt.subplots()

# Create the bar chart
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

# Display the graph
plt.show()
