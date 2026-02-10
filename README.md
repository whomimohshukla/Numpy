
**NumPy Notes + Practice**
This repo contains short scripts and notes about NumPy, focused on array creation and the basics. Each script prints its output so you can see shapes and values immediately.

**What Is NumPy**
NumPy (Numerical Python) is the core library for fast numerical computing in Python. It provides the `ndarray` (n-dimensional array) type and many functions for math, statistics, and linear algebra.

**Why Use NumPy**
- Fast: vectorized operations run in optimized C code.
- Compact: arrays store data in contiguous memory.
- Expressive: powerful slicing, broadcasting, and universal functions (ufuncs).
- Foundation: used by pandas, SciPy, scikit-learn, and many ML/data tools.

**Key Concepts**
- `ndarray`: fixed-size, typed, n-dimensional array.
- Shape and dtype: array dimensions and element type.
- Vectorization: apply operations to whole arrays without Python loops.
- Broadcasting: automatic alignment of shapes in arithmetic.

**Common Use Cases**
- Data analysis and preprocessing.
- Scientific computing and simulations.
- Machine learning feature engineering.
- Image and signal processing.
- Linear algebra and matrix operations.

**Repo Examples**
`creation/1numpy.py` creates a NumPy array from a Python list.
`creation/default.py` creates a zero-filled array with `np.zeros`.
`creation/ones.py` creates a ones-filled array with `np.ones`.
`creation/fullshape.py` creates a filled array with `np.full`.
`creation/identity.py` creates an identity matrix with `np.identity`.
`creation/sequences.py` creates a sequence with `np.arange`.

**Install**
```bash
pip install numpy
```

**Run Examples**
```bash
python creation/1numpy.py
python creation/default.py
python creation/ones.py
python creation/fullshape.py
python creation/identity.py
python creation/sequences.py
```
