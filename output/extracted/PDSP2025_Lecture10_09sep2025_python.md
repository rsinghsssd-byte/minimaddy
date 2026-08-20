## Page 1

PDSP 2025, Lecture 10, 9 September 2025
Mutable and immutable values
Lists and dictionaries are mutable
int , float , bool , str , tuple are immutable
For immutable values, assignment copies the value
x = 5
y = x
y = 7  # Does not affect the value of x
x,y
(5, 7)
For mutable values, assigment aliases the new name to point to the same value as the old name
Updating through either name affects both
l1 = [1,2,3]
l2 = l1
l2[0] = 4
l1,l2
([4, 2, 3], [4, 2, 3])
l1[2] = 6
l1,l2
([4, 2, 6], [4, 2, 6])
We can update a mutable value inside a function
However, we should be careful to use updates that do not reassign the name
Use l.append(v) vs l = l + [v]
def bad(l,v):
    l = l + [v]
    print(l)
    return
def good(l,v):
    l.append(v)
    print(l)
    return
bad(l,v) appends v within the function, but creates a new copy of l in the process, that is different
from the l passed as an argument
l = [1,2,3]
bad(l,4)
[1, 2, 3, 4]
l
[1, 2, 3]
In [1]:
In [2]:
Out[2]:
In [3]:
In [4]:
Out[4]:
In [5]:
In [6]:
Out[6]:
In [7]:
In [8]:
In [9]:
In [10]:
In [11]:
Out[11]:

---

## Page 2

good(l,v) on the other hand updates l in place, so the effect is visible outside
l
[1, 2, 3]
good(l,4)
[1, 2, 3, 4]
l
[1, 2, 3, 4]
We can update bad(l,v) to return the modified list, but then we have to reassign l to the returned
value
def bad2(l,v):
    l = l + [v]
    print(l)
    return(l)
l = [1,2,3]
returnlist = bad2(l,4)
[1, 2, 3, 4]
l,returnlist
([1, 2, 3], [1, 2, 3, 4])
l = [1,2,3]
l = bad2(l,4)
[1, 2, 3, 4]
l
[1, 2, 3, 4]
Slices and copying lists
A slice creates a new list
Full slice l[:] is a faithful copy of l
Abbreviation for l[0:len(l)]
Assigning a full slice makes a disjoint copy of a list
l1 = [1,2,3]
l2 = l1[:]
l1,l2
([1, 2, 3], [1, 2, 3])
l1[2] = 6
l2[0] = 4
l1, l2
([1, 2, 6], [4, 2, 3])
Pitfalls of mutability
zerorow = [0,0,0]
zeromat = [zerorow, zerorow, zerorow]
zeromat
In [12]:
Out[12]:
In [13]:
In [14]:
Out[14]:
In [15]:
In [16]:
In [17]:
Out[17]:
In [18]:
In [19]:
Out[19]:
In [20]:
In [21]:
Out[21]:
In [22]:
In [23]:
Out[23]:
In [24]:
In [25]:

---

## Page 3

