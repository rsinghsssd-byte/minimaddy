## Page 1

Lecture 25, 18 November 2025
Madhavan Mukund
https://www.cmi.ac.in/~madhavan
Programming and Data Structures with Python
Lecture 25, 18 Nov 2025

---

## Page 2

Inductive definitions, recursive programs, subproblems
Factorial
fact(0) = 1
fact(n) = n →fact(n ↑1)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
2 / 33

---

## Page 3

Inductive definitions, recursive programs, subproblems
Factorial
fact(0) = 1
fact(n) = n →fact(n ↑1)
def fact(n):
if n <= 0:
return(1)
else:
return(n * fact(n-1))
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
2 / 33

---

## Page 4

Inductive definitions, recursive programs, subproblems
Factorial
fact(0) = 1
fact(n) = n →fact(n ↑1)
def fact(n):
if n <= 0:
return(1)
else:
return(n * fact(n-1))
Insertion sort
isort([ ]) = [ ]
isort([x0, x1, . . . , xn]) =
insert(isort([x0, x1, . . . , xn→1]), xn)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
2 / 33

---

## Page 5

Inductive definitions, recursive programs, subproblems
Factorial
fact(0) = 1
fact(n) = n →fact(n ↑1)
def fact(n):
if n <= 0:
return(1)
else:
return(n * fact(n-1))
Insertion sort
isort([ ]) = [ ]
isort([x0, x1, . . . , xn]) =
insert(isort([x0, x1, . . . , xn→1]), xn)
fact(n↑1) is a subproblem of fact(n)
So are fact(n↑2), fact(n↑3), . . . ,
fact(0)
isort([x0, x1, . . . , xn→1]) is a subproblem
of isort([x0, x1, . . . , xn])
So is isort([x0, . . . , xj]) for any
0 < j < n
Solution to original problem can be
derived by combining solutions to
subproblems
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
2 / 33
Tradeoff-cost of recursive calls

---

## Page 6

Evaluating subproblems
Fibonacci numbers
fib(0) = 0
fib(1) = 1
fib(n) = fib(n↑1) + fib(n↑2)
def fib(n):
if n <= 1:
value = n
else:
value = fib(n-1) + fib(n-2)
return(value)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
3 / 33

12345
-

fib(5)

---

## Page 7

Evaluating subproblems
Fibonacci numbers
fib(0) = 0
fib(1) = 1
fib(n) = fib(n↑1) + fib(n↑2)
def fib(n):
if n <= 1:
value = n
else:
value = fib(n-1) + fib(n-2)
return(value)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
3 / 33
f.b(5)
f(u) + f(z)
2(a)
1 fute() +c)+(r
fer)"

O

---

## Page 8

Evaluating subproblems
Build a table of values already
computed
Memory table
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
4 / 33

---

## Page 9

Evaluating subproblems
Build a table of values already
computed
Memory table
Memoization
Check if the value to be
computed was already seen
before
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
4 / 33

---

## Page 10

Evaluating subproblems
Build a table of values already
computed
Memory table
Memoization
Check if the value to be
computed was already seen
before
Store each newly computed
value in a table
Look up the table before making
a recursive call
Computation tree becomes linear
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
4 / 33
5 f(5)·
fi *
+(2) r
fitoo

---

## Page 11

Memoizing recursive implmentations
def fib(n):
if n <= 1:
value = n
else:
value = fib(n-1) + fib(n-2)
return(value)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
5 / 33

---

## Page 12

Memoizing recursive implmentations
def fib(n):
if n in fibtable.keys():
return(fibtable[n])
if n <= 1:
value = n
else:
value = fib(n-1) + fib(n-2)
fibtable[n] = value
return(value)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
5 / 33
- fibrable = 23
~

---

## Page 13

Memoizing recursive implmentations
def fib(n):
if n in fibtable.keys():
return(fibtable[n])
if n <= 1:
value = n
else:
value = fib(n-1) + fib(n-2)
fibtable[n] = value
return(value)
In general
def f(x,y,z):
if (x,y,z) in ftable.keys():
return(ftable[(x,y,z)])
recursively compute value
from subproblems
ftable[(x,y,z)] = value
return(value)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
5 / 33

