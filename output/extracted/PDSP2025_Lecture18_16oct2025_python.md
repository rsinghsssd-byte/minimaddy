## Page 1

Lecture 18, 16 October 2025
Using numpy
Arrays and lists
Arrays are "homogenous" with regular structure
Lists are flexible
Load numpy
import numpy as np  # Shortcut, use np for numpy in code
Constructing arrays
np.array() constructs an array from an input sequence
Sequence can be a list, tuple, output of a range() command ...
Size of the array is fixed by the sequence
Underlying type is also fixed
b = np.array(range(10))
b
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b.dtype # Underlying datatype of b
dtype('int64')
Use nested sequences to produce multi-dimensional arrays
A 2d array is an array of 1d arrays
Note: can mix and match notation for sequences, but dimensions much match
c = np.array([(0,1,0),[2,3,2]])
c
array([[0, 1, 0],
      [2, 3, 2]])
c = np.array([(0,1,0),[2,2]])
c
In [1]:
In [2]:
Out[2]:
In [3]:
Out[3]:
In [4]:
Out[4]:
In [5]:

---

## Page 2

--------------------------------------------------------------------------
-
ValueError                                Traceback (most recent call las
t)
Cell In[5], line 1
----> 1 c = np.array([(0,1,0),[2,2]])
     2 c
ValueError: setting an array element with a sequence. The requested array
has an inhomogeneous shape after 1 dimensions. The detected shape was (2,)
+ inhomogeneous part.
d = np.array([(0,1,0),range(3)])
d
array([[0, 1, 0],
      [0, 1, 2]])
A 3d array is an array of 2d arrays
d = np.array([[(0,1,0),[2,3,2]],[[4,5,4],[6,7,6]]])
d
array([[[0, 1, 0],
       [2, 3, 2]],
      [[4, 5, 4],
       [6, 7, 6]]])
m_zeros = np.zeros((5,3))  # np.zeros(shape), shape = (dim1,dim2,...,dimk
m_zeros
array([[0., 0., 0.],
      [0., 0., 0.],
      [0., 0., 0.],
      [0., 0., 0.],
      [0., 0., 0.]])
m_zeros = np.zeros(5,3)
--------------------------------------------------------------------------
-
TypeError                                 Traceback (most recent call las
t)
Cell In[9], line 1
----> 1 m_zeros = np.zeros(5,3)
TypeError: Cannot interpret '3' as a data type
m_zeros.dtype
dtype('float64')
m_zero_int = np.zeros(7,dtype='int64')
m_zero_int
array([0, 0, 0, 0, 0, 0, 0])
In [6]:
Out[6]:
In [7]:
Out[7]:
In [8]:
Out[8]:
In [9]:
In [11]:
Out[11]:
In [12]:
Out[12]:

---

## Page 3

m_ones = np.ones((8,2,3))
m_ones
array([[[1., 1., 1.],
       [1., 1., 1.]],
      [[1., 1., 1.],
       [1., 1., 1.]],
      [[1., 1., 1.],
       [1., 1., 1.]],
      [[1., 1., 1.],
       [1., 1., 1.]],
      [[1., 1., 1.],
       [1., 1., 1.]],
      [[1., 1., 1.],
       [1., 1., 1.]],
      [[1., 1., 1.],
       [1., 1., 1.]],
      [[1., 1., 1.],
       [1., 1., 1.]]])
m_rand = np.random.random((4,6))
m_rand
array([[0.61478095, 0.66873022, 0.95844102, 0.42150011, 0.4276577 ,
       0.4466395 ],
      [0.4091643 , 0.19277623, 0.64426873, 0.29413532, 0.3060221 ,
       0.55254819],
      [0.96782399, 0.64445448, 0.30810994, 0.22376551, 0.87498372,
       0.34494317],
      [0.69119246, 0.57612184, 0.57630797, 0.92630779, 0.64981307,
       0.38438788]])
m_rand_int = np.random.randint(1,100,(3,4))
m_rand_int
array([[89, 84, 64, 20],
      [10, 51, 13, 23],
      [ 2, 35,  5, 34]])
m_normal = np.random.normal(0,1,(5,2))   # np.normal(mean, std_dev, shape
m_normal
array([[ 2.25324418,  0.02261622],
      [ 0.46259818, -0.28531591],
      [-0.83403691, -2.6713428 ],
      [ 1.17590504, -1.09052901],
      [-0.98658065, -0.21246764]])
Broadcasting
In simplest form, scalar operations applied pointwise
In [13]:
Out[13]:
In [14]:
Out[14]:
In [15]:
Out[15]:
In [16]:
Out[16]:

---

## Page 4

a = np.arange(10)  # arange(n) is same as array(range(n))
a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a**3  # Replace each element by its cube  --- [ x**3 for x in a ]
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
a+3   # Add 3 to each element
array([ 3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
3*a   # Multiply each element by 3
array([ 0,  3,  6,  9, 12, 15, 18, 21, 24, 27])
3+a   # Same as a+3
array([ 3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
a-3, 3-a  # Order is important because subtraction is not commutative
(array([-3, -2, -1,  0,  1,  2,  3,  4,  5,  6]),
array([ 3,  2,  1,  0, -1, -2, -3, -4, -5, -6]))
3**a  # Powers of 3
array([    1,     3,     9,    27,    81,   243,   729,  2187,  6561,
      19683])
Stacking arrays
np.random.random(m,n) creates an
 array with random numbers drawn
uniformly from
10*np.random.random() scales the entries by 10
np.floor() removes the fractional part
a = np.floor(10*np.random.random((2,2)))
b = np.floor(10*np.random.random((3,2)))
print(a)
print(b)
[[4. 1.]
[6. 9.]]
[[1. 5.]
[2. 1.]
[5. 2.]]
vstack() stacks a sequence of arrays vertically -- should have same number of
columns
np.vstack((a,b))
In [17]:
Out[17]:
In [18]:
Out[18]:
In [19]:
Out[19]:
In [20]:
Out[20]:
In [21]:
Out[21]:
In [22]:
Out[22]:
In [23]:
Out[23]:
mxn
[0, 1)
In [24]:
In [25]:

---

## Page 5

array([[4., 1.],
      [6., 9.],
      [1., 5.],
      [2., 1.],
      [5., 2.]])
Cannot vstack() if number of columns don't match
c = np.floor(10*np.random.random((2,3)))
c
array([[2., 8., 2.],
      [9., 4., 9.]])
np.vstack((a,c))
--------------------------------------------------------------------------
-
ValueError                                Traceback (most recent call las
t)
Cell In[27], line 1
----> 1 np.vstack((a,c))
File ~/python-venv/lib/python3.13/site-packages/numpy/_core/shape_base.py:
292, in vstack(tup, dtype, casting)
   290 if not isinstance(arrs, tuple):
   291     arrs = (arrs,)
--> 292 return _nx.concatenate(arrs, 0, dtype=dtype, casting=casting)
ValueError: all the input array dimensions except for the concatenation ax
is must match exactly, but along dimension 1, the array at index 0 has siz
e 2 and the array at index 1 has size 3
Number of rows does not matter if columns match
d = np.floor(10*np.random.random((3,2)))
d
array([[1., 2.],
      [2., 2.],
      [6., 0.]])
np.vstack((a,d))
array([[4., 1.],
      [6., 9.],
      [1., 2.],
      [2., 2.],
      [6., 0.]])
Can stack any length sequence of arrays, not just two arrays
np.vstack([a,b,d])
Out[25]:
In [26]:
Out[26]:
In [27]:
In [28]:
Out[28]:
In [29]:
Out[29]:
In [30]:

---

## Page 6

array([[4., 1.],
      [6., 9.],
      [1., 5.],
      [2., 1.],
      [5., 2.],
      [1., 2.],
      [2., 2.],
      [6., 0.]])
Likewise, hstack() stacks horizontally, number of rows must match
np.hstack((a,b))
--------------------------------------------------------------------------
-
ValueError                                Traceback (most recent call las
t)
Cell In[31], line 1
----> 1 np.hstack((a,b))
File ~/python-venv/lib/python3.13/site-packages/numpy/_core/shape_base.py:
367, in hstack(tup, dtype, casting)
   365     return _nx.concatenate(arrs, 0, dtype=dtype, casting=casting)
   366 else:
--> 367     return _nx.concatenate(arrs, 1, dtype=dtype, casting=casting)
ValueError: all the input array dimensions except for the concatenation ax
is must match exactly, but along dimension 0, the array at index 0 has siz
e 2 and the array at index 1 has size 3
np.hstack((b,d))
array([[1., 5., 1., 2.],
      [2., 1., 2., 2.],
      [5., 2., 6., 0.]])
For hstack() , number of columns does not matter
Like vstack() , can combine a sequence of arrays
e = np.floor(10*np.random.random((3,3)))
e
array([[7., 6., 4.],
      [8., 1., 3.],
      [9., 6., 3.]])
np.hstack((b,d,e))
array([[1., 5., 1., 2., 7., 6., 4.],
      [2., 1., 2., 2., 8., 1., 3.],
      [5., 2., 6., 0., 9., 6., 3.]])
Splitting arrays
a = np.floor(10*np.random.random((2,12)))
a
Out[30]:
In [31]:
In [32]:
Out[32]:
In [33]:
Out[33]:
In [34]:
Out[34]:
In [35]:

---

## Page 7

array([[1., 1., 6., 1., 7., 2., 8., 1., 4., 6., 4., 4.],
      [0., 9., 3., 7., 6., 7., 0., 2., 0., 7., 9., 1.]])
hsplit(A,n) splits array A into n equal parts horizontally
n must be a divisor of the number of columns in A
np.hsplit(a,3)
[array([[1., 1., 6., 1.],
       [0., 9., 3., 7.]]),
array([[7., 2., 8., 1.],
       [6., 7., 0., 2.]]),
array([[4., 6., 4., 4.],
       [0., 7., 9., 1.]])]
np.hsplit(a,6)
[array([[1., 1.],
       [0., 9.]]),
array([[6., 1.],
       [3., 7.]]),
array([[7., 2.],
       [6., 7.]]),
array([[8., 1.],
       [0., 2.]]),
array([[4., 6.],
       [0., 7.]]),
array([[4., 4.],
       [9., 1.]])]
np.hsplit(a,5)
--------------------------------------------------------------------------
-
ValueError                                Traceback (most recent call las
t)
Cell In[38], line 1
----> 1 np.hsplit(a,5)
File ~/python-venv/lib/python3.13/site-packages/numpy/lib/_shape_base_imp
l.py:959, in hsplit(ary, indices_or_sections)
   957     raise ValueError('hsplit only works on arrays of 1 or more dim
ensions')
   958 if ary.ndim > 1:
--> 959     return split(ary, indices_or_sections, 1)
   960 else:
   961     return split(ary, indices_or_sections, 0)
File ~/python-venv/lib/python3.13/site-packages/numpy/lib/_shape_base_imp
l.py:884, in split(ary, indices_or_sections, axis)
   882     N = ary.shape[axis]
   883     if N % sections:
--> 884         raise ValueError(
   885             'array split does not result in an equal division') fr
om None
   886 return array_split(ary, indices_or_sections, axis)
ValueError: array split does not result in an equal division
Out[35]:
In [36]:
Out[36]:
In [37]:
Out[37]:
In [38]:

---

## Page 8

Can also specify where to split as a list of columns
hsplit(A,[c1,c2,..,ck]) will split as A[:c1] , A[c1:c2] ,..., A[ck:]
np.hsplit(a,(2,5,7)) # a[:2], a[2:5], a[5:7], a[7:]
[array([[1., 1.],
       [0., 9.]]),
array([[6., 1., 7.],
       [3., 7., 6.]]),
array([[2., 8.],
       [7., 0.]]),
array([[1., 4., 6., 4., 4.],
       [2., 0., 7., 9., 1.]])]
Similarly, vsplit for vertical split
np.vsplit(a,2) # Split a vertically
[array([[1., 1., 6., 1., 7., 2., 8., 1., 4., 6., 4., 4.]]),
array([[0., 9., 3., 7., 6., 7., 0., 2., 0., 7., 9., 1.]])]
np.split(a,2) # behaves like vsplit
[array([[1., 1., 6., 1., 7., 2., 8., 1., 4., 6., 4., 4.]]),
array([[0., 9., 3., 7., 6., 7., 0., 2., 0., 7., 9., 1.]])]
Reshaping arrays
Can change the shape of an array if the dimensions match
a.shape
(2, 12)
a.shape = 2,12
a
array([[1., 1., 6., 1., 7., 2., 8., 1., 4., 6., 4., 4.],
      [0., 9., 3., 7., 6., 7., 0., 2., 0., 7., 9., 1.]])
a.shape = 4,6
a
array([[1., 1., 6., 1., 7., 2.],
      [8., 1., 4., 6., 4., 4.],
      [0., 9., 3., 7., 6., 7.],
      [0., 2., 0., 7., 9., 1.]])
a.shape = 3,8
a
array([[1., 1., 6., 1., 7., 2., 8., 1.],
      [4., 6., 4., 4., 0., 9., 3., 7.],
      [6., 7., 0., 2., 0., 7., 9., 1.]])
In [39]:
Out[39]:
In [40]:
Out[40]:
In [41]:
Out[41]:
In [42]:
Out[42]:
In [43]:
Out[43]:
In [44]:
Out[44]:
In [45]:
Out[45]:

---

## Page 9

a.shape = 2,3,4
a
array([[[1., 1., 6., 1.],
       [7., 2., 8., 1.],
       [4., 6., 4., 4.]],
      [[0., 9., 3., 7.],
       [6., 7., 0., 2.],
       [0., 7., 9., 1.]]])
Copy and view
a.shape = 2,12
c = a.copy()  # Creates a disjoint copy of the array
d = a.view()  # Creates another link to the same array
e = a         # Aliases e to point to same array as a
a, c, d, e
(array([[1., 1., 6., 1., 7., 2., 8., 1., 4., 6., 4., 4.],
       [0., 9., 3., 7., 6., 7., 0., 2., 0., 7., 9., 1.]]),
array([[1., 1., 6., 1., 7., 2., 8., 1., 4., 6., 4., 4.],
       [0., 9., 3., 7., 6., 7., 0., 2., 0., 7., 9., 1.]]),
array([[1., 1., 6., 1., 7., 2., 8., 1., 4., 6., 4., 4.],
       [0., 9., 3., 7., 6., 7., 0., 2., 0., 7., 9., 1.]]),
array([[1., 1., 6., 1., 7., 2., 8., 1., 4., 6., 4., 4.],
       [0., 9., 3., 7., 6., 7., 0., 2., 0., 7., 9., 1.]]))
Updating c has no effect on the others since it is a disjoint copy
c[0,4] = 88  # Note, not c[0][4]
a, c, d, e
(array([[1., 1., 6., 1., 7., 2., 8., 1., 4., 6., 4., 4.],
       [0., 9., 3., 7., 6., 7., 0., 2., 0., 7., 9., 1.]]),
array([[ 1.,  1.,  6.,  1., 88.,  2.,  8.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
array([[1., 1., 6., 1., 7., 2., 8., 1., 4., 6., 4., 4.],
       [0., 9., 3., 7., 6., 7., 0., 2., 0., 7., 9., 1.]]),
array([[1., 1., 6., 1., 7., 2., 8., 1., 4., 6., 4., 4.],
       [0., 9., 3., 7., 6., 7., 0., 2., 0., 7., 9., 1.]]))
Updating d will indirectly update a and e , but not c
d[0,5] = 66
a, c, d, e
In [46]:
Out[46]:
In [47]:
In [48]:
In [49]:
Out[49]:
In [50]:
Out[50]:
In [51]:

---

## Page 10

(array([[ 1.,  1.,  6.,  1.,  7., 66.,  8.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1., 88.,  2.,  8.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1.,  7., 66.,  8.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1.,  7., 66.,  8.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]))
Likewise, updating e updates a and d
e[0,6] = 77
a, c, d, e
(array([[ 1.,  1.,  6.,  1.,  7., 66., 77.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1., 88.,  2.,  8.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1.,  7., 66., 77.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1.,  7., 66., 77.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]))
We can flatten an array into a sequence
for i in a.flat:
    print(i,end=" ")
1.0 1.0 6.0 1.0 7.0 66.0 77.0 1.0 4.0 6.0 4.0 4.0 0.0 9.0 3.0 7.0 6.0 7.0
0.0 2.0 0.0 7.0 9.0 1.0
base tells us if an array shares its storage with another array
For the original array, base is None
For a view, the base points to the "parent" array
a.base, c.base, d.base, e.base
(None,
None,
array([[ 1.,  1.,  6.,  1.,  7., 66., 77.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
None)
d.base is a
True
Changing the shape of the base does array not affect the shape of a view
a.shape = 4,6
a,c,d,e
Out[51]:
In [52]:
Out[52]:
In [53]:
In [54]:
Out[54]:
In [55]:
Out[55]:
In [56]:

---

## Page 11

(array([[ 1.,  1.,  6.,  1.,  7., 66.],
       [77.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.],
       [ 0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1., 88.,  2.,  8.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1.,  7., 66., 77.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1.,  7., 66.],
       [77.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.],
       [ 0.,  2.,  0.,  7.,  9.,  1.]]))
Changing the shape of the view does not affect the shape of the base array
d.shape = 3,8
a,c,d,e
(array([[ 1.,  1.,  6.,  1.,  7., 66.],
       [77.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.],
       [ 0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1., 88.,  2.,  8.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1.,  7., 66., 77.,  1.],
       [ 4.,  6.,  4.,  4.,  0.,  9.,  3.,  7.],
       [ 6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1.,  7., 66.],
       [77.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.],
       [ 0.,  2.,  0.,  7.,  9.,  1.]]))
Since they still have the same base, updating a changes the corresponding element
in d
a[3,0] = 99
a,c,d,e
(array([[ 1.,  1.,  6.,  1.,  7., 66.],
       [77.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.],
       [99.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1., 88.,  2.,  8.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1.,  7., 66., 77.,  1.],
       [ 4.,  6.,  4.,  4.,  0.,  9.,  3.,  7.],
       [ 6.,  7., 99.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1.,  7., 66.],
       [77.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.],
       [99.,  2.,  0.,  7.,  9.,  1.]]))
Likewise, updating the shape of e , which is an alias for a , does not affect the
shape of the view d
Out[56]:
In [57]:
Out[57]:
In [58]:
Out[58]:

---

## Page 12

e.shape = 8,3
a,c,d,e
(array([[ 1.,  1.,  6.],
       [ 1.,  7., 66.],
       [77.,  1.,  4.],
       [ 6.,  4.,  4.],
       [ 0.,  9.,  3.],
       [ 7.,  6.,  7.],
       [99.,  2.,  0.],
       [ 7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1., 88.,  2.,  8.,  1.,  4.,  6.,  4.,  4.],
       [ 0.,  9.,  3.,  7.,  6.,  7.,  0.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.,  1.,  7., 66., 77.,  1.],
       [ 4.,  6.,  4.,  4.,  0.,  9.,  3.,  7.],
       [ 6.,  7., 99.,  2.,  0.,  7.,  9.,  1.]]),
array([[ 1.,  1.,  6.],
       [ 1.,  7., 66.],
       [77.,  1.,  4.],
       [ 6.,  4.,  4.],
       [ 0.,  9.,  3.],
       [ 7.,  6.,  7.],
       [99.,  2.,  0.],
       [ 7.,  9.,  1.]]))
Matrix operations
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
a,b
(array([[1, 2],
       [3, 4]]),
array([[5, 6],
       [7, 8]]))
Pointwise addition and multiplication
a+b, a*b
(array([[ 6,  8],
       [10, 12]]),
array([[ 5, 12],
       [21, 32]]))
Matrix multiplication
np.matmul(a,b)
array([[19, 22],
      [43, 50]])
Transpose and inverse
In [59]:
Out[59]:
In [60]:
In [61]:
Out[61]:
In [62]:
Out[62]:
In [63]:
Out[63]:

---

## Page 13

a.T
array([[1, 3],
      [2, 4]])
np.linalg.inv(a)
array([[-2. ,  1. ],
      [ 1.5, -0.5]])
 should give the identity matrix
Note the small imprecision due to round off error
np.matmul(a,np.linalg.inv(a))
array([[1.0000000e+00, 0.0000000e+00],
      [8.8817842e-16, 1.0000000e+00]])
Fit a function  to a set of data points
Compute mean square error (MSE)
predictions = np.array([1.2,2.3,3.1]) # (f(x1), f(x2), f(x3))
values = np.array([1,2.5,3]) # (y1, y2, y3)
predictions - values creates the array
Applying np.square to this squares each element
Applying np.sum to the result sums up the squares of the errors
n = len(predictions)
mse = 1/n * np.sum(np.square(predictions-values))
mse
np.float64(0.03000000000000002)
Axes
a = np.random.random((4,3))*10
a
array([[0.74535302, 7.32186747, 3.09968508],
      [1.4351353 , 5.3403798 , 2.05243956],
      [0.17113068, 2.72845255, 0.07238354],
      [2.31854671, 6.79866632, 4.2397082 ]])
np.sum() adds up all the entries in the array
np.sum(a)
In [64]:
Out[64]:
In [65]:
Out[65]:
AA−1
In [66]:
Out[66]:
f
{(x1, y1), (x2, y2), … , (xn, yn)}
MSE =
n
∑
i=1
(f(xi) −yi)2

n
In [67]:
(f(x1) −y1, f(x2) −y2, f(x3) −y3)
In [68]:
Out[68]:
In [69]:
Out[69]:
In [70]:

---

## Page 14

np.float64(36.32374822114578)
Selecting axis = 0 applies the operation column by column
np.sum(a,axis=0)
array([ 4.67016571, 22.18936614,  9.46421637])
Selecting axis = 1 applies the opertion row by row
np.sum(a,axis=1)
array([11.16690556,  8.82795466,  2.97196677, 13.35692123])
concatenate() generalizes vstack() and hstack()
By default it is vstack() , equivalent to setting axis = 0
If we set axis = 1 , we get hstack()
b = np.random.random((4,3))*10
b
array([[2.78302014, 7.96796426, 5.57485252],
      [9.52754737, 8.00566296, 3.4566572 ],
      [7.23662734, 3.12841927, 1.92923489],
      [8.92895264, 3.02463578, 6.91495572]])
np.vstack((a,b)), np.hstack((a,b))
(array([[0.74535302, 7.32186747, 3.09968508],
       [1.4351353 , 5.3403798 , 2.05243956],
       [0.17113068, 2.72845255, 0.07238354],
       [2.31854671, 6.79866632, 4.2397082 ],
       [2.78302014, 7.96796426, 5.57485252],
       [9.52754737, 8.00566296, 3.4566572 ],
       [7.23662734, 3.12841927, 1.92923489],
       [8.92895264, 3.02463578, 6.91495572]]),
array([[0.74535302, 7.32186747, 3.09968508, 2.78302014, 7.96796426,
        5.57485252],
       [1.4351353 , 5.3403798 , 2.05243956, 9.52754737, 8.00566296,
        3.4566572 ],
       [0.17113068, 2.72845255, 0.07238354, 7.23662734, 3.12841927,
        1.92923489],
       [2.31854671, 6.79866632, 4.2397082 , 8.92895264, 3.02463578,
        6.91495572]]))
np.concatenate((a,b))  # Implicitly, axis = 0, so vstack()
Out[70]:
In [71]:
Out[71]:
In [72]:
Out[72]:
In [73]:
Out[73]:
In [74]:
Out[74]:
In [75]:

---

## Page 15

array([[0.74535302, 7.32186747, 3.09968508],
      [1.4351353 , 5.3403798 , 2.05243956],
      [0.17113068, 2.72845255, 0.07238354],
      [2.31854671, 6.79866632, 4.2397082 ],
      [2.78302014, 7.96796426, 5.57485252],
      [9.52754737, 8.00566296, 3.4566572 ],
      [7.23662734, 3.12841927, 1.92923489],
      [8.92895264, 3.02463578, 6.91495572]])
np.concatenate((a,b),axis=1) # Concatenate row-wise, so same as hstack()
array([[0.74535302, 7.32186747, 3.09968508, 2.78302014, 7.96796426,
       5.57485252],
      [1.4351353 , 5.3403798 , 2.05243956, 9.52754737, 8.00566296,
       3.4566572 ],
      [0.17113068, 2.72845255, 0.07238354, 7.23662734, 3.12841927,
       1.92923489],
      [2.31854671, 6.79866632, 4.2397082 , 8.92895264, 3.02463578,
       6.91495572]])
c = np.random.random((1,7))
d = np.random.random((1,7))
c,d
(array([[0.77252961, 0.9476818 , 0.22204027, 0.11708873, 0.91664732,
        0.35529799, 0.09111515]]),
array([[0.3056627 , 0.83884962, 0.25602509, 0.06546634, 0.41950657,
        0.73748701, 0.01506722]]))
np.concatenate((c,d),axis=1)
array([[0.77252961, 0.9476818 , 0.22204027, 0.11708873, 0.91664732,
       0.35529799, 0.09111515, 0.3056627 , 0.83884962, 0.25602509,
       0.06546634, 0.41950657, 0.73748701, 0.01506722]])
Broadcasting
Array with scalar --- map operation to each array element
a = np.array([1.0, 2.0, 3.0])
b = 2.0
a * b
array([2., 4., 6.])
Array with array/sequence of same length --- pointwise application of operation
a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
a * b
array([2., 4., 6.])
More generally, can broadcast to an array of same dimension as rightmost index
Out[75]:
In [76]:
Out[76]:
In [77]:
Out[77]:
In [78]:
Out[78]:
In [79]:
Out[79]:
In [80]:
Out[80]:

---

## Page 16

Example
Store an
 image as 3 layers, Red, Blue and Green
Array dimensions are
Want to scale RGB values by different amounts
Multiply image by
pic = np.random.random((4,4,3))*10
pic
array([[[5.7448521 , 6.21715157, 8.09743372],
       [3.86616619, 1.83400169, 3.30234273],
       [7.14510501, 8.53592886, 0.1984932 ],
       [2.83792466, 2.78075699, 6.47495444]],
      [[4.20196209, 0.05568092, 9.82591891],
       [7.88589042, 4.24747824, 1.91112919],
       [6.23340351, 5.32555818, 8.30908835],
       [0.10657329, 6.2069235 , 3.47629843]],
      [[4.79882427, 0.91260498, 4.87367519],
       [5.43909663, 9.33695084, 8.74619775],
       [7.92382402, 0.32737941, 0.68173562],
       [1.91816694, 3.49747929, 7.85137433]],
      [[8.97653917, 4.78902054, 5.36404235],
       [5.54700431, 9.70798109, 8.02925934],
       [8.83133383, 0.98081094, 4.92779854],
       [3.86833919, 4.14670514, 6.73500368]]])
pic*[1,100,1000]
array([[[5.74485210e+00, 6.21715157e+02, 8.09743372e+03],
       [3.86616619e+00, 1.83400169e+02, 3.30234273e+03],
       [7.14510501e+00, 8.53592886e+02, 1.98493199e+02],
       [2.83792466e+00, 2.78075699e+02, 6.47495444e+03]],
      [[4.20196209e+00, 5.56809248e+00, 9.82591891e+03],
       [7.88589042e+00, 4.24747824e+02, 1.91112919e+03],
       [6.23340351e+00, 5.32555818e+02, 8.30908835e+03],
       [1.06573294e-01, 6.20692350e+02, 3.47629843e+03]],
      [[4.79882427e+00, 9.12604978e+01, 4.87367519e+03],
       [5.43909663e+00, 9.33695084e+02, 8.74619775e+03],
       [7.92382402e+00, 3.27379407e+01, 6.81735625e+02],
       [1.91816694e+00, 3.49747929e+02, 7.85137433e+03]],
      [[8.97653917e+00, 4.78902054e+02, 5.36404235e+03],
       [5.54700431e+00, 9.70798109e+02, 8.02925934e+03],
       [8.83133383e+00, 9.80810942e+01, 4.92779854e+03],
       [3.86833919e+00, 4.14670514e+02, 6.73500368e+03]]])
Note
In the example above, a shape of (3,4,4) would display more intuitively as 3
layers of colour for the base image of shape (4,4)
m × n
(m, n, 3)
(rscale, bscale, gscale)
In [81]:
In [82]:
Out[82]:
In [83]:
Out[83]:

---

## Page 17

However, for broadcasting, we need the rightmost index to match, so we wrote it as
(4,4,3) , which is laid out less intuitively by numpy as 4 layers with shape
(4,3)
Broadcasting example
Find the nearest point to a given point in a collection
Given
 and
, report  such that
 is the
closest point to
Distance of each point is
 reports index where
 is achieved
Here is the whole computation in one shot
observation = np.array([111.0, 188.0])  # (x,y)
codes = np.array([[132.0, 193.0],  # [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
               [102.0, 203.0],
               [45.0, 155.0],
               [57.0, 173.0]])
diff = codes - observation
dist = np.sqrt(np.sum(diff**2,axis=1))
dist, np.argmin(dist)
(array([21.58703314, 17.49285568, 73.79024326, 56.04462508]), np.int64
(1))
Let us break this up into steps
1. The setup
observation = np.array([111.0, 188.0])  # (x,y)
codes = np.array([[132.0, 193.0],  # [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
               [102.0, 203.0],
               [45.0, 155.0],
               [57.0, 173.0]])
2. Use broadcast to subtact
 from each
 to get the array
diff = codes - observation
diff
array([[ 21.,   5.],
      [ -9.,  15.],
      [-66., -33.],
      [-54., -15.]])
3. Use scalar broadcast to map each pair
 to
(x, y)
{(x1, y1), (x2, y2), … , (xn, yn)}
j
(xj, yj)
(x, y)
√(xi −x)2 + (yi −y)2
arg min
min
In [84]:
Out[84]:
In [85]:
(x, y)
(xi, yi)
[(x1 −x, y1 −y), (x2 −x, y2 −y), (x3 −x, y3 −y), (x4 −x, y4 −y)]
In [86]:
In [87]:
Out[87]:
(xi −x, yi −y)
((xi −x)2, (yi −y)2)

---

## Page 18

diff**2
array([[ 441.,   25.],
      [  81.,  225.],
      [4356., 1089.],
      [2916.,  225.]])
4. Add up each row as
 by computing np.sum() along axis =

np.sum(diff**2,axis=1)
array([ 466.,  306., 5445., 3141.])
5. Apply np.sqrt() pointwise to this array of squared differences
np.sqrt(np.sum(diff**2,axis=1))
array([21.58703314, 17.49285568, 73.79024326, 56.04462508])
6. Find the index where this value is minimum
dist = np.sqrt(np.sum(diff**2,axis=1))
np.argmin(dist)
np.int64(1)
Or, equivalently, without the intermediate variable dist
np.argmin(np.sqrt(np.sum(diff**2,axis=1)))
np.int64(1)
In fact, the entire computation can be written in one line
np.argmin(np.sqrt(np.sum((codes-observation)**2,axis=1)))
np.int64(1)
np.min(np.sqrt(np.sum((codes-observation)**2,axis=1)))
np.float64(17.4928556845359)
In [88]:
Out[88]:
(xi −x)2 + (yi −y)2
In [89]:
Out[89]:
In [90]:
Out[90]:
In [91]:
Out[91]:
In [92]:
Out[92]:
In [93]:
Out[93]:
In [94]:
Out[94]: