import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file = 'lois_continuous.csv'
data = pd.read_csv(file)

# Filter data for "Swale at Catterick Bridge" location
swale_data = data[data['SITE_NAME'] == 'Swale at Catterick Bridge']

# Calculate mean temperature and median dissolved oxygen
mean_temperature = swale_data['Temperature'].mean()
median_dissolved_oxygen = swale_data['Oxygen'].median()

# Print the calculated values
print(f"Mean Temperature: {mean_temperature} °C")
print(f"Median Dissolved Oxygen: {median_dissolved_oxygen} mg/L")

# Plot histogram of temperature
plt.figure(figsize=(10,6))
plt.hist(swale_data['Temperature'], bins=20, color='skyblue', edgecolor='black')
plt.title('Temperature Distribution at Swale at Catterick Bridge')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
