import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (update the file path as per your system)
file_path = 'Dataset_Ques_1_4.csv'
data = pd.read_csv(file_path)

# a. Read Total profit of all months and show it using a line plot
months = data['month_number']
total_profit = data['total_profit']

plt.figure(figsize=(10,6))
plt.plot(months, total_profit, label='Profit')
plt.title('Total Profit Over Months')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.grid(True)
plt.legend()
plt.show()

# b. Line plot with specific style properties
plt.figure(figsize=(10,6))
plt.plot(months, total_profit, label='Profit', color='r', marker='o', linestyle='--', linewidth=3)
plt.title('Total Profit Over Months (Styled)')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.grid(True, linestyle='-.')
plt.legend()
plt.show()

# c. Multi-line plot for all product sales data
plt.figure(figsize=(10,6))
plt.plot(months, data['facecream'], label='Face Cream', marker='o')
plt.plot(months, data['facewash'], label='Face Wash', marker='x')
plt.plot(months, data['toothpaste'], label='Toothpaste', marker='s')
plt.plot(months, data['bathingsoap'], label='Bathing Soap', marker='D')
plt.plot(months, data['shampoo'], label='Shampoo', marker='*')
plt.plot(months, data['moisturizer'], label='Moisturizer', marker='^')
plt.title('Product Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.legend()
plt.grid(True)
plt.show()

# d. Scatter plot for toothpaste sales
plt.figure(figsize=(10,6))
plt.scatter(months, data['toothpaste'], color='green')
plt.title('Toothpaste Sales Over Months')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.grid(True)
plt.show()

# e. Bar chart for face cream and face wash
plt.figure(figsize=(10,6))
plt.bar(months - 0.2, data['facecream'], width=0.4, label='Face Cream', color='blue')
plt.bar(months + 0.2, data['facewash'], width=0.4, label='Face Wash', color='orange')
plt.title('Face Cream and Face Wash Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.legend()
plt.show()

# f. Bar chart for bathing soap sales and saving to disk
plt.figure(figsize=(10,6))
plt.bar(months, data['bathingsoap'], color='purple')
plt.title('Bathing Soap Sales Over Months')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.grid(True)
plt.savefig('bathing_soap_sales.png')
plt.show()

# g. Histogram for total profit of each month
plt.figure(figsize=(10,6))
plt.hist(total_profit, bins=5, color='skyblue', edgecolor='black')
plt.title('Total Profit Distribution')
plt.xlabel('Profit Range')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# h. Pie chart for total sales of each product
total_sales = [
    data['facecream'].sum(),
    data['facewash'].sum(),
    data['toothpaste'].sum(),
    data['bathingsoap'].sum(),
    data['shampoo'].sum(),
    data['moisturizer'].sum()
]
products = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.figure(figsize=(10,6))
plt.pie(total_sales, labels=products, autopct='%1.1f%%', startangle=140, colors=['blue', 'orange', 'green', 'purple', 'red', 'yellow'])
plt.title('Total Sales Distribution by Product')
plt.show()

# i. Subplot for Bathing Soap and Face Wash sales
plt.figure(figsize=(10,6))

plt.subplot(1, 2, 1)
plt.plot(months, data['bathingsoap'], label='Bathing Soap', color='purple', marker='o')
plt.title('Bathing Soap Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(months, data['facewash'], label='Face Wash', color='orange', marker='o')
plt.title('Face Wash Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.grid(True)

plt.tight_layout()
plt.show()

# j. Stack plot for all product sales data
plt.figure(figsize=(10,6))
plt.stackplot(months, data['facecream'], data['facewash'], data['toothpaste'], data['bathingsoap'], data['shampoo'], data['moisturizer'],
              labels=['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer'], colors=['blue', 'orange', 'green', 'purple', 'red', 'yellow'])
plt.title('Stacked Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.legend(loc='upper left')
plt.show()
