import numpy as np
# genfromtxt is a numpy method and delimiter is a converts strings from csv 
csv = np.genfromtxt('Iris.csv',delimiter=",")
print(csv)