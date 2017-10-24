import numpy as np
import matplotlib.pyplot as pl


# Load data
OriginalData = np.loadtxt("Iris.csv",str, delimiter=",", skiprows=1, unpack=True)
# Transposing the data
data = OriginalData.transpose()
# get each column
petal_length = petal_width = species =[]


petal_length = np.array(petal_length).astype(np.float)
petal_width = np.array(petal_width).astype(np.float)
m,c=np.polyfit(petal_length, petal_width, 1)

print("m is %8.6f and c is %6.6f." % (m, c))

# Create the plot.
pl.plot(petal_length, m * petal_length + c, 'b-')
pl.plot(petal_length, petal_width, 'k.')

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

pl.xlabel('petal length')
pl.ylabel('petal width')


pl.show()