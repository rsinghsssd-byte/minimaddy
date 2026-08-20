## Page 1

PDSP 2025, Lecture 06, 26 August 2025
Tuples
Sequence of values in round brackets - (v1,v2,...,vk)
Typically values are not of a uniform type
Collect together different attributes of an item
Row in a table; each column is an attribute
t = ("Visakhapatnam","DC","CSK","DC","DC",192)
Positional indexing, slicing like other sequences
t[4],t[-1]
('DC', 192)
t[1:4]
('DC', 'CSK', 'DC')
Iterate over a tuple
print() prints its arguments --- either a message (string) or value of a variable
for x in t:
    print("x is", x, ", to repeat", x)
x is Visakhapatnam , to repeat Visakhapatnam
x is DC , to repeat DC
x is CSK , to repeat CSK
x is DC , to repeat DC
x is DC , to repeat DC
x is 192 , to repeat 192
'RR' in t, 'DC' in t
(False, True)
print(t)
('Visakhapatnam', 'DC', 'CSK', 'DC', 'DC', 192)
Unlike lists, cannot update a component of a tuple
t = ("Visakhapatnam","DC","CSK","DC","DC",192) # Change Team 2 to 'RR' from 'CSK'
t[2] = 'RR'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[8], line 1
----> 1 t[2] = 'RR'
TypeError: 'tuple' object does not support item assignment
Can concatenate tuples using +
Update a tuple by assembling a new tuple
Be careful, insert a comma to indicate a singleton tuple: (v,) vs (v)
u = t[0:2]+('RR')+t[3:]  # No difference between 'RR' and ('RR')
In [1]:
In [2]:
Out[2]:
In [3]:
Out[3]:
In [4]:
In [5]:
Out[5]:
In [6]:
In [7]:
In [8]:
In [9]:

---

## Page 2

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[9], line 1
----> 1 u = t[0:2]+('RR')+t[3:]  # No difference between 'RR' and ('RR')
TypeError: can only concatenate tuple (not "str") to tuple
u = t[0:2]+('RR',)+t[3:]  # ('RR',) is recognized a singleton tuple
u
('Visakhapatnam', 'DC', 'RR', 'DC', 'DC', 192)
Can use list() to convert a tuple to a list
list(t)
['Visakhapatnam', 'DC', 'CSK', 'DC', 'DC', 192]
In general list() works provided its argument is a sequence
list(range(5))
[0, 1, 2, 3, 4]
If the argument is not a sequence, list() generates an error
list(7)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[14], line 1
----> 1 list(7)
TypeError: 'int' object is not iterable
Can assign a tuple of variables in one shot
Useful for initialising multiple quantities
In nprimes() we started with primelist = [] and p = 2
(primelist,p) = ([],2)
# Equivalent to
primelist = []
p = 2
(x,y) = (y,x) swaps the values of x and y
All values on rhs are old values
All values on lhs are new assignments
Cannot be done sequentially
Not equivalent to x = y followed by y = x or vice versa
Normally, swap requires a temporary variable
t = y
y = x
x = t
Imagine exchanging the contents of a glass of juice and a glass of milk
Need a third empty glass
(x,y) = (5,[])
(x,y) = (y,x)
In [10]:
In [11]:
Out[11]:
In [12]:
Out[12]:
In [13]:
Out[13]:
In [14]:
In [15]:
In [16]:
In [17]:

---

## Page 3

x,y
([], 5)
When we say x,y we mean (x,y) --- brackets may be omitted
Python inserts them to display the value to us
x,y = 5,[]
x,y
(5, [])
Dictionaries
A list is a collection indexed by position
A list can be thought of as a function
A list maps positions to values
Generalize this to a function
Instead of positions, index by an abstract key
dictionary: maps keys, rather than positions, to values
Notation:
d = {k1:v1, k2:v2} , enumerate a dictionary explicitly
d[k1] , value in dictionary d1 corresponding to key k1
{} , empty dictionary ( [] for lists, () for tuples)
d = {'a':1,'b':17,'c':0}
d['b']

d['d']  # Invalid key
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[23], line 1
----> 1 d['d']  # Invalid key
KeyError: 'd'
d['d'] = 17
d['d']

An assignment d[k] = v serves two purposes
If there is no key k , create the key and assign it the value v
If there is already a key k , replace its current value by v
In a list, we cannot create a value at a new position through an assignment
If l is [0,1,2,3] , l[4] = 4 generate IndexError
If d = {'a':1,'b':17,'c':0} , d['d'] = 19 extends d with a new key-value pair
Iteration
d.keys() generates a sequence of all keys in d
Iterate over keys using for k in d.keys():
for k in d: also works --- d is implicitly intepreted as d.keys()
Though the keys do not form a sequence, Python will generate them in the order in which they were
created
Similarly, d.values() is the sequence of values present
In [18]:
Out[18]:
In [19]:
In [20]:
Out[20]:
f : {0, 1, … , n −1} →{v0, v1, … , vn−1}
f : {k0, k1, … , kn−1} →{v0, v1, … , vn−1}
In [21]:
In [22]:
Out[22]:
In [23]:
In [24]:
In [25]:
Out[25]:

---

## Page 4

d = {'a':1,'b':17,'c':0}
list(d.keys()), list(d.values())
(['a', 'b', 'c'], [1, 17, 0])
d = {'b':17,'c':0,'a':1}
list(d.keys()), list(d.values())
(['b', 'c', 'a'], [17, 0, 1])
In [26]:
In [27]:
Out[27]:
In [28]:
In [29]:
Out[29]: