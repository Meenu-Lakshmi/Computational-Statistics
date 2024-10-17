import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (update the file path as per your system)
file_path = 'BankChurners.csv'  # Replace with the path to your downloaded dataset
data = pd.read_csv(file_path)

# 1. Identify any missing values within the dataset and address them
missing_values = data.isnull().sum()
print("Missing Values:\n", missing_values)

# If you need to fill or drop missing values (if applicable):
# data = data.fillna(method='ffill')  # or use other appropriate methods
# data = data.dropna()  # If you want to drop rows with missing values

# 2. Present the ratio of Attrition_Flag through a bar chart
plt.figure(figsize=(8,6))
data['Attrition_Flag'].value_counts().plot(kind='bar', color=['green', 'red'])
plt.title('Attrition Flag Distribution')
plt.xlabel('Attrition Flag')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# 3. Bar charts and box plots for categorical variables
categorical_cols = ['Gender', 'Education_Level', 'Marital_Status', 'Card_Category']

# Bar charts for categorical variables
for col in categorical_cols:
    plt.figure(figsize=(8,6))
    data[col].value_counts().plot(kind='bar', color='blue')
    plt.title(f'{col} Distribution')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# Box plots for categorical variables vs. Credit Limit
for col in categorical_cols:
    plt.figure(figsize=(8,6))
    sns.boxplot(x=col, y='Credit_Limit', data=data)
    plt.title(f'{col} vs. Credit Limit')
    plt.xticks(rotation=45)
    plt.show()

# 4. Compute descriptive statistics for the dataframe
desc_stats = data.describe()
print("\nDescriptive Statistics:\n", desc_stats)

# 5. Utilize a heatmap to determine the correlation coefficient
plt.figure(figsize=(12,8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Coefficient Heatmap')
plt.show()

# 6. Eliminate any unnecessary columns from the dataset
# Assume that 'CLIENTNUM' is an unnecessary column
data_cleaned = data.drop(columns=['CLIENTNUM'])

print("\nColumns after removal:\n", data_cleaned.columns)
