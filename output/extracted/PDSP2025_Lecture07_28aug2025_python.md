## Page 1

PDSP 2025, Lecture 07, 28 August 2025
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
--------------------------------------------------------------------------
-
KeyError                                  Traceback (most recent call las
t)
Cell In[3], line 1
----> 1 d['d']  # Invalid key
KeyError: 'd'
d['d'] = 17
d['d']

An assignment d[k] = v serves two purposes
If there is no key k , create the key and assign it the value v
If there is already a key k , replace its current value by v
In a list, we cannot create a value at a new position through an assignment
If l is [0,1,2,3] , l[4] = 4 generate IndexError
If d = {'a':1,'b':17,'c':0} , d['d'] = 19 extends d with a new
key-value pair
Iteration
d.keys() generates a sequence of all keys in d
f : {0, 1, … , n −1} →{v0, v1, … , vn−1}
f : {k0, k1, … , kn−1} →{v0, v1, … , vn−1}
In [1]:
In [2]:
Out[2]:
In [3]:
In [4]:
In [5]:
Out[5]:

---

## Page 2

Iterate over keys using for k in d.keys():
for k in d: also works --- d is implicitly intepreted as d.keys()
Though the keys do not form a sequence, Python will generate them in the
order in which they were created
Similarly, d.values() is the sequence of values present
d = {'a':1,'b':17,'c':0}
list(d.keys()), list(d.values())
(['a', 'b', 'c'], [1, 17, 0])
d = {'b':17,'c':0,'a':1}
list(d.keys()), list(d.values())
(['b', 'c', 'a'], [17, 0, 1])
Example
Count frequency of numbers in a list
Maintain a counter for each value that appears in the list
Dictionary freqd where each key is a number v and freqd[v] is a positive
integer
The first time we see a number, need to create a key and assign it the value 1
If there is already a key for the current number, increment its count
Test if a key k is present using k in d.keys() (or, shorter, k in d )
def frequency(l):
    freqd = {}
    for v in l:
        if v in freqd:  # Check if v is already a key
            freqd[v] = freqd[v] + 1
        else:           # Create a new key with count 1
            freqd[v] = 1
    return(freqd)
d = frequency([1,2,1,3,1,4,2,3,1,5,6,2,7])
d
{1: 4, 2: 3, 3: 2, 4: 1, 5: 1, 6: 1, 7: 1}
Keys are listed in the order they are inserted
This is guaranteed by current versions of Python, need not hold for dictionaries in
general
d2 = frequency([1,2,1,3,1,4,2,3,1,5,7,2,6])
d2
In [6]:
In [7]:
Out[7]:
In [8]:
In [9]:
Out[9]:
In [10]:
In [11]:
In [12]:
Out[12]:
In [13]:
In [14]:

---

## Page 3

{1: 4, 2: 3, 3: 2, 4: 1, 5: 1, 7: 1, 6: 1}
List membership
v in l returns True iff value v is in l
Implicit iteration, same as
def element(l,v):
  for x in l:
    if x == v:
      return(True)
  return(False)
Linear scan of the list, examine all elements (worst case) if v is not in l
Extract unique elements from a list
Standard loop builds a new list of unique elements
Check if each element in the original list is already in the new list before adding
def uniq(l):
    uniqlist = []
    for x in l:
        if not (x in uniqlist):  # Implicit nested loop
            uniqlist.append(x)
    return(uniqlist)
Complexity
Worst case is when original list has no duplicates
l[k] will be compared to k elements in newl before being added to newl
Takes
 steps, which is
Proportional to
Using a dictionary
Cannot have duplicate keys in a dictionary
Create a dictionary whose keys are values in the original list
Value associated with key is not important
If we see the same value twice, the key will be updated, not duplicated
In the end, return the list of keys
def uniqd(l):
    uniqdict = {}
    for x in l:
        uniqdict[x] = 1
    return(list(uniqdict))
Complexity
Out[14]:
In [15]:
1 + 2 + ⋯n −1
n(n −1)

n2
In [16]:

---

## Page 4

