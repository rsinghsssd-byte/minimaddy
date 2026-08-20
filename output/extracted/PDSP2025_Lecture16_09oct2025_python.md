## Page 1

Lecture 16, 09 October 2025
Linked lists
Our current definition, with iterative append()
class List:
    def __init__(self,initlist = []):
        self.value = None
        self.next = None
        for x in initlist:
            self.append(x)
        return
    def isempty(self):
        return(self.value == None)

    def append(self,v):
        if self.isempty():
            self.value = v
            return

        temp = self
        while temp.next != None:
            temp = temp.next
        temp.next = List()
        temp.next.value = v
        return
    def insert(self,v):
        if self.isempty():
            self.value = v
            return
        newnode = List()
        newnode.value = v

        # Exchange values in self and newnode
        (self.value, newnode.value) = (newnode.value, self.value)
        # Switch links
        (self.next, newnode.next) = (newnode, self.next)
        return
    def __str__(self):
        # Iteratively create a Python list from linked list
        # and convert that to a string
        selflist = []
        if self.isempty():
            return(str(selflist))
        temp = self
In [1]:

---

## Page 2

selflist.append(temp.value)

        while temp.next != None:
          temp = temp.next
          selflist.append(temp.value)
        return(str(selflist))
Add recursive append()
appendi() , iterative
appendr() , recursive
Dummy append() that calls either appendi() or appendr()
To avoid problems with __init__ , __str__
class List:
    def __init__(self,initlist = []):
        self.value = None
        self.next = None
        for x in initlist:
            self.append(x)
        return
    def isempty(self):
        return(self.value == None)

    def appendi(self,v):   # append, iterative
        if self.isempty():
            self.value = v
            return

        temp = self
        while temp.next != None:
            temp = temp.next
        temp.next = List()
        temp.next.value = v
        return
    def appendr(self,v):   # append, recursive
        if self.isempty():
            self.value = v
        elif self.next == None:
            self.next = List()
            self.next.value = v
        else:
            self.next.appendr(v)
        return
    def append(self,v): # Could point to appendi or appendr
        self.appendr(v)
        return
    def insert(self,v):
        if self.isempty():
            self.value = v
            return
In [2]:

---

## Page 3

newnode = List()
        newnode.value = v

        # Exchange values in self and newnode
        (self.value, newnode.value) = (newnode.value, self.value)
        # Switch links
        (self.next, newnode.next) = (newnode, self.next)
        return
    def __str__(self):
        # Iteratively create a Python list from linked list
        # and convert that to a string
        selflist = []
        if self.isempty():
            return(str(selflist))
        temp = self
        selflist.append(temp.value)

        while temp.next != None:
          temp = temp.next
          selflist.append(temp.value)
        return(str(selflist))
l = List()
for i in range(20,0,-1):
    l.appendr(i)
print(l)
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Some performance measurements
import time
Iterative append, quadratic complexity
for i in range(1,5):
    unit = 1000
    l1 = List()
    start = time.perf_counter()
    for j in range(i*unit):
        l1.appendi(j)
    elapsed = time.perf_counter() - start
    print(i*unit,elapsed)
1000 0.037408503994811326
2000 0.13884098699782044
3000 0.25658054200175684
4000 0.41125536999606993
Recursive append, also quadratic, but 5x overhead due to recursive calls
In [3]:
In [4]:
In [5]:

---

## Page 4

for i in range(1,5):
    unit = 1000
    l1 = List()
    start = time.perf_counter()
    for j in range(i*unit):
        l1.appendr(j)
    elapsed = time.perf_counter() - start
    print(i*unit,elapsed)
1000 0.15295926301041618
2000 0.5776570989983156
--------------------------------------------------------------------------
-
RecursionError                            Traceback (most recent call las
t)
Cell In[6], line 6
     4 start = time.perf_counter()
     5 for j in range(i*unit):
----> 6     l1.appendr(j)
     7 elapsed = time.perf_counter() - start
     8 print(i*unit,elapsed)
Cell In[2], line 32, in List.appendr(self, v)
    30     self.next.value = v
    31 else:
---> 32     self.next.appendr(v)
    33 return
Cell In[2], line 32, in List.appendr(self, v)
    30     self.next.value = v
    31 else:
---> 32     self.next.appendr(v)
    33 return
   [... skipping similar frames: List.appendr at line 32 (2973 times)]
Cell In[2], line 32, in List.appendr(self, v)
    30     self.next.value = v
    31 else:
---> 32     self.next.appendr(v)
    33 return
Cell In[2], line 26, in List.appendr(self, v)
    25 def appendr(self,v):   # append, recursive
---> 26     if self.isempty():
    27         self.value = v
    28     elif self.next == None:
RecursionError: maximum recursion depth exceeded
Enhance recursion limit
 is maximum allowed
import sys
sys.setrecursionlimit(2**31-1)
for i in range(1,5):
    unit = 1000
In [6]:
231 −1
In [7]:
In [8]:

---

## Page 5

l1 = List()
    start = time.perf_counter()
    for j in range(i*unit):
        l1.appendr(j)
    elapsed = time.perf_counter() - start
    print(i*unit,elapsed)
