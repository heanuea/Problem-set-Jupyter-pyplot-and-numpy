import numpy as np
# genfromtxt is a numpy method and delimiter is a converts strings from csv 
csv = np.genfromtxt('data.csv',delimiter=",")
print(csv)