Creating/updating a key in a dictionary takes a fixed amount of time, independent of
the size of the dictionary
Assuming the hash function works well and there are no (or very few) collisions
This works effectively in time proportional to , the length of the list
We can experimentally verify this by applying both functions to a large list without
duplicates
In the examples below, we have asked for the length of the list rather than the
list itself to avoid large outputs cluttering the page
len(uniq(list(range(50000)))) # Takes a long time
50000
len(uniqd(list(range(100000))))  # Almost instantaneous
100000
len(uniqd(list(range(10000000)))) # Python can do about 10^7 ops/sec
10000000
"Classical" solution is to sort the list
In the sorted list, duplicates are bunched together
Scan the sorted list and retain an element if it is different from the previous one
Sorting takes time
 -- we will see this later
Scanning for duplicates takes time
Overall
def uniqs(l):
    if l == []:
        return([])
    lsorted = sorted(l)
    uniqlist,previous = [l[0]],l[0]
    for x in lsorted[1:]:
        if x != previous:
            uniqlist.append(x)
        previous = x
    return(uniqlist)
len(uniqs(list(range(50000))))
50000
len(uniqs(list(range(10000000))))
10000000
Only marginally slower than uniqd
n
In [17]:
Out[17]:
In [18]:
Out[18]:
In [19]:
Out[19]:
n log n
n
n log n
In [20]:
In [21]:
Out[21]:
In [22]:
Out[22]:

---

## Page 5

Intersection of two lists
For each element v of l1 check if v occurs in l2
Nested loop
def intersect(l1,l2):
    commonlist = []
    for x in l1:
        for y in l2:
            if x == y:
                if not(x in commonlist):
                    commonlist.append(x)
    return(commonlist)
len(intersect(list(range(0,100)),list(range(50,150))))

len(intersect(list(range(0,30000)),list(range(15000,45000))))
15000
While we scan l1 we can check if the element is in l2
x in l2 is an implicit nested iteration
Performance is same as the explicit nested loop above
def intersect2(l1,l2):
    commonlist = []
    for x in l1:
        if x in l2: # Hidden nested loop
            if not(x in commonlist):
                commonlist.append(x)
    return(commonlist)
len(intersect2(list(range(0,100)),list(range(50,150))))

len(intersect2(list(range(0,30000)),list(range(15000,45000))))
15000
Using dictionaries
Create a dictionary whose keys are the elements in l1
Check each element in l2 against the keys of this dictionary
Checking x in l takes time proportional to len(l)
Checking y in d.keys() takes constant time
Overall time is proportional to len(l1) + len(l2)
In [23]:
In [24]:
Out[24]:
In [25]:
Out[25]:
In [26]:
In [27]:
Out[27]:
In [28]:
Out[28]:

---

## Page 6

def intersectd(l1,l2):
    commondict = {}
    l1dict = {}
    for x in l1:
        l1dict[x] = 1
    for y in l2:
        if y in l1dict:
            commondict[y] = 1
    return(list(commondict.keys()))
len(intersectd(list(range(0,300000)),list(range(150000,450000))))
150000
"Classical" solution is to sort and merge
Sort both lists
Scan the two sorted lists in a single pass and identify common elements
Sorting takes time
Merging takes time
Overall
def intersectm(l1,l2):
    l1sort = sorted(l1)
    l2sort = sorted(l2)
    commonlist = []
    i,j = 0,0
    while i < len(l1sort) and j < len(l2sort):
        if l1sort[i] < l2sort[j]:
            i += 1
        elif l1sort[i] > l2sort[j]:
            j += 1
        elif l1sort[i] == l2sort[j]:
            if (not l1sort[i] in commonlist):
                commonlist.append(l1sort[i])
            i += 1
            j += 1
    return(commonlist)
len(intersectm(list(range(0,50000)),list(range(25000,75000))))
25000
len(intersectm(list(range(0,100000)),list(range(50000,150000))))
50000
Noticeably slower than intersectd
In [29]:
In [30]:
Out[30]:
n log n
n
n log n
In [31]:
In [32]:
Out[32]:
In [33]:
Out[33]: