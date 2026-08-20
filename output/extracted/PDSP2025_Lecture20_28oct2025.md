## Page 1

Lecture 21, 28 October 2025
Madhavan Mukund
https://www.cmi.ac.in/~madhavan
Programming and Data Structures with Python
Lecture 21, 28 Oct 2025

---

## Page 2

Asymptotic worst-case complexity
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
2 / 14
Worst Case
- reconstruct the most complicated
imput
T(n)
- a
input size
flul = O(g(n))
7c
. En
f(u) < (g(n)
SSu+ 312n ~0(nz)

---

## Page 3

Orders of magnitude
Input size
Values of t(n)
log n
n
n log n
n2
n3
2n
n!

3.3

1000
1000

6.6

1030
10157
1000

1000

1012

1010

1012

1010
1010

1010
1011
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
3 / 14
~

---

## Page 4

Searching
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
4 / 14
Unsuited sequence
- O(n)
Win
Sorted Sequence
- binary
search
Ollogz(n)
-
-
min
max
O
len(e)/2
lan(l)
- 1
loglu)
steps
-
>
search
interval is

---

## Page 5

Searching
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
4 / 14
logz(n)
vo logs (n)

---

## Page 6

Searching a sorted list — binary search
def binarysearch(v,l):
if l == []:
return(False)
m = len(l)//2
if v == l[m]:
return(True)
if v < l[m]:
return(binarysearch(v,l[:m]))
else:
return(binarysearch(v,l[m+1:]))
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
5 / 14

---

## Page 7

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
6 / 14
Binary
Search requires
a sorted
list
Ascending order
Two
"intuitive" strategies

---

## Page 8

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
6 / 14
Compute
⑭
min/max i
513 14 22374168
one pass
4168
[
"Selection Sort"

---

## Page 9

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
6 / 14
Space-building
a new
list
- Avoid ?
-
14 22 13 041537
-
68 at end
-
14221337415168
Fa
221337511468
%
in find posite
↳
sorted
unsorted
LINVARIANT -

---

## Page 10

Selection sort
def SelectionSort(L):
n = len(L)
if n < 1:
return(L)
for i in range(n):
# Assume L[:i] is sorted
mpos = i
# mpos: position of minimum in L[i:]
for j in range(i+1,n):
if L[j] < L[mpos]:
mpos = j
# L[mpos] : smallest value in L[i:]
# Exchange L[mpos] and L[i]
(L[i],L[mpos]) = (L[mpos],L[i])
# Now L[:i+1] is sorted
return(L)
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
7 / 14
I Base case *
-
-

---

## Page 11

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
8 / 14
Analysis
of
Selection
Sort ?
-
Find
min of C[0 :n]
m -
For
an of [1
:2]
i
n
1 +2+
-
+ n
Ei
+) = = 0(nz)

---

## Page 12

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
8 / 14
Selection sait always
takes
n++) +nz --H steps
Check
ifI
is
sorted
in
one pass)
&
Es

-
WorstCase
apples to
may input

---

## Page 13

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
8 / 14
Another natural sort
Insect each book
in
ored
-
#
its
correct place
I
&
Insertin
Sort
s

---

## Page 14

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
8 / 14
i

---

## Page 15

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
8 / 14
In
place#28
H
unsorted
12 551682

---

## Page 16

Insertion sort
def InsertionSort(L):
n = len(L)
if n < 1:
return(L)
for i in range(n):
# Assume L[:i] is sorted
# Move L[i] to correct position in L[:i]
j = i
while(j > 0 and L[j] < L[j-1]):
(L[j],L[j-1]) = (L[j-1],L[j])
j = j-1
# Now L[:i+1] is sorted
return(L)
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
9 / 14
Tortell
unsorted
Invariant
-
-
- Extended sorted segment

---

## Page 17

Insertion sort
def InsertionSort(L):
n = len(L)
if n < 1:
return(L)
for i in range(n):
# Assume L[:i] is sorted
# Move L[i] to correct position in L[:i]
j = i
while(j > 0 and L[j] < L[j-1]):
(L[j],L[j-1]) = (L[j-1],L[j])
j = j-1
# Now L[:i+1] is sorted
return(L)
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
9 / 14

---

## Page 18

