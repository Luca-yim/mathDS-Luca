import pandas as pd

points = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",").itertuples()

m = 1.93939
b = 4.73333

sum_of_squares = 0.0

for p in points:
    y_actual = p.y 
    y_predict = m*p.x + b
    residual = (y_actual - y_predict)**2
    print(residual)