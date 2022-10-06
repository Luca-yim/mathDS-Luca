# Number of pets each person owns
from math import *
data = [0, 1, 5, 7, 9, 10, 14]

def variance(values):
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / (len(values) - 1)
    return _variance

def std_div(values):
    return sqrt(variance(values))

print(variance(data))
print(std_div(data))