Analysis of
insertion sort
#
↑
0 +H · +n-1
Descending nch
Sh
32 /
- O(n)
Es
-

---

## Page 19

What if
Input is
already
sorted ?
10.

1 1
O(n)
"Almost"
sorted
lists
- good

---

## Page 20

Insertion sort
def InsertionSort(L):
n = len(L)
if n < 1:
return(L)
for i in range(n):
# Assume L[:i] is sorted
# Move L[i] to correct position in L[:i]
j = i
while(j > 0 and L[j] < L[j-1]):
(L[j],L[j-1]) = (L[j-1],L[j])
j = j-1
# Now L[:i+1] is sorted
return(L)
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
9 / 14

---

## Page 21

Recursively
Insert operation
-
Insert (e, u)
=C + [r] if CES e[w]
If
CF1] > er]
Insert (eC : -D,v) +[e[T]

---

## Page 22

left to
right
If
v = 10]
return
[v]+e
de
retur [e03]+
Insect (v, &[1 :5)

---

## Page 23

Insertion
Sort
Sort
&[1 :3
Insert
IO] into this
list

---

## Page 24

Insertion sort
def Insert(L,v):
n = len(L)
if n == 0:
return([v])
if v >= L[-1]:
return(L+[v])
else:
return(Insert(L[:-1],v)+L[-1:])
def ISort(L):
n = len(L)
if n < 1:
return(L)
L = Insert(ISort(L[:-1]),L[-1])
return(L)
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
10 / 14
-
Analysis?
-
stick v at end
TI(n)
-
Insert vin
n elem list
--
TS(m)
- Sortn elements
-
-
using insertion
-

---

## Page 25

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
11 / 14
Insertion
-
TI(0)
=

Basele/
Inductive Step
/T
T

---

## Page 26

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
11 / 14
Isot
.
Ts (b)
=

is (n)
= TS(n -T +TI(n-D
↓
n- 1
TS(n-2) +TI(n-2)
·i /
n tim
TS(0) ++(0)
12+ -(n -2) + 1n+)

---

## Page 27

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
11 / 14
2 "name" sorting algorithms
- both 0(nz)
Different strategy
in
exam papers , graded, to
sort by
marks
↑
n/2
N/2
Split the
work to
2 TAs
↓
↓
sorted
sorted

---

## Page 28

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
11 / 14
684436/377273
446886/327392
"Merge" there
sorted lists
i
smalle,

---

## Page 29

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
11 / 14
uBe
Each
N -
comparison
-is
adds
one
N -
item to

compare
sorted output
more smalle o
In outputs
sorted
In steps

---

## Page 30

Sorting
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
11 / 14
Boundary
word
X
X
34X
-
Is
1234

---

## Page 31

Merging sorted lists
def merge(A,B):
(m,n) = (len(A),len(B))
(C,i,j,k) = ([],0,0,0)
while k < m+n:
if i == m:
C.extend(B[j:])
k = k + (n-j)
elif j == n:
C.extend(A[i:])
k = k + (m-i)
elif A[i] < B[j]:
C.append(A[i])
(i,k) = (i+1,k+1)
else:
C.append(B[j])
(j,k) = (j+1,k+1)
return(C)
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
12 / 14
-
=
i
L
---
-
---
a T
↓
B
-
↑
↳

---

## Page 32

Merge sort
def merge(A,B):
(m,n) = (len(A),len(B))
(C,i,j,k) = ([],0,0,0)
while k < m+n:
if i == m:
C.extend(B[j:])
k = k + (n-j)
elif j == n:
C.extend(A[i:])
k = k + (m-i)
elif A[i] < B[j]:
C.append(A[i])
(i,k) = (i+1,k+1)
else:
C.append(B[j])
(j,k) = (j+1,k+1)
return(C)
def mergesort(A):
n = len(A)
if n <= 1:
return(A)
L = mergesort(A[:n//2])
R = mergesort(A[n//2:])
B = merge(L,R)
return(B)
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
13 / 14
G
-
-

---

## Page 33

Merge sort
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
14 / 14
12/72(93/15/23/14/73/62

72 931526

75 62
it
X
'·

IS

62727593

---

## Page 34

Merge sort analysis
Madhavan Mukund
Lecture 21, 28 October 2025
PDSP Lecture 21
15 / 14
Dinde & conquer
Analysis
?