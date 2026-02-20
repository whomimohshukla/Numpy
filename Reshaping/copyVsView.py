import numpy as np

a = np.array([1, 2, 3])
view_arr = a.view()
copy_arr = a.copy()

a[0] = 99

print("original:", a)
print("view    :", view_arr)   # reflects change
print("copy    :", copy_arr)   # independent
