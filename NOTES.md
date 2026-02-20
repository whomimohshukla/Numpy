# Project Notes: NumPy Practice Repo

## Overview
This repository is a beginner-friendly NumPy practice collection with small scripts grouped by topic:
- array creation
- array properties
- indexing/slicing
- broadcasting
- reshaping
- mathematical operations

---

## File-by-File Notes

### `README.md`
- Interview-style NumPy revision notes.
- Covers basics + common interview questions (vectorization, broadcasting, dtype, axis, copy/view, random, linear algebra).

### `1.py`
- Creates a simple 1D NumPy array and prints it.

### `creation/1numpy.py`
- Basic creation of a 1D array using `np.array`.

### `creation/default.py`
- Uses `np.zeros(5)` to create an array filled with zeros.

### `creation/ones.py`
- Uses `np.ones((2,3))` to create a 2x3 matrix of ones.

### `creation/fullshape.py`
- Uses `np.full((2,3), 7)` to create a 2x3 matrix filled with 7.

### `creation/identity.py`
- Uses `np.identity(5)` to create a 5x5 identity matrix.

### `creation/sequences.py`
- Uses `np.arange(1,10,2)` to generate a number sequence.

### `SpecialAraay/numArray.py`
- Demonstrates special array constructors:
  - `np.zeros`, `np.ones`, `np.full`, `np.eye`
  - sequence generators: `np.arange`, `np.linspace`, `np.logspace`, `np.geomspace`
  - random values: `np.random.rand`

### `NumPy-properties/dtype.py`
- Prints dtype of a 1D array.

### `NumPy-properties/ndim.py`
- Demonstrates dimensionality (`ndim`) for 1D, 2D, 3D arrays.

### `NumPy-properties/shape.py`
- Prints shape of a 2D array.

### `NumPy-properties/size.py`
- Prints total number of elements (`size`) in a 2D array.

### `NumPy-properties/astype.py`
- Demonstrates type conversion with `astype(float)` and `astype(int)`.

### `NumPy-properties/maths.py`
- Demonstrates element-wise arithmetic with scalar:
  - `+`, `-`, `*`, `/`, `**`, `%`, `//`

### `indexing/indexing&slicing.py`
- Demonstrates 2D indexing and slicing:
  - single element access `arr2[0,1]`
  - full column selection `arr2[:,1]`

### `indexing/tempCodeRunnerFile.py`
- Temporary editor-generated file (not part of learning content).
- Safe to remove.

### `Broadcasting/broadcasting.py`
- Demonstrates broadcasting between:
  - `a` shape `(2,3)`
  - `b` shape `(3,)`
- Performs element-wise arithmetic operations.

### `Reshaping/reshaping.py`
- Shows:
  - `arr.shape`
  - flattening with `flatten()` and `ravel()`
  - transpose with `.T`

### `Reshaping/copyVsView.py`
- Intended to demonstrate copy/view behavior.
- Current code assigns `b=a` then overwrites with `b=a.copy()`, so it only ends up showing copy assignment.

### `Mathematical fuct/maths.py`
- Demonstrates math functions:
  - `sqrt`, `exp`, `log`, `log10`
  - `sin`, `cos`, `tan`, `arctan`
- Includes `arcsin(a)` and `arccos(a)` where `a=[1..10]`, which is outside valid domain for most values and will output `nan` with runtime warnings.

---

## Issues / Cleanup Suggestions
1. Rename typo folders for clarity:
- `SpecialAraay` -> `SpecialArray`
- `Mathematical fuct` -> `Mathematical funct` or `MathematicalFunctions`

2. Remove temporary file:
- `indexing/tempCodeRunnerFile.py`

3. Fix inverse trig domain in `Mathematical fuct/maths.py`:
- `np.arcsin` and `np.arccos` should be used on values in `[-1, 1]`.

4. Improve `Reshaping/copyVsView.py`:
- Add both `view` and `copy` examples in the same script for clear comparison.

---

## Suggested Next Step
If you want, I can do an immediate cleanup pass now:
- remove temp file
- fix copy-vs-view demo
- fix inverse trig example
- standardize folder names and update paths