1000 0.1520825240004342
2000 0.59965024900157
3000 1.326439897005912
4000 2.4543402420094935
Add delete()
class List:
    def __init__(self,initlist = []):
        self.value = None
        self.next = None
        for x in initlist:
            self.append(x)
        return
    def isempty(self):
        return(self.value == None)

    def appendi(self,v):   # append, iterative
        if self.isempty():
            self.value = v
            return

        temp = self
        while temp.next != None:
            temp = temp.next
        temp.next = List()
        temp.next.value = v
        return
    def appendr(self,v):   # append, recursive
        if self.isempty():
            self.value = v
        elif self.next == None:
            self.next = List([v])
        else:
            self.next.appendr(v)
        return
    def append(self,v):
        self.appendr(v)
        return
    def insert(self,v):
        if self.isempty():
            self.value = v
            return
        newnode = List()
        newnode.value = v
In [9]:

---

## Page 6

# Exchange values in self and newnode
        (self.value, newnode.value) = (newnode.value, self.value)
        # Switch links
        (self.next, newnode.next) = (newnode, self.next)
        return
    def delete(self,v):   # delete, recursive
        if self.isempty():
            return
        if self.value == v:
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            else:
                self.value = None
            return
        else:
            if self.next != None:
                self.next.delete(v)
                # Ensure that there is no empty node at the end of the li
                if self.next.value == None:
                    self.next = None
        return

    def __str__(self):
        # Iteratively create a Python list from linked list
        # and convert that to a string
        selflist = []
        if self.isempty():
            return(str(selflist))
        temp = self
        selflist.append(temp.value)

        while temp.next != None:
          temp = temp.next
          selflist.append(temp.value)
        return(str(selflist))
l = List(list(range(100)))
print(l)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 3
9, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 7
6, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
95, 96, 97, 98, 99]
l.delete(1)
print(l)
In [10]:
In [11]:

---

## Page 7

[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 2
1, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 5
8, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76,
77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 9
5, 96, 97, 98, 99]
l.delete(0)
print(l)
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 2
2, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 5
9, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 9
6, 97, 98, 99]
l.delete(99)
print(l)
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 2
2, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 5
9, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 9
6, 97, 98]
Exception handling
Example with input()
Python statement pass is a do-nothing placeholder. Cannot omit except:
block, nor can you have an empty block.
invalid = True
while (invalid):
    try:
        xstr = input("Enter a number: ")
        xint = int(xstr)
        invalid = False
    except:
        pass
print(xint)
-99
invalid = True
tryagain = False
while (invalid):
    try:
        if tryagain:
            print("Try again:")
        xstr = input("Enter a number: ")
        xint = int(xstr)
        invalid = False
    except:
        tryagain = True
print(xint)
In [12]:
In [13]:
In [14]:
In [15]:

---

## Page 8

Try again:
Try again:
-919
Catch a specific type of exception
int("abc")
--------------------------------------------------------------------------
-
ValueError                                Traceback (most recent call las
t)
Cell In[16], line 1
----> 1 int("abc")
ValueError: invalid literal for int() with base 10: 'abc'
invalid = True
while (invalid):
    try:
        xstr = input("Enter a number: ")
        xint = int(xstr)
        invalid = False
    except ValueError:
        pass
print(xint)

Raising an exception in List()
Inserting a negative value raises ValueError
Add negative value to error message
class List:
    def __init__(self,initlist = []):
        self.value = None
        self.next = None
        for x in initlist:
            self.append(x)
        return
    def isempty(self):
        return(self.value == None)

    def appendi(self,v):   # append, iterative
        if v < 0:
            raise ValueError("Negative input: " + str(v))
        if self.isempty():
            self.value = v
            return

        temp = self
        while temp.next != None:
            temp = temp.next
        temp.next = List()
        temp.next.value = v
        return
In [16]:
In [17]:
In [18]:

---

## Page 9

def appendr(self,v):   # append, recursive
        if v < 0:
            raise ValueError("Negative input: " + str(v))
        if self.isempty():
            self.value = v
        elif self.next == None:
            self.next = List([v])
        else:
            self.next.appendr(v)
        return
    def append(self,v):
        self.appendr(v)
        return
    def insert(self,v):
        if v < 0:
            raise ValueError("Negative input: " + str(v))
        if self.isempty():
            self.value = v
            return
        newnode = List()
        newnode.value = v

        # Exchange values in self and newnode
        (self.value, newnode.value) = (newnode.value, self.value)
        # Switch links
        (self.next, newnode.next) = (newnode, self.next)
        return
    def delete(self,v):   # delete, recursive
        if self.isempty():
            return
        if self.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None
        return

    def __str__(self):
        # Iteratively create a Python list from linked list
        # and convert that to a string
        selflist = []
        if self.isempty():
            return(str(selflist))
        temp = self
        selflist.append(temp.value)

---

## Page 10

while temp.next != None:
          temp = temp.next
          selflist.append(temp.value)
        return(str(selflist))
l = List([1,-2,3])
print(l)
--------------------------------------------------------------------------
-
ValueError                                Traceback (most recent call las
t)
Cell In[19], line 1
----> 1 l = List([1,-2,3])
     2 print(l)
Cell In[18], line 6, in List.__init__(self, initlist)
     4 self.next = None
     5 for x in initlist:
----> 6     self.append(x)
     7 return
Cell In[18], line 39, in List.append(self, v)
    38 def append(self,v):
---> 39     self.appendr(v)
    40     return
Cell In[18], line 29, in List.appendr(self, v)
    27 def appendr(self,v):   # append, recursive
    28     if v < 0:
---> 29         raise ValueError("Negative input: " + str(v))
    30     if self.isempty():
    31         self.value = v
ValueError: Negative input: -2
try:
    l = List([1,-2,3])
except ValueError:
    print("oops")
oops
try:
    l = List([1,-2,3])
except ValueError as errormsg:  # Saves error value in errormsg
    print(errormsg)
Negative input: -2
In [19]:
In [20]:
In [21]: