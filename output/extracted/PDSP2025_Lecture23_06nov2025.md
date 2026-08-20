## Page 1

Lecture 23, 6 November 2025
Madhavan Mukund
https://www.cmi.ac.in/~madhavan
Programming and Data Structures with Python
Lecture 23, 06 Nov 2025

---

## Page 2

Data Structures
Information
+
Operations
List
-
implemented
as
a flexible array
Dictionary

---

## Page 3

Stack
Stack is a last-in, first-out sequence
push(s,x) — add x to stack s
pop(s) — return most recently added
element
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
2 / 22
pops&
Push

---

## Page 4

Stack
Stack is a last-in, first-out sequence
push(s,x) — add x to stack s
pop(s) — return most recently added
element
Maintain stack as list, push and pop
from the right
push(s,x) is s.append(x)
s.pop() — Python built-in, returns
last element
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
2 / 22

---

## Page 5

Stack
Stack is a last-in, first-out sequence
push(s,x) — add x to stack s
pop(s) — return most recently added
element
Maintain stack as list, push and pop
from the right
push(s,x) is s.append(x)
s.pop() — Python built-in, returns
last element
Stack defined using classes:
s.push(x), s.pop()
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
2 / 22

---

## Page 6

Stack
Stack is a last-in, first-out sequence
push(s,x) — add x to stack s
pop(s) — return most recently added
element
Maintain stack as list, push and pop
from the right
push(s,x) is s.append(x)
s.pop() — Python built-in, returns
last element
Stack defined using classes:
s.push(x), s.pop()
Stack as an abstract datatype (ADT)
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
2 / 22
# (sush(r)pop
sisempty ()

---

## Page 7

Stack
Stack is a last-in, first-out sequence
push(s,x) — add x to stack s
pop(s) — return most recently added
element
Maintain stack as list, push and pop
from the right
push(s,x) is s.append(x)
s.pop() — Python built-in, returns
last element
Stack defined using classes:
s.push(x), s.pop()
Stack as an abstract datatype (ADT)
Stacks are natural to keep track of local
variables through function calls
Each function call pushes current
frame onto a stack
When function exits, pop its frame o!
the stack
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
2 / 22
fact(n) = n fact(n
-)
Fren
GE

---

## Page 8

Queue
First-in, first-out sequence
addq(q,x) — adds x to rear of queue q
removeq(q) — removes element at head of q
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
3 / 22
:enter

. add(2)
gremoeg()

---

## Page 9

Queue
First-in, first-out sequence
addq(q,x) — adds x to rear of queue q
removeq(q) — removes element at head of q
Using Python lists, left is rear, right is front
addq(q,x) is q.insert(0,x)
insert(j,x), insert x before position j
removeq(q) is q.pop()
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
3 / 22
top

---

## Page 10

Systematic exploration
Rectangular m →n grid
Chess knight starts at (sx, sy) •
Usual knight moves
Can it reach a target square (tx, ty)? ↭
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
4 / 22
-
·↑

---

## Page 11

Systematic exploration
Rectangular m →n grid
Chess knight starts at (sx, sy) •
Usual knight moves
Can it reach a target square (tx, ty)? ↭
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
4 / 22

---

## Page 12

Systematic exploration
Rectangular m →n grid
Chess knight starts at (sx, sy) •
Usual knight moves
Can it reach a target square (tx, ty)? ↭
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
4 / 22

---

## Page 13

Systematic exploration
Rectangular m →n grid
Chess knight starts at (sx, sy) •
Usual knight moves
Can it reach a target square (tx, ty)? ↭
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
4 / 22

---

## Page 14

Systematic exploration
X1 — all squares reachable in one
move from (sx, sy)
X2 —- all squares reachable from X1 in
one move
. . .
Don't explore an already marked square
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
5 / 22
E

---

## Page 15

Systematic exploration
X1 — all squares reachable in one
move from (sx, sy)
X2 —- all squares reachable from X1 in
one move
. . .
Don't explore an already marked square
When do we stop?
If we reach target square
What if target is not reachable?
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
5 / 22

---

## Page 16

Systematic exploration
X1 — all squares reachable in one
move from (sx, sy)
X2 —- all squares reachable from X1 in
one move
. . .
Don't explore an already marked square
When do we stop?
If we reach target square
What if target is not reachable?
Maintain a queue Q of cells to be
explored
Initially Q contains only start node
(sx, sy)
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
5 / 22

---

## Page 17

Systematic exploration
X1 — all squares reachable in one
move from (sx, sy)
X2 —- all squares reachable from X1 in
one move
. . .
Don't explore an already marked square
When do we stop?
If we reach target square
What if target is not reachable?
Maintain a queue Q of cells to be
explored
Initially Q contains only start node
(sx, sy)
Remove (ax, ay) from head of queue
Mark all squares reachable in one step
from (ax, ay)
Add all newly marked squares to the
queue
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
5 / 22

---

## Page 18

Systematic exploration
X1 — all squares reachable in one
move from (sx, sy)
X2 —- all squares reachable from X1 in
one move
. . .
Don't explore an already marked square
When do we stop?
If we reach target square
What if target is not reachable?
Maintain a queue Q of cells to be
explored
Initially Q contains only start node
(sx, sy)
Remove (ax, ay) from head of queue
Mark all squares reachable in one step
from (ax, ay)
Add all newly marked squares to the
queue
When the queue is empty, we have
finished
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
5 / 22

---

## Page 19

Dealing with priorities
Job scheduler
A job scheduler maintains a list of
pending jobs with their priorities
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
6 / 22

---

## Page 20

Dealing with priorities
Job scheduler
A job scheduler maintains a list of
pending jobs with their priorities
When the processor is free, the
scheduler picks out the job with
maximum priority in the list and
schedules it
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
6 / 22

---

## Page 21

Dealing with priorities
Job scheduler
A job scheduler maintains a list of
pending jobs with their priorities
When the processor is free, the
scheduler picks out the job with
maximum priority in the list and
schedules it
New jobs may join the list at any time
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
6 / 22

---

## Page 22

Dealing with priorities
Job scheduler
A job scheduler maintains a list of
pending jobs with their priorities
When the processor is free, the
scheduler picks out the job with
maximum priority in the list and
schedules it
New jobs may join the list at any time
How should the scheduler maintain the
list of pending jobs and their priorities?
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
6 / 22

---

## Page 23

Dealing with priorities
Job scheduler
A job scheduler maintains a list of
pending jobs with their priorities
When the processor is free, the
scheduler picks out the job with
maximum priority in the list and
schedules it
New jobs may join the list at any time
How should the scheduler maintain the
list of pending jobs and their priorities?
Priority queue
Need to maintain a collection of items
with priorities to optimise the following
operations
delete max()
Identify and remove item with highest
priority
Need not be unique
insert()
Add a new item to the collection
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
6 / 22

---

## Page 24

Implementing priority queues with one dimensional structures
delete_max()
Identify and remove item with highest
priority
Need not be unique
insert()
Add a new item to the list
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
7 / 22

---

## Page 25

Implementing priority queues with one dimensional structures
Unsorted list
insert() is O(1)
delete max() is O(n)
delete_max()
Identify and remove item with highest
priority
Need not be unique
insert()
Add a new item to the list
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
7 / 22
#
-
↑
max

---

## Page 26

Implementing priority queues with one dimensional structures
Unsorted list
insert() is O(1)
delete max() is O(n)
Sorted list
delete max() is O(1)
insert() is O(n)
delete_max()
Identify and remove item with highest
priority
Need not be unique
insert()
Add a new item to the list
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
7 / 22
↑
Insertion Sort

---

## Page 27

Implementing priority queues with one dimensional structures
Unsorted list
insert() is O(1)
delete max() is O(n)
Sorted list
delete max() is O(1)
insert() is O(n)
Processing n items requires O(n2)
delete_max()
Identify and remove item with highest
priority
Need not be unique
insert()
Add a new item to the list
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
7 / 22

---

## Page 28

Moving to two dimensions
First attempt
Assume N processes enter/leave the
queue
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
8 / 22

---

## Page 29

Moving to two dimensions
First attempt
Assume N processes enter/leave the
queue
Maintain a
↑
N →
↑
N array
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
8 / 22
-
-
~
-
-
>
&
-

---

## Page 30

Moving to two dimensions
First attempt
Assume N processes enter/leave the
queue
Maintain a
↑
N →
↑
N array
Each row is in sorted order
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
8 / 22

---

## Page 31

insert()
Keep track of the size of each row
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
9 / 22

---

## Page 32

insert()
Keep track of the size of each row
Insert into the first row that has space
Use size of row to determine
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
9 / 22

---

## Page 33

insert()
Keep track of the size of each row
Insert into the first row that has space
Use size of row to determine
Insert 15
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
9 / 22

---

## Page 34

insert()
Keep track of the size of each row
Insert into the first row that has space
Use size of row to determine
Insert 15
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
9 / 22

---

## Page 35

insert()
Keep track of the size of each row
Insert into the first row that has space
Use size of row to determine
Insert 15
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
9 / 22

---

## Page 36

insert()
Keep track of the size of each row
Insert into the first row that has space
Use size of row to determine
Insert 15
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
9 / 22

---

## Page 37

insert()
Keep track of the size of each row
Insert into the first row that has space
Use size of row to determine
Insert 15
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
9 / 22

---

## Page 38

insert()
Keep track of the size of each row
Insert into the first row that has space
Use size of row to determine
Insert 15
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
9 / 22

---

## Page 39

insert()
Keep track of the size of each row
Insert into the first row that has space
Use size of row to determine
Insert 15
Takes time O(
↑
N)
Scan size column to locate row to insert,
O(
↑
N)
Insert into the first row with free space,
O(
↑
N)
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
9 / 22

---

## Page 40

delete max()
Maximum in each row is the last element
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
10 / 22

---

## Page 41

delete max()
Maximum in each row is the last element
Position is available through size column
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
10 / 22
S

---

## Page 42

delete max()
Maximum in each row is the last element
Position is available through size column
Identify the maximum amongst these
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
10 / 22
oo

---

## Page 43

delete max()
Maximum in each row is the last element
Position is available through size column
Identify the maximum amongst these
Delete it
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
10 / 22
O

---

## Page 44

delete max()
Maximum in each row is the last element
Position is available through size column
Identify the maximum amongst these
Delete it
Again O(
↑
N)
Find the maximum among last entries,
O(
↑
N)
Delete it, O(1)
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
10 / 22

---

## Page 45

Summary
2D
↑
N →
↑
N array with sorted rows
insert() is O(
↑
N)
delete max() is O(
↑
N)
Processing N items is O(N
↑
N)
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
11 / 22
Nlog N

---

## Page 46

Summary
2D
↑
N →
↑
N array with sorted rows
insert() is O(
↑
N)
delete max() is O(
↑
N)
Processing N items is O(N
↑
N)
Can we do better?
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
11 / 22

---

## Page 47

Summary
2D
↑
N →
↑
N array with sorted rows
insert() is O(
↑
N)
delete max() is O(
↑
N)
Processing N items is O(N
↑
N)
Can we do better?
Maintain a special binary tree — heap
Height O(log N)
insert() is O(log N)
delete max() is O(log N)
Processing N items is O(N log N)
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
11 / 22

---

## Page 48

Summary
2D
↑
N →
↑
N array with sorted rows
insert() is O(
↑
N)
delete max() is O(
↑
N)
Processing N items is O(N
↑
N)
Can we do better?
Maintain a special binary tree — heap
Height O(log N)
insert() is O(log N)
delete max() is O(log N)
Processing N items is O(N log N)
Flexible — need not fix N in advance
N = 25

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
11 / 22

---

## Page 49

Binary trees
Values are stored as nodes in a
rooted tree
Each node has up to two
children
Left child and right child
Order is important
Other than the root, each node
has a unique parent
Leaf node — no children
Size — number of nodes
Height — number of levels

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
12 / 22
↓
-
root
-Parent
YI
left child
right child

---

## Page 50

Heap
Binary tree filled level by level,
left to right
The value at each node is at
least as big the values of its
children
max-heap

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
13 / 22
-
a/557
da3

---

## Page 51

Heap
Binary tree filled level by level,
left to right
The value at each node is at
least as big the values of its
children
max-heap

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
13 / 22
?

=

I II

---

## Page 52

Heap
Binary tree filled level by level,
left to right
The value at each node is at
least as big the values of its
children
max-heap
Binary tree on the right is an
example of a heap

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
13 / 22

---

## Page 53

Heap
Binary tree filled level by level,
left to right
The value at each node is at
least as big the values of its
children
max-heap
Binary tree on the right is an
example of a heap
Root always has the largest
value
By induction, because of the
max-heap property

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
13 / 22
largest
E
Of

---

## Page 54

Non-examples
No "holes" allowed

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
14 / 22
i
o?

---

## Page 55

Non-examples
No "holes" allowed

Cannot leave a level incomplete

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
14 / 22
iC
G

---

## Page 56

Non-examples
Heap property is violated

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
15 / 22
O

---

## Page 57

insert()
insert(77)

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
16 / 22
↓

---

## Page 58

insert()
insert(77)
Add a new node at dictated by
heap structure

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
16 / 22
?

---

## Page 59

insert()
insert(77)
Add a new node at dictated by
heap structure
Restore the heap property along
path to the root

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
16 / 22
?

---

## Page 60

insert()
insert(77)
Add a new node at dictated by
heap structure
Restore the heap property along
path to the root

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
16 / 22
74Fi
?

---

## Page 61

insert()
insert(77)
Add a new node at dictated by
heap structure
Restore the heap property along
path to the root
insert(44)

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
16 / 22
b

---

## Page 62

insert()
insert(77)
Add a new node at dictated by
heap structure
Restore the heap property along
path to the root
insert(44)
insert(57)

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
16 / 22
O

---

## Page 63

insert()
insert(77)
Add a new node at dictated by
heap structure
Restore the heap property along
path to the root
insert(44)
insert(57)

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
16 / 22
~

---

## Page 64

Complexity of insert()
Need to walk up from the leaf to
the root
Height of the tree

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
17 / 22

---

## Page 65

Complexity of insert()
Need to walk up from the leaf to
the root
Height of the tree
Number of nodes at level 0 is
20 = 1

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
17 / 22

---

## Page 66

Complexity of insert()
Need to walk up from the leaf to
the root
Height of the tree
Number of nodes at level 0 is
20 = 1
Number of nodes at level j is 2j

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
17 / 22
O
I

---

## Page 67

Complexity of insert()
Need to walk up from the leaf to
the root
Height of the tree
Number of nodes at level 0 is
20 = 1
Number of nodes at level j is 2j
If we fill k levels,
20 + 21 + · · · + 2k→1 = 2k ↓1
nodes

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
17 / 22

---

## Page 68

Complexity of insert()
Need to walk up from the leaf to
the root
Height of the tree
Number of nodes at level 0 is
20 = 1
Number of nodes at level j is 2j
If we fill k levels,
20 + 21 + · · · + 2k→1 = 2k ↓1
nodes
If we have N nodes, at most
1 + log N levels

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
17 / 22

---

## Page 69

Complexity of insert()
Need to walk up from the leaf to
the root
Height of the tree
Number of nodes at level 0 is
20 = 1
Number of nodes at level j is 2j
If we fill k levels,
20 + 21 + · · · + 2k→1 = 2k ↓1
nodes
If we have N nodes, at most
1 + log N levels
insert() is O(log N)

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
17 / 22

---

## Page 70

delete max()
Maximum value is always at the
root

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
18 / 22
-I

---

## Page 71

delete max()
Maximum value is always at the
root
After we delete one value, tree
shrinks
Node to delete is rightmost at
lowest level

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
18 / 22

---

## Page 72

delete max()
Maximum value is always at the
root
After we delete one value, tree
shrinks
Node to delete is rightmost at
lowest level
Move "homeless" value to the
root

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
18 / 22
↳

---

## Page 73

delete max()
Maximum value is always at the
root
After we delete one value, tree
shrinks
Node to delete is rightmost at
lowest level
Move "homeless" value to the
root
Restore the heap property
downwards

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
18 / 22

---

## Page 74

delete max()
Maximum value is always at the
root
After we delete one value, tree
shrinks
Node to delete is rightmost at
lowest level
Move "homeless" value to the
root
Restore the heap property
downwards
Only need to follow a single path
down
Again O(log N)

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
18 / 22
①

---

## Page 75

delete max()
Maximum value is always at the
root
After we delete one value, tree
shrinks
Node to delete is rightmost at
lowest level
Move "homeless" value to the
root
Restore the heap property
downwards
Only need to follow a single path
down
Again O(log N)

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
18 / 22
⑰

---

## Page 76

delete max()
Maximum value is always at the
root
After we delete one value, tree
shrinks
Node to delete is rightmost at
lowest level
Move "homeless" value to the
root
Restore the heap property
downwards
Only need to follow a single path
down
Again O(log N)

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
18 / 22

---

## Page 77

Implementation
Number the nodes top to
bottom, left to right
Store as a list
H = [h0,h1,h2,...,h9]
Children of H[i] are at
H[2*i+1], H[2*i+2]
H[i] is a leaf if 2*i+1 ↔N
Parent of H[i], for i > 0,
is H[(i-1)//2]
h0
h1
h3
h7
h8
h4
h9
h2
h5
h6
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
19 / 22·
-

---

## Page 78

Building a heap — heapify()
Convert a list [v0,v1,...,vN]
into a heap
h0
h1
h3
h7
h8
h4
h9
h2
h5
h6
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
20 / 22

---

## Page 79

Building a heap — heapify()
Convert a list [v0,v1,...,vN]
into a heap
Simple strategy
Start with an empty heap
Repeatedly apply insert(vj)
Total time is O(N log N)
h0
h1
h3
h7
h8
h4
h9
h2
h5
h6
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
20 / 22

---

## Page 80

Heap sort
Start with an unordered list
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
21 / 22

---

## Page 81

Heap sort
Start with an unordered list
Build a heap — O(N log N)
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
21 / 22

---

## Page 82

Heap sort
Start with an unordered list
Build a heap — O(N log N)
Call delete max() N times to extract elements in descending order — O(N log N)
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
21 / 22

---

## Page 83

Heap sort
Start with an unordered list
Build a heap — O(N log N)
Call delete max() N times to extract elements in descending order — O(N log N)
After each delete max(), heap shrinks by 1
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
21 / 22
-
O
N-1
#

---

## Page 84

Heap sort
Start with an unordered list
Build a heap — O(N log N)
Call delete max() N times to extract elements in descending order — O(N log N)
After each delete max(), heap shrinks by 1
Store maximum value at the end of current heap
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
21 / 22

---

## Page 85

Heap sort
Start with an unordered list
Build a heap — O(N log N)
Call delete max() N times to extract elements in descending order — O(N log N)
After each delete max(), heap shrinks by 1
Store maximum value at the end of current heap
In place O(N log N) sort
Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
21 / 22

---

## Page 86

Summary
Heaps are a tree implementation
of priority queues
insert() is O(log N)
delete max() is O(log N)
heapify() builds a heap in
O(N)

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
22 / 22

---

## Page 87

Summary
Heaps are a tree implementation
of priority queues
insert() is O(log N)
delete max() is O(log N)
heapify() builds a heap in
O(N)
Can invert the heap condition
Each node is smaller than its
children
min-heap
delete min() rather than
delete max()

Madhavan Mukund
Lecture 23, 6 November 2025
PDSP Lecture 23
22 / 22