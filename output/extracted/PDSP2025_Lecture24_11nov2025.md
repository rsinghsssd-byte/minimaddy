## Page 1

Lecture 24, 11 November 2025
Madhavan Mukund
https://www.cmi.ac.in/~madhavan
Programming and Data Structures with Python
Lecture 24, 11 Nov 2025

---

## Page 2

Two dimensional
data structures
in x in
array
Binary tree-heap
-
Insert()
I
delete-max ()
balanced
by
construction
height
is
0 (log size)

---

## Page 3

Dynamic sorted data
Sorting is useful for e!cient searching
What if the data is changing dynamically?
Items are periodically inserted and deleted
Insert/delete in a sorted list takes time O(n)
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
2 / 23

---

## Page 4

Dynamic sorted data
Sorting is useful for e!cient searching
What if the data is changing dynamically?
Items are periodically inserted and deleted
Insert/delete in a sorted list takes time O(n)
Move to a tree structure, like heaps for priority queues
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
2 / 23

---

## Page 5

Binary search tree
For each node with value v
All values in the left subtree
are < v
All values in the right subtree
are > v

Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
3 / 23
-
No duplicates

---

## Page 6

Binary search tree
For each node with value v
All values in the left subtree
are < v
All values in the right subtree
are > v
No duplicate values

Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
3 / 23

---

## Page 7

Implementing a binary search tree
Each node has a value and
pointers to its children
v
ω
r
5 • •
8 – •
9 – –
2 • •
4 – –
1 – –

Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
4 / 23
⑯

---

## Page 8

Back to lists#
get Get-T
appendr(v) - If empty
2base(t
value-
add a successor v
else
recursively append v to
next

---

## Page 9

Solution
Ferminate
every list
with an empty mode
↓empty list
---
appendr(v)
If emptylist
set value
= v
set next =
new Node()
else
self-next Appender(v)

---

## Page 10

Implementing a binary search tree
Each node has a value and
pointers to its children
v
ω
r
5 • •
8 • •
9 • •
– – –
– – –
– – –
2 • •
4 • •
1 • •
– – –
– – –
– – –
– – –

Add a frontier with empty nodes, all fields –
Empty tree is single empty node
Leaf node points to empty nodes
Easier to implement operations recursively
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
4 / 23
E
G00a
sa
d
- Go

---

## Page 11

The class Tree
Three local fields, value, left,
right
Value None for empty value –
Empty tree has all fields None
Leaf has a nonempty value and
empty left and right
class Tree:
# Constructor:
def __init__(self,initval=None):
self.value = initval
if self.value != None:
self.left = Tree()
self.right = Tree()
else:
self.left = None
self.right = None
return
# Only empty node has value None
def isempty(self):
return (self.value == None)
# Leaf nodes have both children empty
def isleaf(self):
return (self.value != None and
self.left.isempty() and
self.right.isempty())
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
5 / 23

---

## Page 12

Inorder traversal
List the left subtree, then the
current node, then the right subtree
Lists values in sorted order
Use to print the tree
class Tree:
...
# Inorder traversal
def inorder(self):
if self.isempty():
return([])
else:
return(self.left.inorder()+
[self.value]+
self.right.inorder())
# Display Tree as a string
def __str__(self):
return(str(self.inorder()))
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
6 / 23

---

## Page 13

Inorder traversal
List the left subtree, then the
current node, then the right subtree
Lists values in sorted order
Use to print the tree

class Tree:
...
# Inorder traversal
def inorder(self):
if self.isempty():
return([])
else:
return(self.left.inorder()+
[self.value]+
self.right.inorder())
# Display Tree as a string
def __str__(self):
return(str(self.inorder()))
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
6 / 23
y
[1 , 2, 4) + [s) + [] +[8] + 99]

---

## Page 14

Find a value v
Check value at current node
If v smaller than current node, go
left
If v smaller than current node, go
right
Natural generalization of binary
search
class Tree:
...
# Check if value v occurs in tree
def find(self,v):
if self.isempty():
return(False)
if self.value == v:
return(True)
if v < self.value:
return(self.left.find(v))
if v > self.value:
return(self.right.find(v))
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
7 / 23

---

## Page 15

Find a value v
Check value at current node
If v smaller than current node, go
left
If v smaller than current node, go
right
Natural generalization of binary
search

class Tree:
...
# Check if value v occurs in tree
def find(self,v):
if self.isempty():
return(False)
if self.value == v:
return(True)
if v < self.value:
return(self.left.find(v))
if v > self.value:
return(self.right.find(v))
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
7 / 23
-