[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
zeromat[2][2] = 33
zeromat
[[0, 0, 33], [0, 0, 33], [0, 0, 33]]
zerorow
[0, 0, 33]
This happens because updating any row in zeromat impliciltly updates zerolist
And vice versa
zerorow[0] = 11
zeromat
[[11, 0, 33], [11, 0, 33], [11, 0, 33]]
An aside
Multiplication is repeated addtion:
For lists, + denotes concatenation
l+l+l+l can be written as l*4
4 + 4 + 4

4*3

[0,0,0] + [0,0,0] + [0,0,0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0,0,0]*3
[0, 0, 0, 0, 0, 0, 0, 0, 0]
This does not avoid list aliasing issues
zerorow = [0,0,0]
zerolist = [zerorow]*3
zerolist
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
zerolist[1][1] = 44
zerolist
[[0, 44, 0], [0, 44, 0], [0, 44, 0]]
Use list comprehension instead
Each list comprehension creates a new list
[ 0 for i in range(3) ]  # A list of 3 zeros
Out[25]:
In [26]:
In [27]:
Out[27]:
In [28]:
Out[28]:
In [29]:
In [30]:
Out[30]:
n × m = n + n + ⋯+ n

m~times
In [31]:
Out[31]:
In [32]:
Out[32]:
In [33]:
Out[33]:
In [34]:
Out[34]:
In [35]:
In [36]:
In [37]:
Out[37]:
In [38]:
In [39]:
Out[39]:
In [40]:

---

## Page 4

[0, 0, 0]
[ [ 0 for i in range(3) ] for j in range (3) ] # 3 disjoint lists of 3 zeros
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
zmat = [ [ 0 for i in range(3) ] for j in range (3) ]
zmat
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
zmat[1][1] = 1
zmat
[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
Calling functions
Suppose we have a function definition def f(a,b): and a function call f(x,y)
When f(x,y) is executed, it is as though we start f with the assignments
    a = x
    b = y
This explains how/when values can be updated within a function
def factorial(n):
    ans = 1
    while n >= 1:
        ans = ans * n
        n = n-1
    return(ans)
x = 6
y = factorial(x)
x,y
(6, 720)
Inside the function, the parameter n is decremented to 0
n is derived from the variable x passed when the function is called
Since x is immutable, the implicit assignment n = x copies the value of x into n
Updating n has no effect on x
This also means we cannot write a function swap along the following lines
def swap(x,y):
    (x,y) = (y,x)
    return
m = 5
n = 7
swap(m,n)
m,n
(5, 7)
This will not work with mutable values either
The problem is the reassignment inside the function
Out[40]:
In [41]:
Out[41]:
In [42]:
In [43]:
Out[43]:
In [44]:
In [45]:
Out[45]:
In [46]:
In [47]:
In [48]:
Out[48]:
In [49]:
In [50]:
In [51]:
Out[51]:

---

## Page 5

list1 = [1,2,3]
list2 = [4,5,6]
swap(list1,list2)
list1, list2
([1, 2, 3], [4, 5, 6])
Passing mutable values to a function
Passing an argument is like executing an assignment statement before starting the function
For mutable values, this aliases the function parameter to the called value
In place changes in the function affect the value outside the function
def concat(l1,l2):
    l1.extend(l2)
    return
l3 = [1,2,3]
l4 = [4,5,6]
concat(l3,l4)
l3,l4
([1, 2, 3, 4, 5, 6], [4, 5, 6])
If we pass a slice, the value in the function is a disjoint copy
l3 = [1,2,3]
l4 = [4,5,6]
concat(l3[:],l4[:])
l3,l4
([1, 2, 3], [4, 5, 6])
However, reassigning the variable inside the function creates a new value not connected to the outer
value
def concat2(l1,l2):
    l1 = l1 + l2
    return
l3 = [1,2,3]
l4 = [4,5,6]
concat2(l3,l4)
l3,l4  # No effect - reassignment in function creates a local copy
([1, 2, 3], [4, 5, 6])
In fact, our problem with swap() applies to mutable values as well
The statement (m,n) = (n,m) is a reassignment and creates new values inside the function
swap(l3,l4)
l3,l4
([1, 2, 3], [4, 5, 6])
Be careful not to mix reassignment with in-place modification
What is the outcome of the following?
In [52]:
In [53]:
Out[53]:
In [54]:
In [55]:
In [56]:
Out[56]:
In [57]:
In [58]:
Out[58]:
In [59]:
In [60]:
In [61]:
Out[61]:
In [62]:
In [63]:
Out[63]:

---

## Page 6

def myappend(l,x):
    l = l.append(x)
    return(l)
l1 = [1,2]
l1 = myappend(l1,3)
l1
print(l1)
None
None is a special value in Python that explicitly represents that no value is assigned
A function that does not return a value returns None
In the notebook, the value is "empty", but print() displays it as None
In other words, str(None) converts the value None to the string "None"
None has its own type which is not compatible with any other type, so no operations are legal
str(None)
'None'
print(None)
None
type(None)
NoneType
Setting a variable to None is different from leaving it undefined
x = 7
type(x)
int
del(x)
x
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[74], line 1
----> 1 x
NameError: name 'x' is not defined
x = None
x
We can test if a variable is set to None
We will use this later
x == None
True
More on equality
x == y checks that x and y contain the same value
An assignment l2 = l1 aliases l2 to point to the same list as l1
Naturally, we expect l2 == l1 to be True
In [64]:
In [65]:
In [66]:
In [67]:
In [68]:
Out[68]:
In [69]:
In [70]:
Out[70]:
In [71]:
In [72]:
Out[72]:
In [73]:
In [74]:
In [75]:
In [76]:
In [77]:
Out[77]:

---

## Page 7

But there is a stronger relationship, because l1 and l2 are the same value
x is y checks if x and y refer to the same value
If x is y holds, it must be that x == y
Converse is not true
l1 = [1,2,3]
l2 = l1
l3 = l1[:]
l1 == l2, l1 == l3
(True, True)
l1 is l2, l1 is l3
(True, False)
x is y can also be tested for immutable values, but the outcome is not useful or reliable
x = 5
y = x
x is y # Not useful for immutable values
True
x = 5
y = 5
x is y
True
s = "hello"
t = s
s is t
True
s = "hello"
t = "hello"
s is t
True
In [78]:
In [79]:
Out[79]:
In [80]:
Out[80]:
In [81]:
In [82]:
Out[82]:
In [83]:
In [84]:
Out[84]:
In [85]:
In [86]:
Out[86]:
In [87]:
In [88]:
Out[88]: