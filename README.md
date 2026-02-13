# NumPy Interview Questions & Answers (Complete Guide)

This README is a quick interview revision sheet for NumPy, from basics to commonly asked advanced concepts.

## 1. What is NumPy?
NumPy (Numerical Python) is a Python library for high-performance numerical computing.  
It provides:
- N-dimensional array (`ndarray`)
- Mathematical functions
- Linear algebra tools
- Statistics utilities
- Random number generation

Key idea: fast array operations implemented in optimized C code.

## 2. Why is NumPy faster than Python lists?
NumPy is faster because:
- Data is stored in contiguous memory
- Arrays are homogeneous (same dtype)
- Core operations are implemented in C
- Vectorized operations avoid Python-level loops

Python lists store references to Python objects, which adds overhead.

## 3. List vs NumPy Array
| Feature | Python List | NumPy Array |
|---|---|---|
| Data type | Mixed | Homogeneous |
| Speed | Slower | Faster |
| Memory usage | Higher | Lower |
| Vectorization | No | Yes |

## 4. What is vectorization?
Vectorization means applying operations to entire arrays without explicit loops.

```python
import numpy as np
a = np.array([1, 2, 3])
print(a * 2)  # [2 4 6]
```

## 5. What is broadcasting?
Broadcasting allows NumPy to perform arithmetic on arrays with different shapes.

```python
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
print(a + b)
```

Broadcasting rules:
- Dimensions must be equal, or
- One of them must be `1`

## 6. `reshape()` vs `resize()`
| Method | Behavior |
|---|---|
| `reshape()` | Returns a new reshaped array (original unchanged) |
| `resize()` | Modifies array in-place and can change total size |

## 7. `flatten()` vs `ravel()`
| Method | Behavior |
|---|---|
| `flatten()` | Returns a copy |
| `ravel()` | Returns a view when possible |

`ravel()` is usually more memory efficient.

## 8. Copy vs View
```python
import numpy as np
a = np.array([1, 2, 3])
b = a.view()   # view
c = a.copy()   # copy
```

- View shares memory with original array
- Copy has independent memory

## 9. What is axis in NumPy?
For a 2D array:
- `axis=0`: operation down rows (column-wise result)
- `axis=1`: operation across columns (row-wise result)

Example:
```python
np.sum(arr, axis=0)
```

## 10. What is `dtype`?
`dtype` defines the data type of array elements.

```python
np.array([1, 2, 3], dtype=np.int8)
```

Smaller dtypes can reduce memory usage.

## 11. `np.arange()` vs `np.linspace()`
| Function | Main parameter |
|---|---|
| `arange(start, stop, step)` | step size |
| `linspace(start, stop, num)` | number of points |

`linspace()` includes end point by default.

## 12. What is `np.logspace()`?
Creates values evenly spaced on a log scale.

```python
np.logspace(1, 3, 3)  # [10., 100., 1000.]
```

## 13. What is `np.geomspace()`?
Creates numbers spaced geometrically (constant ratio).

## 14. `*` vs `@`
| Operator | Meaning |
|---|---|
| `*` | Element-wise multiplication |
| `@` | Matrix multiplication |

## 15. How to perform matrix multiplication?
```python
np.dot(a, b)
a @ b
```

## 16. How to generate random numbers?
```python
np.random.rand()      # uniform [0, 1)
np.random.randn()     # normal distribution
np.random.randint(1, 10)
np.random.seed(42)
```

## 17. What is `np.random.seed()`?
It sets the random seed so results are reproducible.

## 18. Mean, median, standard deviation, variance
```python
np.mean(arr)
np.median(arr)
np.std(arr)
np.var(arr)
```

## 19. How to filter an array?
Use boolean indexing:

```python
arr[arr > 10]
```

## 20. What is `np.linalg`?
Linear algebra module for operations like:

```python
np.linalg.det(A)
np.linalg.inv(A)
np.linalg.eig(A)
np.linalg.solve(A, b)
```

## 21. What is contiguous memory?
Array data is stored sequentially in memory, enabling faster access.

## 22. What is a structured array?
A NumPy array where each element can have multiple named fields with different dtypes.

## 23. How to stack arrays?
```python
np.vstack([a, b])   # vertical stack
np.hstack([a, b])   # horizontal stack
```

## 24. How to split arrays?
```python
np.split(arr, 3)    # split into 3 equal parts
```

## 25. `sum()` vs `add()`
| Function | Meaning |
|---|---|
| `np.sum(arr)` | Aggregates values |
| `np.add(a, b)` | Element-wise addition |

## 26. What is fancy indexing?
Selecting elements using lists/arrays of indices:

```python
arr[[0, 2]]
```

## 27. Memory optimization in NumPy
Choose appropriate `dtype`:

```python
arr = np.array([1, 2, 3], dtype=np.int8)
```

## 28. `range()` vs `np.arange()`
| Function | Returns |
|---|---|
| `range()` | iterator |
| `np.arange()` | NumPy array |

## 29. What happens if shapes don't match?
NumPy raises broadcasting error:

```python
ValueError: operands could not be broadcast together
```

## 30. Real-world uses of NumPy
- Data preprocessing
- Machine learning pipelines
- Image processing
- Scientific computing
- Statistical analysis

## Advanced Interview Concepts
### Why is NumPy the foundation of ML?
Most ML libraries depend on NumPy-style array computation for tensor/matrix operations.

### What is BLAS?
BLAS (Basic Linear Algebra Subprograms) is a set of optimized routines used by NumPy for fast linear algebra.

## Important Topics to Master
- Broadcasting
- Axis concept
- Copy vs view
- Matrix multiplication
- Random module
- Boolean indexing
- Reshaping