---

## Page 16

Minimum and maximum
Minimum is left most node in the
tree
Maximum is right most node in the
tree
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
8 / 23

---

## Page 17

Minimum and maximum
Minimum is left most node in the
tree
Maximum is right most node in the
tree

Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
8 / 23

O

---

## Page 18

Minimum and maximum
Minimum is left most node in the
tree
Maximum is right most node in the
tree

class Tree:
...
def minval(self):
if self.left.isempty():
return(self.value)
else:
return(self.left.minval())
def maxval(self):
if self.right.isempty():
return(self.value)
else:
return(self.right.maxval())
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
8 / 23
I
& ·Y
&
-
-

---

## Page 20

Insert a value v
Try to find v
Insert at the position where find
fails
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
9 / 23

---

## Page 21

Insert a value v
Try to find v
Insert at the position where find
fails
Insert 21

Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
9 / 23
Y
Y
d

---

## Page 22

Insert a value v
Try to find v
Insert at the position where find
fails
Insert 21

Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
9 / 23

---

## Page 23

Insert a value v
Try to find v
Insert at the position where find
fails
Insert 21

Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
9 / 23

---

## Page 24

Insert a value v
Try to find v
Insert at the position where find
fails
Insert 65

Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
9 / 23
Y
X
?

---

## Page 25

Insert a value v
Try to find v
Insert at the position where find
fails
Insert 65

Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
9 / 23

---

## Page 26

Insert a value v
Try to find v
Insert at the position where find
fails
Insert 65

Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
9 / 23

---

## Page 27

Insert a value v
Try to find v
Insert at the position where find
fails
Insert 91

Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
9 / 23

v

---

## Page 28

Insert a value v
Try to find v
Insert at the position where find
fails
Insert 91

class Tree:
...
def insert(self,v):
if self.isempty():
self.value = v
self.left = Tree()
self.right = Tree()
if self.value == v:
return
if v < self.value:
self.left.insert(v)
return
if v > self.value:
self.right.insert(v)
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
9 / 23
find
return (False)
return time)

---

## Page 29

Delete a value v
If v is present, delete
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
10 / 23

---

## Page 30

Delete a value v
If v is present, delete
Leaf node? No problem
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
10 / 23

---

## Page 31

Delete a value v
If v is present, delete
Leaf node? No problem
If only one child, promote that
subtree
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
10 / 23.

---

## Page 32

Delete a value v
If v is present, delete
Leaf node? No problem
If only one child, promote that
subtree
Otherwise, replace v with
self.left.maxval() and delete
self.left.maxval()
self.left.maxval() has no
right child
class Tree:
...
def delete(self,v):
if self.isempty():
return
if v < self.value:
self.left.delete(v)
return
if v > self.value:
self.right.delete(v)
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
10 / 23
CaseI
- v absent
Case2
-
~
Case3
Case I
Jease

---

## Page 33

↓X
delete ve
D
↓1
[V ,V ,]
[V+, V
,=]
~
~

---

## Page 34

Delete a value v
Delete 65

class Tree:
...
def delete(self,v):
if self.isempty():
return
if v < self.value:
self.left.delete(v)
return
if v > self.value:
self.right.delete(v)
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
11 / 23
T
Casel

---

## Page 35

Delete a value v
Delete 65

class Tree:
...
def delete(self,v):
if self.isempty():
return
if v < self.value:
self.left.delete(v)
return
if v > self.value:
self.right.delete(v)
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
11 / 23

---

## Page 36

Delete a value v
Delete 65

class Tree:
...
def delete(self,v):
if self.isempty():
return
if v < self.value:
self.left.delete(v)
return
if v > self.value:
self.right.delete(v)
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
11 / 23

---

## Page 37

Delete a value v
Delete 74

class Tree:
...
def delete(self,v):
if self.isempty():
return
if v < self.value:
self.left.delete(v)
return
if v > self.value:
self.right.delete(v)
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
11 / 23
Or

---

## Page 38

Delete a value v
Delete 74

class Tree:
...
def delete(self,v):
if self.isempty():
return
if v < self.value:
self.left.delete(v)
return
if v > self.value:
self.right.delete(v)
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
11 / 23

---

## Page 39

Delete a value v
Delete 74

class Tree:
...
def delete(self,v):
if self.isempty():
return
if v < self.value:
self.left.delete(v)
return
if v > self.value:
self.right.delete(v)
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
11 / 23

---

## Page 40

Delete a value v
Delete 37

class Tree:
...
def delete(self,v):
if self.isempty():
return
if v < self.value:
self.left.delete(v)
return
if v > self.value:
self.right.delete(v)
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
11 / 23
O
St
Xx

---

## Page 41

Delete a value v
Delete 37

class Tree:
...
def delete(self,v):
if self.isempty():
return
if v < self.value:
self.left.delete(v)
return
if v > self.value:
self.right.delete(v)
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
11 / 23

---

## Page 42

Delete a value v
Delete 37

class Tree:
...
def delete(self,v):
if self.isempty():
return
if v < self.value:
self.left.delete(v)
return
if v > self.value:
self.right.delete(v)
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
11 / 23

---

## Page 43

Delete a value v
Delete 37

class Tree:
...
def delete(self,v):
if self.isempty():
return
if v < self.value:
self.left.delete(v)
return
if v > self.value:
self.right.delete(v)
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
11 / 23
↑
X

---

## Page 44

Delete a value v
Delete 37

class Tree:
...
def delete(self,v):
if self.isempty():
return
if v < self.value:
self.left.delete(v)
return
if v > self.value:
self.right.delete(v)
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
11 / 23

---

## Page 45

Delete a value v
class Tree:
...
def delete(self,v):
if self.isempty():
return
if v < self.value:
self.left.delete(v)
return
if v > self.value:
self.right.delete(v)
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
# Convert leaf node to empty node
def makeempty(self):
self.value = None
self.left = None
self.right = None
return
# Promote left child
def copyleft(self):
self.value = self.left.value
self.right = self.left.right
self.left = self.left.left
return
# Promote right child
def copyright(self):
self.value = self.right.value
self.left = self.right.left
self.right = self.right.right
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
12 / 23

---

## Page 46

Complexity
find(), insert() and delete() all walk down a single path
Worst-case: height of the tree
An unbalanced tree with n nodes may have height O(n)
Balanced trees have height O(log n)
How can we maintain balance as tree grows and shrinks?
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
13 / 23

---

## Page 47

Operations on search trees
Defining balance
Left and right subtrees should be "equal"
Two possible measures: size and
height
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
14 / 23

---

## Page 48

Operations on search trees
Defining balance
Left and right subtrees should be "equal"
Two possible measures: size and
height
self.left.size() and
self.right.size() are equal?
Only possible for complete binary trees
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
14 / 23

---

## Page 49

Operations on search trees
Defining balance
Left and right subtrees should be "equal"
Two possible measures: size and
height
self.left.size() and
self.right.size() are equal?
Only possible for complete binary trees
self.left.size() and
self.right.size() di!er by at most 1?
Plausible, but di"cult to maintain
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
14 / 23

---

## Page 50

Height balanced trees
self.height() — number of nodes on
longest path from root to leaf
0 for empty tree
1 for tree with only a root node
1 + max of heights of left and right
subtrees, in general
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
15 / 23

---

## Page 51

Height balanced trees
self.height() — number of nodes on
longest path from root to leaf
0 for empty tree
1 for tree with only a root node
1 + max of heights of left and right
subtrees, in general
Height balance
self.left.height() and
self.right.height() di!er by at most

AVL trees — Adelson-Velskii, Landis
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
15 / 23
Red Black trees
&
I

---

## Page 52

Height balanced trees
self.height() — number of nodes on
longest path from root to leaf
0 for empty tree
1 for tree with only a root node
1 + max of heights of left and right
subtrees, in general
Height balance
self.left.height() and
self.right.height() di!er by at most

AVL trees — Adelson-Velskii, Landis
Does height balance guarantee O(log n)
height?
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
15 / 23

---

## Page 53

Height balanced trees
self.height() — number of nodes on
longest path from root to leaf
0 for empty tree
1 for tree with only a root node
1 + max of heights of left and right
subtrees, in general
Height balance
self.left.height() and
self.right.height() di!er by at most

AVL trees — Adelson-Velskii, Landis
Does height balance guarantee O(log n)
height?
Minimum size height-balanced trees
•
h=1
•
•
h = 2
•
•
•
•
h = 3
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
15 / 23
!
11 Win
h=4
height is small
not size
log (size)
size
is large
not height
zheight

---

## Page 54

Height balanced trees
self.height() — number of nodes on
longest path from root to leaf
0 for empty tree
1 for tree with only a root node
1 + max of heights of left and right
subtrees, in general
Height balance
self.left.height() and
self.right.height() di!er by at most

AVL trees — Adelson-Velskii, Landis
Does height balance guarantee O(log n)
height?
Minimum size height-balanced trees
•
h=1
•
•
h = 2
•
•
•
•
h = 3
•
•
•
•
•
•
•
h = 4
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
15 / 23
fo

---

## Page 55

Height balanced trees
self.height() — number of nodes on
longest path from root to leaf
0 for empty tree
1 for tree with only a root node
1 + max of heights of left and right
subtrees, in general
Height balance
self.left.height() and
self.right.height() di!er by at most

AVL trees — Adelson-Velskii, Landis
Does height balance guarantee O(log n)
height?
Minimum size height-balanced trees
•
h=1
•
•
h = 2
•
•
•
•
h = 3
•
•
•
•
•
•
•
h = 4
General strategy to build a small
balanced tree of height h
Smallest balanced tree of height
h →1 as left subtree
Smallest balanced tree of height
h →2 as right subtree
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
15 / 23

---

## Page 56

Height balanced trees
Minimum size height-balanced trees
•
h=1
•
•
h = 2
•
•
•
•
h = 3
•
•
•
•
•
•
•
h = 4
General strategy to build a small
balanced tree of height h
Smallest balanced tree of height
h →1 as left subtree
Smallest balanced tree of height
h →2 as right subtree
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
16 / 23

---

## Page 57

Height balanced trees
Minimum size height-balanced trees
•
h=1
•
•
h = 2
•
•
•
•
h = 3
•
•
•
•
•
•
•
h = 4
General strategy to build a small
balanced tree of height h
Smallest balanced tree of height
h →1 as left subtree
Smallest balanced tree of height
h →2 as right subtree
S(h), size of smallest height-balanced tree
of height h
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
16 / 23

---

## Page 58

Height balanced trees
Minimum size height-balanced trees
•
h=1
•
•
h = 2
•
•
•
•
h = 3
•
•
•
•
•
•
•
h = 4
General strategy to build a small
balanced tree of height h
Smallest balanced tree of height
h →1 as left subtree
Smallest balanced tree of height
h →2 as right subtree
S(h), size of smallest height-balanced tree
of height h
Recurrence
S(0) = 0, S(1) = 1
S(h) = 1 + S(h →1) + S(h →2)
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
16 / 23

---

## Page 59

Height balanced trees
Minimum size height-balanced trees
•
h=1
•
•
h = 2
•
•
•
•
h = 3
•
•
•
•
•
•
•
h = 4
General strategy to build a small
balanced tree of height h
Smallest balanced tree of height
h →1 as left subtree
Smallest balanced tree of height
h →2 as right subtree
S(h), size of smallest height-balanced tree
of height h
Recurrence
S(0) = 0, S(1) = 1
S(h) = 1 + S(h →1) + S(h →2)
Compare to Fibonacci sequence
F(0) = 0, F(1) = 1
F(n) = F(n →1) + F(n →2)
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
16 / 23
O

---

## Page 60

Height balanced trees
Minimum size height-balanced trees
•
h=1
•
•
h = 2
•
•
•
•
h = 3
•
•
•
•
•
•
•
h = 4
General strategy to build a small
balanced tree of height h
Smallest balanced tree of height
h →1 as left subtree
Smallest balanced tree of height
h →2 as right subtree
S(h), size of smallest height-balanced tree
of height h
Recurrence
S(0) = 0, S(1) = 1
S(h) = 1 + S(h →1) + S(h →2)
Compare to Fibonacci sequence
F(0) = 0, F(1) = 1
F(n) = F(n →1) + F(n →2)
S(h) grows exponentially with h
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
16 / 23

---

## Page 61

Height balanced trees
Minimum size height-balanced trees
•
h=1
•
•
h = 2
•
•
•
•
h = 3
•
•
•
•
•
•
•
h = 4
General strategy to build a small
balanced tree of height h
Smallest balanced tree of height
h →1 as left subtree
Smallest balanced tree of height
h →2 as right subtree
S(h), size of smallest height-balanced tree
of height h
Recurrence
S(0) = 0, S(1) = 1
S(h) = 1 + S(h →1) + S(h →2)
Compare to Fibonacci sequence
F(0) = 0, F(1) = 1
F(n) = F(n →1) + F(n →2)
S(h) grows exponentially with h
For size n, h is O(log n)
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
16 / 23

---

## Page 62

Correcting imbalance
Slope of a node : self.left.height() - self.right.height()
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
17 / 23

---

## Page 63

Correcting imbalance
Slope of a node : self.left.height() - self.right.height()
Balanced tree — slope is {→1, 0, 1}
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
17 / 23

---

## Page 64

Correcting imbalance
Slope of a node : self.left.height() - self.right.height()
Balanced tree — slope is {→1, 0, 1}
t.insert(v), t.delete(v) can alter slope to →2 or +2
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
17 / 23

---

## Page 65

Correcting imbalance
Slope of a node : self.left.height() - self.right.height()
Balanced tree — slope is {→1, 0, 1}
t.insert(v), t.delete(v) can alter slope to →2 or +2
Left rotation
•
h
h+2
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
17 / 23
h may be 0
- 2
but h+2 > o

---

## Page 66

Correcting imbalance
Slope of a node : self.left.height() - self.right.height()
Balanced tree — slope is {→1, 0, 1}
t.insert(v), t.delete(v) can alter slope to →2 or +2
Left rotation
•
h
h+2
=
•
↭
h
L
h/
h+1
R
h/
h+1
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
17 / 23
J

---

## Page 67

Correcting imbalance
Slope of a node : self.left.height() - self.right.height()
Balanced tree — slope is {→1, 0, 1}
t.insert(v), t.delete(v) can alter slope to →2 or +2
Left rotation — converts slope →2 to {0, 1, 2}
•
h
h+2
=
•
↭
h
L
h/
h+1
R
h/
h+1
=↑
↭
•
h
L
h/
h+1
R
h/
h+1
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
17 / 23
0 -
e
L -
g
O
.o
--

---

## Page 68

Correcting imbalance
Slope of a node : self.left.height() - self.right.height()
Balanced tree — slope is {→1, 0, 1}
t.insert(v), t.delete(v) can alter slope to →2 or +2
Right rotation
•
h+2
h
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
17 / 23

---

## Page 69

Correcting imbalance
Slope of a node : self.left.height() - self.right.height()
Balanced tree — slope is {→1, 0, 1}
t.insert(v), t.delete(v) can alter slope to →2 or +2
Right rotation
•
h+2
h
=
•
↭
h
R
h/
h+1
L
h/
h+1
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
17 / 23

---

## Page 70

Correcting imbalance
Slope of a node : self.left.height() - self.right.height()
Balanced tree — slope is {→1, 0, 1}
t.insert(v), t.delete(v) can alter slope to →2 or +2
Right rotation — converts slope +2 to {→2, →1, 0}
•
h+2
h
=
•
↭
h
R
h/
h+1
L
h/
h+1
=↑
↭
•
h
R
h/
h+1
L
h/
h+1
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
17 / 23
O

---

## Page 71

Implementing rotations
•
v
↭vr
h
L
h/
h+1
R
h/
h+1
↓
↭vr
•
v
h
L
h/
h+1
R
h/
h+1
class Tree:
...
def leftrotate(self):
v = self.value
vr = self.right.value
tl = self.left
trl = self.right.left
trr = self.right.right
newleft = Tree(v)
newleft.left = tl
newleft.right = trl
self.value = vr
self.left = newleft
self.right = trr
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
18 / 23

---

## Page 72

Implementing rotations
• v
↭
vl
h
R
h/
h+1
L
h/
h+1
↓
↭
vl
• v
h
R
h/
h+1
L
h/
h+1
class Tree:
...
def rightrotate(self):
v = self.value
vl = self.left.value
tll = self.left.left
tlr = self.left.right
tr = self.right
newright = Tree(v)
newright.left = tlr
newright.right = tr
self.value = vl
self.left = tll
self.right = newright
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
19 / 23

---

## Page 73

Rebalancing, root has slope +2
Rebalance bottom-up, assume subtrees
are balanced
•
↭
R
L
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
20 / 23

---

## Page 74

Rebalancing, root has slope +2
Rebalance bottom-up, assume subtrees
are balanced
Case 1: Slope at ↭is in {0, 1}
•
↭
h
R
h/
h+1
L
h+1
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
20 / 23
-
h+z

---

## Page 75

Rebalancing, root has slope +2
Rebalance bottom-up, assume subtrees
are balanced
Case 1: Slope at ↭is in {0, 1}
Rotate right at •
All nodes are balanced
↭
•
h
R
h/
h+1
L
h+1
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
20 / 23

---

