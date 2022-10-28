from numpy import array

basis = array(
    [
        [3, 0],
        [0, 2]
    ])

v = array([1, 1])

new_v = basis.dot(v)

print(new_v)