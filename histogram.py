import matplotlib.pyplot as plt
heights = [170,166,177,181,162,157,172,168,175,174,162,169,171,179]
plt.hist(heights,bins=5,edgecolor='#000000',color='green')
plt.xlabel('Heights (cm)')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
