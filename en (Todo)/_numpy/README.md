* Rev.1: 2020-05-25 (Mon)
* Draft: 2017-01-10 (Tue)
# Numpy
For details, refer to:
* [Quickstart tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html)
* [NumPy Basics](https://numpy.org/doc/stable/user/basics.html)
* [Numpy and Scipy Documentation](https://docs.scipy.org/doc/)
* [NumPy User Guide](https://numpy.org/doc/stable/user/)
* [NumPy Reference](https://numpy.org/doc/stable/reference/)

## Tutorials
* [NumPy in Python | Set 1 (Introduction)](https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/)
* [NumPy in Python | Set 2 (Advanced)](https://www.geeksforgeeks.org/numpy-python-set-2-advanced/)
* [Python Numpy Tutorial (CS231n Convolutional Neural Networks for Visual Recognition)](http://cs231n.github.io/python-numpy-tutorial/)

## How to add numpy array iteratively
[The proper way to create a numpy array inside a for-loop](http://akuederle.com/create-numpy-array-with-for-loop)

```python
# From the reply by bwanamarko
result_array = np.empty(data_array.size) # the default dtype is float, so set dtype if it isn't float
for idx, line in enumerate(data_array):
   result_array[idx] = do_stuff(line)
```
