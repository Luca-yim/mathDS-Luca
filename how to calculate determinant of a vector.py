from numpy.linalg import det
from numpy import array

i_hat = array([2, 1])
j_hat = array([6, 3])

basis = array([i_hat, j_hat]).transpose()

determinant = det(basis)

print("Determinant =" + str(determinant))
print("LINEAR DEPENDENCE CHECK:")
print("TRANSFORMATION HAS LINEAR DEPENDENCE" if determinant==0 else "NO LINEAR DEPENDENCE IN TRANSFORMATION")