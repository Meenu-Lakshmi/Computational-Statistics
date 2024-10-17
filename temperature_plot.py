import pandas as pd
import matplotlib.pyplot as plt
url = "(link unavailable)"
data = pd.read_csv("lois_continuous")
swale_data = data[data['Location'] == 'Swale at Catterick Bridge']
mean_temp = swale_data['Temperature'].mean()
print(f"Mean Temperature: {mean_temp}°C")
median_do = swale_data['Dissolved Oxygen'].median()
print(f"Median Dissolved Oxygen: {median_do} mg/L")
plt.figure(figsize=(10, 6))
plt.hist(swale_data['Temperature'], bins=20, edgecolor='black')
plt.title('Temperature Distribution at Swale at Catterick Bridge')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.show()
