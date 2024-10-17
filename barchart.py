import matplotlib.pyplot as plt

continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America', 'Soviet Union']
areas = [11.7, 10.4, 1.9, 9.4, 3.3, 6.9, 7.9]


plt.figure(figsize=(10, 6))
plt.bar(continents, areas, color='green')


plt.title('Areas of Various Continents (in millions of square miles)')
plt.xlabel('Continent')
plt.ylabel('Area (in millions of square miles)')


plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()       # Adjust layout to fit labels
plt.show()
