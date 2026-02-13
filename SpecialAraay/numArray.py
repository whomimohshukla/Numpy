import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

print(np.zeros((2,3)))
print(np.ones((2,3)))
print(np.full((2,3), 7))   # must provide fill value
print(np.eye(2))

print(np.arange(2,10))
print(np.linspace(2,3,5))
print(np.logspace(2,3,5))
print(np.geomspace(2,32,5))

print(np.random.rand(2,3))