---

## Page 14

Dynamic programming
Anticipate the structure of subproblems
Derive from inductive definition
Dependencies are acyclic
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
6 / 33
Recursion
①-Wasteful recomputation
②lost of
recursive
calls
①
Memorization
②Translate to
iteration

---

## Page 15

Dynamic programming
Anticipate the structure of subproblems
Derive from inductive definition
Dependencies are acyclic
Evaluating fib(5)
fib(5)
fib(4)
fib(3)
fib(2)
fib(1)
fib(0)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
6 / 33
-+ -
01234S
X
i
x
-
-

---

## Page 16

Dynamic programming
Anticipate the structure of subproblems
Derive from inductive definition
Dependencies are acyclic
Solve subproblems in appropriate order
Start with base cases — no
dependencies
Evaluate a value after all its
dependencies are available
Fill table iteratively
Never need to make a recursive call
Evaluating fib(5)
fib(5)
fib(4)
fib(3)
fib(2)
fib(1)
fib(0)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
6 / 33
2123581321
--
--
Eg
-

---

## Page 17

Grid paths
Rectangular grid of one-way roads
Can only go up and right
How many paths from (0, 0) to (m, n)?
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
7 / 33
m+n steps
, each
R--#
e
RURRUV--R

---

(5) (min)(m(

---

## Page 18

Combinatorial solution
Every path from (0, 0) to (5, 10) has 15
segments
Out of 15, exactly 5 are right moves,
10 are up moves
Fix the positions of the 5 right moves
among the 15 positions overall
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
8 / 33

---

## Page 19

Combinatorial solution
Every path from (0, 0) to (5, 10) has 15
segments
Out of 15, exactly 5 are right moves,
10 are up moves
Fix the positions of the 5 right moves
among the 15 positions overall
!15

"
=
15!
10! · 5! = 3003
Same as
!15

"
— fix the 10 up moves
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
8 / 33

---

## Page 20

Combinatorial solution
Every path from (0, 0) to (5, 10) has 15
segments
Out of 15, exactly 5 are right moves,
10 are up moves
Fix the positions of the 5 right moves
among the 15 positions overall
!15

"
=
15!
10! · 5! = 3003
Same as
!15

"
— fix the 10 up moves
In general m+n segments from (0, 0) to
(m, n)
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
8 / 33

---

## Page 21

Holes
What if an intersection is blocked?
For instance, (2, 4)
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
9 / 33
Count paths
(00 - (2,4)
- 1
(2 , 4) - (5, 10)
-e
(2,4)
kot
bad paths
(min)
- k.e

---

## Page 22

Combinatorial solution for holes
Discard paths passing through (2, 4)
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
10 / 33

---

## Page 23

More holes
What if two intersections are blocked?
Discard paths via (2, 4), (4, 4)
Some paths are counted twice
Add back the paths that pass through
both holes
Inclusion-exclusion — counting is messy
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
11 / 33
(2,2)
(4ihl
(2,4)
k -l = A
(4 .4)
Kni = B)You are

---

## Page 24

Inductive formulation
How can a path reach (i, j)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
12 / 33I

---

## Page 25

Inductive formulation
How can a path reach (i, j)
Move up from (i, j ↑1)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
12 / 33

---

## Page 26

Inductive formulation
How can a path reach (i, j)
Move up from (i, j ↑1)
Move right from (i ↑1, j)
(i→1, j)
(i, j→1)
(i, j)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
12 / 33

---

## Page 27

Inductive formulation
How can a path reach (i, j)
Move up from (i, j ↑1)
Move right from (i ↑1, j)
Each path to these neighbours extends
to a unique path to (i, j)
(i→1, j)
(i, j→1)
(i, j)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
12 / 33

---

## Page 28

Inductive formulation
How can a path reach (i, j)
Move up from (i, j ↑1)
Move right from (i ↑1, j)
Each path to these neighbours extends
to a unique path to (i, j)
Recurrence for P(i, j), number of paths
from (0, 0) to (i, j)
P(i, j) = P(i ↑1, j) + P(i, j ↑1)
(i→1, j)
(i, j→1)
(i, j)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
12 / 33

---

## Page 29

Inductive formulation
How can a path reach (i, j)
Move up from (i, j ↑1)
Move right from (i ↑1, j)
Each path to these neighbours extends
to a unique path to (i, j)
Recurrence for P(i, j), number of paths
from (0, 0) to (i, j)
P(i, j) = P(i ↑1, j) + P(i, j ↑1)
P(0, 0) = 1 — base case
(i→1, j)
(i, j→1)
(i, j)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
12 / 33

---

## Page 30

Inductive formulation
How can a path reach (i, j)
Move up from (i, j ↑1)
Move right from (i ↑1, j)
Each path to these neighbours extends
to a unique path to (i, j)
Recurrence for P(i, j), number of paths
from (0, 0) to (i, j)
P(i, j) = P(i ↑1, j) + P(i, j ↑1)
P(0, 0) = 1 — base case
P(i, 0) = P(i ↑1, 0) — bottom row
(i→1, j)
(i, j→1)
(i, j)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
12 / 33

---

## Page 31

Inductive formulation
How can a path reach (i, j)
Move up from (i, j ↑1)
Move right from (i ↑1, j)
Each path to these neighbours extends
to a unique path to (i, j)
Recurrence for P(i, j), number of paths
from (0, 0) to (i, j)
P(i, j) = P(i ↑1, j) + P(i, j ↑1)
P(0, 0) = 1 — base case
P(i, 0) = P(i ↑1, 0) — bottom row
P(0, j) = P(0, j ↑1) — left column
(i→1, j)
(i, j→1)
(i, j)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
12 / 33
P(72]P(l-i ,i)
P(u ,j)
IsS

---

## Page 32

Inductive formulation
How can a path reach (i, j)
Move up from (i, j ↑1)
Move right from (i ↑1, j)
Each path to these neighbours extends
to a unique path to (i, j)
Recurrence for P(i, j), number of paths
from (0, 0) to (i, j)
P(i, j) = P(i ↑1, j) + P(i, j ↑1)
P(0, 0) = 1 — base case
P(i, 0) = P(i ↑1, 0) — bottom row
P(0, j) = P(0, j ↑1) — left column
P(i, j) = 0 if there is a hole at (i, j)
(i→1, j)
(i, j→1)
(i, j)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
12 / 33

---

## Page 33

Computing P(i, j)
Naive recursion recomputes same
subproblem repeatedly
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
13 / 33

---

## Page 34

Computing P(i, j)
Naive recursion recomputes same
subproblem repeatedly
P(5, 10) requires P(4, 10), P(5, 9)
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
13 / 33

---

## Page 35

Computing P(i, j)
Naive recursion recomputes same
subproblem repeatedly
P(5, 10) requires P(4, 10), P(5, 9)
Both P(4, 10), P(5, 9) require P(4, 9)
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
13 / 33

---

## Page 36

Computing P(i, j)
Naive recursion recomputes same
subproblem repeatedly
P(5, 10) requires P(4, 10), P(5, 9)
Both P(4, 10), P(5, 9) require P(4, 9)
Use memoization . . .
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
13 / 33

---

## Page 37

Computing P(i, j)
Naive recursion recomputes same
subproblem repeatedly
P(5, 10) requires P(4, 10), P(5, 9)
Both P(4, 10), P(5, 9) require P(4, 9)
Use memoization . . .
. . . or find a suitable order to compute
the subproblems
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
13 / 33

---

## Page 38

Dynamic programming
Identify subproblem structure
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
14 / 33

---

## Page 39

Dynamic programming
Identify subproblem structure
P(0, 0) has no dependencies
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
14 / 33

---

## Page 40

Dynamic programming
Identify subproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
15 / 33

---

## Page 41

Dynamic programming
Identify subproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
15 / 33

---

## Page 42

Dynamic programming
Identify subproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
15 / 33

---

## Page 43

Dynamic programming
Identify subproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
15 / 33

---

## Page 44

Dynamic programming
Identify subproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
15 / 33

---

## Page 45

Dynamic programming
Identify subproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
15 / 33

---

## Page 46

Dynamic programming
Identify subproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
15 / 33

---

## Page 47

Dynamic programming
Identify subproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
(0, 0)
(5, 10)

526 1358
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
15 / 33

---

## Page 48

Dynamic programming
Identify suproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
Fill column by column
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
16 / 33

---

## Page 49

Dynamic programming
Identify suproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
Fill column by column
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
16 / 33

---

## Page 50

Dynamic programming
Identify suproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
Fill column by column
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
16 / 33

---

## Page 51

Dynamic programming
Identify suproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
Fill column by column
(0, 0)
(5, 10)

526 1358
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
16 / 33

---

## Page 52

Dynamic programming
Identify subproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
Fill column by column
Fill diagonal by diagonal
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
17 / 33

---

## Page 53

Dynamic programming
Identify subproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
Fill column by column
Fill diagonal by diagonal
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
17 / 33

---

## Page 54

Dynamic programming
Identify subproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
Fill column by column
Fill diagonal by diagonal
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
17 / 33

---

## Page 55

Dynamic programming
Identify subproblem structure
P(0, 0) has no dependencies
Start at (0, 0)
Fill row by row
Fill column by column
Fill diagonal by diagonal
(0, 0)
(5, 10)

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
17 / 33r

---

## Page 56

Memoization vs dynamic programming
Barrier of holes just inside the border
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
18 / 33
#

---

## Page 57

Memoization vs dynamic programming
Barrier of holes just inside the border
Memoization never explores the shaded
region
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
18 / 33
D

---

## Page 58

Memoization vs dynamic programming
Barrier of holes just inside the border
Memoization never explores the shaded
region
Memo table has O(m + n) entries
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
18 / 33

---

## Page 59

Memoization vs dynamic programming
Barrier of holes just inside the border
Memoization never explores the shaded
region
Memo table has O(m + n) entries
Dynamic programming blindly fills all
mn cells of the table
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
18 / 33

---

## Page 60

Memoization vs dynamic programming
Barrier of holes just inside the border
Memoization never explores the shaded
region
Memo table has O(m + n) entries
Dynamic programming blindly fills all
mn cells of the table
Tradeo! between recursion and
iteration
"Wasteful" dynamic programming still
better in general
(0, 0)
(5, 10)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
18 / 33

---

## Page 61

Longest common subword
Given two strings, find the (length of the) longest common subword
"secret", "secretary" — "secret", length 6
"bisect", "trisect" — "isect", length 5
"bisect", "secret" — "sec", length 3
"director", "secretary" — "ec", "re", length 2
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
19 / 33
-
=--
-w
ect

---

## Page 62

Longest common subword
Given two strings, find the (length of the) longest common subword
"secret", "secretary" — "secret", length 6
"bisect", "trisect" — "isect", length 5
"bisect", "secret" — "sec", length 3
"director", "secretary" — "ec", "re", length 2
Formally
u = a0a1 . . . am→1
v = b0b1 . . . bn→1
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
19 / 33

---

## Page 63

Longest common subword
Given two strings, find the (length of the) longest common subword
"secret", "secretary" — "secret", length 6
"bisect", "trisect" — "isect", length 5
"bisect", "secret" — "sec", length 3
"director", "secretary" — "ec", "re", length 2
Formally
u = a0a1 . . . am→1
v = b0b1 . . . bn→1
Common subword of length k — for some positions i and j,
aiai+1ai+k→1 = bjbj+1bj+k→1
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
19 / 33

---

## Page 64

Longest common subword
Given two strings, find the (length of the) longest common subword
"secret", "secretary" — "secret", length 6
"bisect", "trisect" — "isect", length 5
"bisect", "secret" — "sec", length 3
"director", "secretary" — "ec", "re", length 2
Formally
u = a0a1 . . . am→1
v = b0b1 . . . bn→1
Common subword of length k — for some positions i and j,
aiai+1ai+k→1 = bjbj+1bj+k→1
Find the largest such k — length of the longest common subword
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
19 / 33

---

## Page 65

Brute force
u = a0a1 . . . am→1
v = b0b1 . . . bn→1
Find the largest k such that for some positions i and j,
aiai+1ai+k→1 = bjbj+1bj+k→1
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
20 / 33

---

## Page 66

Brute force
u = a0a1 . . . am→1
v = b0b1 . . . bn→1
Find the largest k such that for some positions i and j,
aiai+1ai+k→1 = bjbj+1bj+k→1
Try every pair of starting positions i in u, j in v
Match (ai, bj), (ai+1, bj+1), . . . as far as possible
Keep track of longest match
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
20 / 33

---

## Page 67

Brute force
u = a0a1 . . . am→1
v = b0b1 . . . bn→1
Find the largest k such that for some positions i and j,
aiai+1ai+k→1 = bjbj+1bj+k→1
Try every pair of starting positions i in u, j in v
Match (ai, bj), (ai+1, bj+1), . . . as far as possible
Keep track of longest match
Assuming m > n, this is O(mn2)
mn pairs of starting positions
From each starting position, scan could be O(n)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
20 / 33
an--aba
na---aba
win
stardy pos
13 If
men

---

## Page 68

Inductive structure
u = a0a1 . . . am→1
v = b0b1 . . . bn→1
Find the largest k such that for some positions i and j,
aiai+1ai+k→1 = bjbj+1bj+k→1
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
21 / 33

---

## Page 69

Inductive structure
u = a0a1 . . . am→1
v = b0b1 . . . bn→1
Find the largest k such that for some positions i and j,
aiai+1ai+k→1 = bjbj+1bj+k→1
LCW (i, j) — length of longest common subword in aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai ↓= bj, LCW (i, j) = 0
If ai = bj, LCW (i, j) = 1 + LCW (i+1, j+1)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
21 / 33

---

## Page 70

Inductive structure
u = a0a1 . . . am→1
v = b0b1 . . . bn→1
Find the largest k such that for some positions i and j,
aiai+1ai+k→1 = bjbj+1bj+k→1
LCW (i, j) — length of longest common subword in aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai ↓= bj, LCW (i, j) = 0
If ai = bj, LCW (i, j) = 1 + LCW (i+1, j+1)
Base case: LCW (m, n) = 0
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
21 / 33

---

## Page 71

Inductive structure
u = a0a1 . . . am→1
v = b0b1 . . . bn→1
Find the largest k such that for some positions i and j,
aiai+1ai+k→1 = bjbj+1bj+k→1
LCW (i, j) — length of longest common subword in aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai ↓= bj, LCW (i, j) = 0
If ai = bj, LCW (i, j) = 1 + LCW (i+1, j+1)
Base case: LCW (m, n) = 0
In general, LCW (i, n) = 0 for all 0 ↔i ↔m
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
21 / 33

---

## Page 72

Inductive structure
u = a0a1 . . . am→1
v = b0b1 . . . bn→1
Find the largest k such that for some positions i and j,
aiai+1ai+k→1 = bjbj+1bj+k→1
LCW (i, j) — length of longest common subword in aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai ↓= bj, LCW (i, j) = 0
If ai = bj, LCW (i, j) = 1 + LCW (i+1, j+1)
Base case: LCW (m, n) = 0
In general, LCW (i, n) = 0 for all 0 ↔i ↔m
In general, LCW (m, j) = 0 for all 0 ↔j ↔n
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
21 / 33
-
(ii)
↑
(L+1,j+1)

---

## Page 73

Subproblem dependency
Subproblems are LCW (i, j), for
0 ↔i ↔m, 0 ↔j ↔n
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
22 / 33

---

## Page 74

Subproblem dependency
Subproblems are LCW (i, j), for
0 ↔i ↔m, 0 ↔j ↔n
Table of (m + 1) · (n + 1) values

s
e
c
r
e
t
•

b
i
s
e
c
t
•
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
22 / 33
#

---

## Page 75

Subproblem dependency
Subproblems are LCW (i, j), for
0 ↔i ↔m, 0 ↔j ↔n
Table of (m + 1) · (n + 1) values
LCW (i, j) depends on LCW (i+1, j+1)

s
e
c
r
e
t
•

b
i
s
e
c
t
•
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
22 / 33
?
-
↑
·
To

---

## Page 76

Subproblem dependency
Subproblems are LCW (i, j), for
0 ↔i ↔m, 0 ↔j ↔n
Table of (m + 1) · (n + 1) values
LCW (i, j) depends on LCW (i+1, j+1)
Start at bottom right and fill row by
row or column by column

s
e
c
r
e
t
•

b
i
s
e
c
t
•

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
22 / 33
I
&
Y
LCw(m, n) = 0
↳
-
in
-
=
-

---

## Page 77

Subproblem dependency
Subproblems are LCW (i, j), for
0 ↔i ↔m, 0 ↔j ↔n
Table of (m + 1) · (n + 1) values
LCW (i, j) depends on LCW (i+1, j+1)
Start at bottom right and fill row by
row or column by column

s
e
c
r
e
t
•

b
i
s
e
c
t
•

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
22 / 33
O
I
O

---

## Page 78

Subproblem dependency
Subproblems are LCW (i, j), for
0 ↔i ↔m, 0 ↔j ↔n
Table of (m + 1) · (n + 1) values
LCW (i, j) depends on LCW (i+1, j+1)
Start at bottom right and fill row by
row or column by column

s
e
c
r
e
t
•

b
i
s
e
c
t
•

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
22 / 33
O
o
-
&

---

## Page 79

Subproblem dependency
Subproblems are LCW (i, j), for
0 ↔i ↔m, 0 ↔j ↔n
Table of (m + 1) · (n + 1) values
LCW (i, j) depends on LCW (i+1, j+1)
Start at bottom right and fill row by
row or column by column

s
e
c
r
e
t
•

b
i
s
e
c
t
•

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
22 / 33
nor
= O
=

---

## Page 80

Subproblem dependency
Subproblems are LCW (i, j), for
0 ↔i ↔m, 0 ↔j ↔n
Table of (m + 1) · (n + 1) values
LCW (i, j) depends on LCW (i+1, j+1)
Start at bottom right and fill row by
row or column by column

s
e
c
r
e
t
•

b
i
s
e
c
t
•

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
22 / 33

0-!
O

---

## Page 81

Subproblem dependency
Subproblems are LCW (i, j), for
0 ↔i ↔m, 0 ↔j ↔n
Table of (m + 1) · (n + 1) values
LCW (i, j) depends on LCW (i+1, j+1)
Start at bottom right and fill row by
row or column by column

s
e
c
r
e
t
•

b
i
s
e
c
t
•

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
22 / 33
·I

---

## Page 82

Subproblem dependency
Subproblems are LCW (i, j), for
0 ↔i ↔m, 0 ↔j ↔n
Table of (m + 1) · (n + 1) values
LCW (i, j) depends on LCW (i+1, j+1)
Start at bottom right and fill row by
row or column by column

s
e
c
r
e
t
•

b
i
s
e
c
t
•

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
22 / 33
O

---

## Page 83

Subproblem dependency
Subproblems are LCW (i, j), for
0 ↔i ↔m, 0 ↔j ↔n
Table of (m + 1) · (n + 1) values
LCW (i, j) depends on LCW (i+1, j+1)
Start at bottom right and fill row by
row or column by column
Reading o! the solution
Find entry (i, j) with largest LCW value

s
e
c
r
e
t
•

b
i
s
e
c
t
•

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
22 / 33

8) i

---

## Page 84

Subproblem dependency
Subproblems are LCW (i, j), for
0 ↔i ↔m, 0 ↔j ↔n
Table of (m + 1) · (n + 1) values
LCW (i, j) depends on LCW (i+1, j+1)
Start at bottom right and fill row by
row or column by column
Reading o! the solution
Find entry (i, j) with largest LCW value
Read o! the actual subword diagonally

s
e
c
r
e
t
•

b
i
s
e
c
t
•

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
22 / 33

---

## Page 85

Subproblem dependency
Subproblems are LCW (i, j), for
0 ↔i ↔m, 0 ↔j ↔n
Table of (m + 1) · (n + 1) values
LCW (i, j) depends on LCW (i+1, j+1)
Start at bottom right and fill row by
row or column by column
Reading o! the solution
Find entry (i, j) with largest LCW value
Read o! the actual subword diagonally

s
e
c
r
e
t
•

b
i
s
e
c
t
•

Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
22 / 33
->

---

## Page 86

Implementation
def LCW(u,v):
import numpy as np
(m,n) = (len(u),len(v))
lcw = np.zeros((m+1,n+1))
maxlcw = 0
for j in range(n-1,-1,-1):
for i in range(m-1,-1,-1):
if u[i] == v[j]:
lcw[i,j] = 1 + lcw[i+1,j+1]
else:
lcw[i,j] = 0
if lcw[i,j] > maxlcw:
maxlcw = lcw[i,j]
return(maxlcw)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
23 / 33

---

## Page 87

Implementation
def LCW(u,v):
import numpy as np
(m,n) = (len(u),len(v))
lcw = np.zeros((m+1,n+1))
maxlcw = 0
for j in range(n-1,-1,-1):
for i in range(m-1,-1,-1):
if u[i] == v[j]:
lcw[i,j] = 1 + lcw[i+1,j+1]
else:
lcw[i,j] = 0
if lcw[i,j] > maxlcw:
maxlcw = lcw[i,j]
return(maxlcw)
Complexity
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
23 / 33

---

## Page 88

Implementation
def LCW(u,v):
import numpy as np
(m,n) = (len(u),len(v))
lcw = np.zeros((m+1,n+1))
maxlcw = 0
for j in range(n-1,-1,-1):
for i in range(m-1,-1,-1):
if u[i] == v[j]:
lcw[i,j] = 1 + lcw[i+1,j+1]
else:
lcw[i,j] = 0
if lcw[i,j] > maxlcw:
maxlcw = lcw[i,j]
return(maxlcw)
Complexity
Recall that brute force was
O(mn2)
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
23 / 33

---

## Page 89

Implementation
def LCW(u,v):
import numpy as np
(m,n) = (len(u),len(v))
lcw = np.zeros((m+1,n+1))
maxlcw = 0
for j in range(n-1,-1,-1):
for i in range(m-1,-1,-1):
if u[i] == v[j]:
lcw[i,j] = 1 + lcw[i+1,j+1]
else:
lcw[i,j] = 0
if lcw[i,j] > maxlcw:
maxlcw = lcw[i,j]
return(maxlcw)
Complexity
Recall that brute force was
O(mn2)
Inductive solution is O(mn),
using dynamic programming or
memoization
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
23 / 33

---

## Page 90

Implementation
def LCW(u,v):
import numpy as np
(m,n) = (len(u),len(v))
lcw = np.zeros((m+1,n+1))
maxlcw = 0
for j in range(n-1,-1,-1):
for i in range(m-1,-1,-1):
if u[i] == v[j]:
lcw[i,j] = 1 + lcw[i+1,j+1]
else:
lcw[i,j] = 0
if lcw[i,j] > maxlcw:
maxlcw = lcw[i,j]
return(maxlcw)
Complexity
Recall that brute force was
O(mn2)
Inductive solution is O(mn),
using dynamic programming or
memoization
Fill a table of size O(mn)
Each table entry takes
constant time to compute
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
23 / 33
↑Flip
NOT
NEEDED

---

## Page 91

Longest common subsequence
Subsequence — can drop some letters in
between
Given two strings, find the (length of the)
longest common subsequence
"secret", "secretary" —
"secret", length 6
"bisect", "trisect" —
"isect", length 5
"bisect", "secret" —
"sect", length 4
"director", "secretary" —
"ectr", "retr", length 4
Madhavan Mukund
Lecture 25, 18 November 2025
PDSP Lecture 25
24 / 33