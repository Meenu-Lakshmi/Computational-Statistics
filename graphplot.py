import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(10,0,10)
y = x**2;
plt.figure(figsize=(10,5))
plt.title("Graph")
plt.plot(x,y,marker='*',linestyle='dotted',color='r',ms=10,mec='#070707',mfc='r')
plt.show()