## Page 76

Rebalancing, root has slope +2
Rebalance bottom-up, assume subtrees
are balanced
Case 1: Slope at ↭is in {0, 1}
Rotate right at •
All nodes are balanced
Case 2: Slope at ↭is →1
•
↭
h
R
h+1
L
h
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
20 / 23
E-1,0,

---

## Page 77

Rebalancing, root has slope +2
Rebalance bottom-up, assume subtrees
are balanced
Case 1: Slope at ↭is in {0, 1}
Rotate right at •
All nodes are balanced
Case 2: Slope at ↭is →1
Expand R
•
↭
↫
h
Y
h/
h→1
X
h/
h→1
L
h
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
20 / 23

---

## Page 78

Rebalancing, root has slope +2
Rebalance bottom-up, assume subtrees
are balanced
Case 1: Slope at ↭is in {0, 1}
Rotate right at •
All nodes are balanced
Case 2: Slope at ↭is →1
Expand R
Rotate left at ↭
•
↫
↭
h
Y
h/
h→1
X
h/
h→1
L
h
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
20 / 23

---

## Page 79

Rebalancing, root has slope +2
Rebalance bottom-up, assume subtrees
are balanced
Case 1: Slope at ↭is in {0, 1}
Rotate right at •
All nodes are balanced
Case 2: Slope at ↭is →1
Expand R
Rotate left at ↭
Rotate left at •
↫
•
↭
h
Y
h/
h→1
X
h/
h→1
L
h
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
20 / 23

---

## Page 80

Rebalancing, root has slope +2
Rebalance bottom-up, assume subtrees
are balanced
Case 1: Slope at ↭is in {0, 1}
Rotate right at •
All nodes are balanced
Case 2: Slope at ↭is →1
Expand R
Rotate left at ↭
Rotate left at •
Rebalance with root slope →2 is
symmetric
↫
•
↭
h
Y
h/
h→1
X
h/
h→1
L
h
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
20 / 23

---

## Page 81

Update insert() and delete()
Use the rebalancing strategy to
define a function rebalance()
Rebalance each time the tree is
modified
Automatically rebalances bottom
up
class Tree:
...
def insert(self,v):
if self.isempty():
self.value = v
self.left = Tree()
self.right = Tree()
if self.value == v:
return
if v < self.value:
self.left.insert(v)
self.left.rebalance()
return
if v > self.value:
self.right.insert(v)
self.right.rebalance()
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
21 / 23

---

## Page 82

Update insert() and delete()
Use the rebalancing strategy to
define a function rebalance()
Rebalance each time the tree is
modified
Automatically rebalances bottom
up
class Tree:
...
def delete(self,v):
...
if v < self.value:
self.left.delete(v)
self.left.rebalance()
return
if v > self.value:
self.right.delete(v)
self.right.rebalance()
return
if v == self.value:
if self.isleaf():
self.makeempty()
elif self.left.isempty():
self.copyright()
elif self.right.isempty():
self.copyleft()
else:
self.value = self.left.maxval()
self.left.delete(self.left.maxval())
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
21 / 23

---

## Page 83

Computing slope
To compute the slope we need
heights of subtrees
But, computing height is O(n)
class Tree:
...
def height(self):
if self.isempty():
return(0)
else:
return(1 +
max(self.left.height(),
self.right.height())
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
22 / 23

---

## Page 84

Computing slope
To compute the slope we need
heights of subtrees
But, computing height is O(n)
Instead, maintain a field
self.height
class Tree:
...
def height(self):
if self.isempty():
return(0)
else:
return(1 +
max(self.left.height(),
self.right.height())
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
22 / 23

---

## Page 85

Computing slope
To compute the slope we need
heights of subtrees
But, computing height is O(n)
Instead, maintain a field
self.height
After each modification, update
self.height based on
self.left.height,
self.right.height
class Tree:
...
def insert(self,v):
...
if v < self.value:
self.left.insert(v)
self.left.rebalance()
self.height = 1 +
max(self.left.height,
self.right.height)
return
if v > self.value:
self.right.insert(v)
self.right.rebalance()
self.height = 1 +
max(self.left.height,
self.right.height)
return
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
22 / 23

---

## Page 86

Summary
Using rotations, we can maintain height balance
Height balanced trees have height O(log n)
find(), insert() and delete() all walk down a single path, take time O(log n)
Madhavan Mukund
Lecture 24, 11 November 2025
PDSP Lecture 24
23 / 23