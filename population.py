import numpy as np
population = np.array([4779736,710231,6392017,2915918,37253956,5029196,3574097,897934])

mean_population = np.mean(population)
median_population = np.median(population)
variance_population = np.var(population) 

print(f"Population Mean: {mean_population}")
print(f"Population Median: {median_population}")
print(f"Population Variance: {variance_population}") 
