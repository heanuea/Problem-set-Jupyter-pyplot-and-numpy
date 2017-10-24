import numpy as np
import matplotlib.pyplot as pl

pl.rcParams['figure.figsize'] = (16.0, 8.0)


# Load data
OriginalData = np.loadtxt("Iris.csv",str, delimiter=",", skiprows=1, unpack=True)
# Transposing the data
data = OriginalData.transpose()
# get each column
sepal_length = sepal_width = petal_length = petal_width = species =[]
sepal_length , sepal_width , petal_length , petal_width , species = OriginalData


# Create the plot.
pl.scatter(sepal_length, sepal_width, c='pink')

# Set properties.
pl.xlabel('sepal length')
pl.ylabel('sepal width')

# Display plots .
pl.title('TITLE')
pl.show()