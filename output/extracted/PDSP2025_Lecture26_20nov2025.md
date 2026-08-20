## Page 1

Lecture 26, 20 November 2025
Madhavan Mukund
https://www.cmi.ac.in/~madhavan
Programming and Data Structures with Python
Lecture 26, 20 Nov 2025

---

## Page 2

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
Lecture 26, 20 November 2025
PDSP Lecture 26
2 / 18
-
-
-

---

## Page 3

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
Lecture 26, 20 November 2025
PDSP Lecture 26
3 / 18
- -
--
0. 0-
------

---

## Page 4

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
LCS is the longest path connecting
non-zero LCW entries, moving right/down

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
Lecture 26, 20 November 2025
PDSP Lecture 26
3 / 18

On
X
O
Al

---

## Page 5

Applications
Analyzing genes
DNA is a long string over A, T, G, C
Two species are similar if their DNA has
long common subsequences
diff command in Unix/Linux
Compares text files
Find the longest matching subsequence
of lines
Each line of text is a "character"

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
Lecture 26, 20 November 2025
PDSP Lecture 26
4 / 18

---

## Page 6

Inductive structure
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
LCS(i, j) — length of longest common subsequence in
aiai+1 . . . am→1, bjbj+1 . . . bn→1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
5 / 18
it
je

---

## Page 7

Inductive structure
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
LCS(i, j) — length of longest common subsequence in
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj
Can assume (ai, bj) is part of LCS
LCS(i, j) = 1 + LCS(i+1, j+1)
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
5 / 18
D
#

---

## Page 8

Inductive structure
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
LCS(i, j) — length of longest common subsequence in
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj
Can assume (ai, bj) is part of LCS
LCS(i, j) = 1 + LCS(i+1, j+1)
If ai →= bj, ai and bj cannot both belong to LCS
Which one should we drop?
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
5 / 18
Dad
a

---

## Page 9

Inductive structure
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
LCS(i, j) — length of longest common subsequence in
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj
Can assume (ai, bj) is part of LCS
LCS(i, j) = 1 + LCS(i+1, j+1)
If ai →= bj, ai and bj cannot both belong to LCS
Which one should we drop?
LCS(i, j) = max(LCS(i, j+1), LCS(i+1, j)
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
5 / 18
·

---

## Page 10

Inductive structure
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
LCS(i, j) — length of longest common subsequence in
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj
Can assume (ai, bj) is part of LCS
LCS(i, j) = 1 + LCS(i+1, j+1)
If ai →= bj, ai and bj cannot both belong to LCS
Which one should we drop?
LCS(i, j) = max(LCS(i, j+1), LCS(i+1, j)
Base cases as with LCW
LCS(i, n) = 0 for all 0 ↑i ↑m
LCS(m, j) = 0 for all 0 ↑j ↑n
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
5 / 18
a
A
C

---

## Page 11

Subproblem dependency
Subproblems are LCS(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
6 / 18

---

## Page 12

Subproblem dependency
Subproblems are LCS(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
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
Lecture 26, 20 November 2025
PDSP Lecture 26
6 / 18

---

## Page 13

Subproblem dependency
Subproblems are LCS(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
LCS(i, j) depends on LCS(i+1, j+1),
LCS(i, j+1),LCS(i+1, j),

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
Lecture 26, 20 November 2025
PDSP Lecture 26
6 / 18

---

## Page 14

Subproblem dependency
Subproblems are LCS(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
LCS(i, j) depends on LCS(i+1, j+1),
LCS(i, j+1),LCS(i+1, j),
No dependency for LCS(m, n) — start
at bottom right and fill by row, column
or diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
6 / 18

---

## Page 15

Subproblem dependency
Subproblems are LCS(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
LCS(i, j) depends on LCS(i+1, j+1),
LCS(i, j+1),LCS(i+1, j),
No dependency for LCS(m, n) — start
at bottom right and fill by row, column
or diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
6 / 18
D
my2

---

## Page 16

Subproblem dependency
Subproblems are LCS(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
LCS(i, j) depends on LCS(i+1, j+1),
LCS(i, j+1),LCS(i+1, j),
No dependency for LCS(m, n) — start
at bottom right and fill by row, column
or diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
6 / 18
⑳
G
O

---

## Page 17

Subproblem dependency
Subproblems are LCS(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
LCS(i, j) depends on LCS(i+1, j+1),
LCS(i, j+1),LCS(i+1, j),
No dependency for LCS(m, n) — start
at bottom right and fill by row, column
or diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
6 / 18

---

## Page 18

Subproblem dependency
Subproblems are LCS(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
LCS(i, j) depends on LCS(i+1, j+1),
LCS(i, j+1),LCS(i+1, j),
No dependency for LCS(m, n) — start
at bottom right and fill by row, column
or diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
6 / 18

---

## Page 19

Subproblem dependency
Subproblems are LCS(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
LCS(i, j) depends on LCS(i+1, j+1),
LCS(i, j+1),LCS(i+1, j),
No dependency for LCS(m, n) — start
at bottom right and fill by row, column
or diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
6 / 18

---

## Page 20

Subproblem dependency
Subproblems are LCS(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
LCS(i, j) depends on LCS(i+1, j+1),
LCS(i, j+1),LCS(i+1, j),
No dependency for LCS(m, n) — start
at bottom right and fill by row, column
or diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
6 / 18
O

---

## Page 21

Subproblem dependency
Subproblems are LCS(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
LCS(i, j) depends on LCS(i+1, j+1),
LCS(i, j+1),LCS(i+1, j),
No dependency for LCS(m, n) — start
at bottom right and fill by row, column
or diagonal
Reading o! the solution
Trace back the path by which each
entry was filled

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
Lecture 26, 20 November 2025
PDSP Lecture 26
6 / 18

---

## Page 22

Subproblem dependency
Subproblems are LCS(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
LCS(i, j) depends on LCS(i+1, j+1),
LCS(i, j+1),LCS(i+1, j),
No dependency for LCS(m, n) — start
at bottom right and fill by row, column
or diagonal
Reading o! the solution
Trace back the path by which each
entry was filled
Each diagonal step is an element of LCS

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
Lecture 26, 20 November 2025
PDSP Lecture 26
6 / 18

---

## Page 23

Implementation
def LCS(u,v):
import numpy as np
(m,n) = (len(u),len(v))
lcs = np.zeros((m+1,n+1))
for j in range(n-1,-1,-1):
for i in range(m-1,-1,-1):
if u[i] == v[j]:
lcs[i,j] = 1 + lcs[i+1,j+1]
else:
lcs[i,j] = max(lcs[i+1,j],
lcs[i,j+1])
return(lcs[0,0])
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
7 / 18

---

## Page 24

Implementation
def LCS(u,v):
import numpy as np
(m,n) = (len(u),len(v))
lcs = np.zeros((m+1,n+1))
for j in range(n-1,-1,-1):
for i in range(m-1,-1,-1):
if u[i] == v[j]:
lcs[i,j] = 1 + lcs[i+1,j+1]
else:
lcs[i,j] = max(lcs[i+1,j],
lcs[i,j+1])
return(lcs[0,0])
Complexity
Again O(mn), using dynamic
programming or memoization
Fill a table of size O(mn)
Each table entry takes
constant time to compute
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
7 / 18
C

---

## Page 25

Document similarity
"The students were able to appreciate the
concept optimal substructure property and
its use in designing algorithms"
"The lecture taught the students to
appreciate how the concept of optimal
substructures can be used in designing
algorithms"
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
8 / 18

---

## Page 26

Document similarity
"The students were able to appreciate the
concept optimal substructure property and
its use in designing algorithms"
"The lecture taught the students to
appreciate how the concept of optimal
substructures can be used in designing
algorithms"
Edit operations to transform documents
Insert a character
Delete a character
Substitute one character by another
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
8 / 18
-
-
- Delete
I
Insert
Delete
Insert

---

## Page 27

Document similarity
"The students were able to appreciate the
concept optimal substructure property and
its use in designing algorithms"
"The lecture taught the students to
appreciate how the concept of optimal
substructures can be used in designing
algorithms"
Edit operations to transform documents
Insert a character
Delete a character
Substitute one character by another
"The lecture taught the students
were able to appreciate how the
concept of optimal substructures
property cand itbse used in designing
algorithms"
insert, delete, substitute
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
8 / 18

---

## Page 28

Document similarity
"The students were able to appreciate the
concept optimal substructure property and
its use in designing algorithms"
"The lecture taught the students to
appreciate how the concept of optimal
substructures can be used in designing
algorithms"
Edit operations to transform documents
Insert a character
Delete a character
Substitute one character by another
"The lecture taught the students
were able to appreciate how the
concept of optimal substructures
property cand itbse used in designing
algorithms"
insert, delete, substitute
Edit distance
Minimum number of edit operations
needed
In our example, 24 characters
inserted, 18 deleted, 2 substituted
Edit distance is at most 44
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
8 / 18

---

## Page 29

Edit distance
Minimum number of editing operations
needed to transform one document to
the other
Insert a character
Delete a character
Substitute one character by another
Also called Levenshtein distance
Vladimir Levenshtein, 1965
Applications
Suggestions for spelling correction
Genetic similarity of species
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
9 / 18

---

## Page 30

Edit distance
Minimum number of editing operations
needed to transform one document to
the other
Insert a character
Delete a character
Substitute one character by another
Also called Levenshtein distance
Vladimir Levenshtein, 1965
Applications
Suggestions for spelling correction
Genetic similarity of species
Edit distance and LCS
Longest common subsequence of u, v
Minimum number of deletes needed to
make them equal
Deleting a letter from u is equivalent to
inserting it in v
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
9 / 18

---

## Page 31

Edit distance
Minimum number of editing operations
needed to transform one document to
the other
Insert a character
Delete a character
Substitute one character by another
Also called Levenshtein distance
Vladimir Levenshtein, 1965
Applications
Suggestions for spelling correction
Genetic similarity of species
Edit distance and LCS
Longest common subsequence of u, v
Minimum number of deletes needed to
make them equal
Deleting a letter from u is equivalent to
inserting it in v
bisect, secret — LCS is sect
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
9 / 18

---

## Page 32

Edit distance
Minimum number of editing operations
needed to transform one document to
the other
Insert a character
Delete a character
Substitute one character by another
Also called Levenshtein distance
Vladimir Levenshtein, 1965
Applications
Suggestions for spelling correction
Genetic similarity of species
Edit distance and LCS
Longest common subsequence of u, v
Minimum number of deletes needed to
make them equal
Deleting a letter from u is equivalent to
inserting it in v
bisect, secret — LCS is sect
Delete b, i in bisect and r, e in
secret
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
9 / 18
- -

---

## Page 33

Edit distance
Minimum number of editing operations
needed to transform one document to
the other
Insert a character
Delete a character
Substitute one character by another
Also called Levenshtein distance
Vladimir Levenshtein, 1965
Applications
Suggestions for spelling correction
Genetic similarity of species
Edit distance and LCS
Longest common subsequence of u, v
Minimum number of deletes needed to
make them equal
Deleting a letter from u is equivalent to
inserting it in v
bisect, secret — LCS is sect
Delete b, i in bisect and r, e in
secret
Delete b, i and then insert r, e in
bisect
From LCS, we can compute edit
distance without substitution
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
9 / 18
-re

---

## Page 34

Inductive structure for edit distance
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
10 / 18

---

## Page 35

Inductive structure for edit distance
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
Recall LCS
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
10 / 18

---

## Page 36

Inductive structure for edit distance
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
Recall LCS
LCS(i, j) — length of longest
common subsequence in
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj,
LCS(i, j) = 1 + LCS(i+1, j+1)
If ai →= bj,
LCS(i, j) = max[ LCS(i, j+1),
LCS(i+1, j) ]
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
10 / 18

---

## Page 37

Inductive structure for edit distance
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
Recall LCS
LCS(i, j) — length of longest
common subsequence in
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj,
LCS(i, j) = 1 + LCS(i+1, j+1)
If ai →= bj,
LCS(i, j) = max[ LCS(i, j+1),
LCS(i+1, j) ]
Edit distance — aim is to transform u to v
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
10 / 18
ana

---

## Page 38

Inductive structure for edit distance
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
Recall LCS
LCS(i, j) — length of longest
common subsequence in
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj,
LCS(i, j) = 1 + LCS(i+1, j+1)
If ai →= bj,
LCS(i, j) = max[ LCS(i, j+1),
LCS(i+1, j) ]
Edit distance — aim is to transform u to v
If ai = bj, nothing to be done
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
10 / 18

---

## Page 39

Inductive structure for edit distance
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
Recall LCS
LCS(i, j) — length of longest
common subsequence in
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj,
LCS(i, j) = 1 + LCS(i+1, j+1)
If ai →= bj,
LCS(i, j) = max[ LCS(i, j+1),
LCS(i+1, j) ]
Edit distance — aim is to transform u to v
If ai = bj, nothing to be done
If ai →= bj, best among
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
10 / 18

---

## Page 40

Inductive structure for edit distance
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
Recall LCS
LCS(i, j) — length of longest
common subsequence in
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj,
LCS(i, j) = 1 + LCS(i+1, j+1)
If ai →= bj,
LCS(i, j) = max[ LCS(i, j+1),
LCS(i+1, j) ]
Edit distance — aim is to transform u to v
If ai = bj, nothing to be done
If ai →= bj, best among
Substitute ai by bj
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
10 / 18

---

## Page 41

Inductive structure for edit distance
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
Recall LCS
LCS(i, j) — length of longest
common subsequence in
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj,
LCS(i, j) = 1 + LCS(i+1, j+1)
If ai →= bj,
LCS(i, j) = max[ LCS(i, j+1),
LCS(i+1, j) ]
Edit distance — aim is to transform u to v
If ai = bj, nothing to be done
If ai →= bj, best among
Substitute ai by bj
Delete ai
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
10 / 18

---

## Page 42

Inductive structure for edit distance
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
Recall LCS
LCS(i, j) — length of longest
common subsequence in
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj,
LCS(i, j) = 1 + LCS(i+1, j+1)
If ai →= bj,
LCS(i, j) = max[ LCS(i, j+1),
LCS(i+1, j) ]
Edit distance — aim is to transform u to v
If ai = bj, nothing to be done
If ai →= bj, best among
Substitute ai by bj
Delete ai
Insert bj before ai
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
10 / 18
Jall
changeu

---

## Page 43

Inductive structure for edit distance
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
ED(i, j) — edit distance for
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj, nothing to be done
If ai →= bj, best among
Substitute ai by bj
Delete ai
Insert bj before ai
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
11 / 18

---

## Page 44

Inductive structure for edit distance
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
ED(i, j) — edit distance for
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj, nothing to be done
If ai →= bj, best among
Substitute ai by bj
Delete ai
Insert bj before ai
If ai = bj,
ED(i, j) = ED(i+1, j+1)
If ai →= bj,
ED(i, j) = 1 + min[ ED(i+1, j+1),
ED(i+1, j),
ED(i, j+1) ]
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
11 / 18
O
subst
dah
Insert

---

## Page 45

Inductive structure for edit distance
u = a0a1 . . . am→1, v = b0b1 . . . bn→1
ED(i, j) — edit distance for
aiai+1 . . . am→1, bjbj+1 . . . bn→1
If ai = bj, nothing to be done
If ai →= bj, best among
Substitute ai by bj
Delete ai
Insert bj before ai
If ai = bj,
ED(i, j) = ED(i+1, j+1)
If ai →= bj,
ED(i, j) = 1 + min[ ED(i+1, j+1),
ED(i+1, j),
ED(i, j+1) ]
Base cases
ED(m, n) = 0
ED(i, n) = m ↓i for all 0 ↑i ↑m
Delete aiai+1 . . . am→1 from u
ED(m, j) = n ↓j for all 0 ↑j ↑n
Insert bjbj+1 . . . bn→1 into u
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
11 / 18
min
O
i
-
-
90Attract--
Ama
-
O

---

## Page 46

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 47

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 48

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
Like LCS, ED(i, j) depends on
ED(i+1, j+1), ED(i, j+1), ED(i+1, j)

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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 49

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
Like LCS, ED(i, j) depends on
ED(i+1, j+1), ED(i, j+1), ED(i+1, j)
No dependency for ED(m, n) — start at
bottom right and fill by row, column or
diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 50

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
Like LCS, ED(i, j) depends on
ED(i+1, j+1), ED(i, j+1), ED(i+1, j)
No dependency for ED(m, n) — start at
bottom right and fill by row, column or
diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 51

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
Like LCS, ED(i, j) depends on
ED(i+1, j+1), ED(i, j+1), ED(i+1, j)
No dependency for ED(m, n) — start at
bottom right and fill by row, column or
diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 52

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
Like LCS, ED(i, j) depends on
ED(i+1, j+1), ED(i, j+1), ED(i+1, j)
No dependency for ED(m, n) — start at
bottom right and fill by row, column or
diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 53

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
Like LCS, ED(i, j) depends on
ED(i+1, j+1), ED(i, j+1), ED(i+1, j)
No dependency for ED(m, n) — start at
bottom right and fill by row, column or
diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 54

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
Like LCS, ED(i, j) depends on
ED(i+1, j+1), ED(i, j+1), ED(i+1, j)
No dependency for ED(m, n) — start at
bottom right and fill by row, column or
diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 55

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
Like LCS, ED(i, j) depends on
ED(i+1, j+1), ED(i, j+1), ED(i+1, j)
No dependency for ED(m, n) — start at
bottom right and fill by row, column or
diagonal

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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 56

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
Like LCS, ED(i, j) depends on
ED(i+1, j+1), ED(i, j+1), ED(i+1, j)
No dependency for ED(m, n) — start at
bottom right and fill by row, column or
diagonal
Reading o! the solution
Transform bisect to secret

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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 57

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
Like LCS, ED(i, j) depends on
ED(i+1, j+1), ED(i, j+1), ED(i+1, j)
No dependency for ED(m, n) — start at
bottom right and fill by row, column or
diagonal
Reading o! the solution
Transform bisect to secret
Delete b

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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 58

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
Like LCS, ED(i, j) depends on
ED(i+1, j+1), ED(i, j+1), ED(i+1, j)
No dependency for ED(m, n) — start at
bottom right and fill by row, column or
diagonal
Reading o! the solution
Transform bisect to secret
Delete b , Delete i

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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 59

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
Like LCS, ED(i, j) depends on
ED(i+1, j+1), ED(i, j+1), ED(i+1, j)
No dependency for ED(m, n) — start at
bottom right and fill by row, column or
diagonal
Reading o! the solution
Transform bisect to secret
Delete b , Delete i , Insert r

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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 60

Subproblem dependency
Subproblems are ED(i, j), for
0 ↑i ↑m, 0 ↑j ↑n
Table of (m + 1) · (n + 1) values
Like LCS, ED(i, j) depends on
ED(i+1, j+1), ED(i, j+1), ED(i+1, j)
No dependency for ED(m, n) — start at
bottom right and fill by row, column or
diagonal
Reading o! the solution
Transform bisect to secret
Delete b , Delete i , Insert r , Insert e

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
Lecture 26, 20 November 2025
PDSP Lecture 26
12 / 18

---

## Page 61

Implementation
def ED(u,v):
import numpy as np
(m,n) = (len(u),len(v))
ed = np.zeros((m+1,n+1))
for i in range(m-1,-1,-1):
ed[i,n] = m-i
for j in range(n-1,-1,-1):
ed[m,j] = n-j
for j in range(n-1,-1,-1):
for i in range(m-1,-1,-1):
if u[i] == v[j]:
ed[i,j] = ed[i+1,j+1]
else:
ed[i,j] = 1 + min(ed[i+1,j+1],
ed[i,j+1],
ed[i+1,j])
return(ed[0,0])
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
13 / 18
C

---

## Page 62

Implementation
def ED(u,v):
import numpy as np
(m,n) = (len(u),len(v))
ed = np.zeros((m+1,n+1))
for i in range(m-1,-1,-1):
ed[i,n] = m-i
for j in range(n-1,-1,-1):
ed[m,j] = n-j
for j in range(n-1,-1,-1):
for i in range(m-1,-1,-1):
if u[i] == v[j]:
ed[i,j] = ed[i+1,j+1]
else:
ed[i,j] = 1 + min(ed[i+1,j+1],
ed[i,j+1],
ed[i+1,j])
return(ed[0,0])
Complexity
Again O(mn), using dynamic
programming or memoization
Fill a table of size O(mn)
Each table entry takes
constant time to compute
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
13 / 18

---

## Page 63

Multiplying matrices
Multiply matrices A, B
AB[i, j] =
n→1
!
k=0
A[i, k]B[k, j]
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
14 / 18
(r- n(z)nr)
·[ ]
recentriese
compute

---

## Page 64

Multiplying matrices
Multiply matrices A, B
AB[i, j] =
n→1
!
k=0
A[i, k]B[k, j]
Dimensions must be compatible
A : m ↔n, B : n ↔p
AB : m ↔p
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
14 / 18

---

## Page 65

Multiplying matrices
Multiply matrices A, B
AB[i, j] =
n→1
!
k=0
A[i, k]B[k, j]
Dimensions must be compatible
A : m ↔n, B : n ↔p
AB : m ↔p
Computing each entry in AB is O(n)
Overall, computing AB is O(mnp)
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
14 / 18

---

## Page 66

Multiplying matrices
Multiply matrices A, B
AB[i, j] =
n→1
!
k=0
A[i, k]B[k, j]
Dimensions must be compatible
A : m ↔n, B : n ↔p
AB : m ↔p
Computing each entry in AB is O(n)
Overall, computing AB is O(mnp)
Matrix multiplication is associative
ABC = (AB)C = A(BC)
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
14 / 18

---

## Page 67

Multiplying matrices
Multiply matrices A, B
AB[i, j] =
n→1
!
k=0
A[i, k]B[k, j]
Dimensions must be compatible
A : m ↔n, B : n ↔p
AB : m ↔p
Computing each entry in AB is O(n)
Overall, computing AB is O(mnp)
Matrix multiplication is associative
ABC = (AB)C = A(BC)
Bracketing does not change answer
. . . but can a!ect the complexity!
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
14 / 18

---

## Page 68

Multiplying matrices
Multiply matrices A, B
AB[i, j] =
n→1
!
k=0
A[i, k]B[k, j]
Dimensions must be compatible
A : m ↔n, B : n ↔p
AB : m ↔p
Computing each entry in AB is O(n)
Overall, computing AB is O(mnp)
Matrix multiplication is associative
ABC = (AB)C = A(BC)
Bracketing does not change answer
. . . but can a!ect the complexity!
Let A : 1 ↔100, B : 100 ↔1, C : 1 ↔100
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
14 / 18

---

## Page 69

Multiplying matrices
Multiply matrices A, B
AB[i, j] =
n→1
!
k=0
A[i, k]B[k, j]
Dimensions must be compatible
A : m ↔n, B : n ↔p
AB : m ↔p
Computing each entry in AB is O(n)
Overall, computing AB is O(mnp)
Matrix multiplication is associative
ABC = (AB)C = A(BC)
Bracketing does not change answer
. . . but can a!ect the complexity!
Let A : 1 ↔100, B : 100 ↔1, C : 1 ↔100
Computing A(BC)
BC : 100 ↔100, takes
100 · 1 · 100 = 10000 steps to compute
A(BC) : 1 ↔100, takes
1 · 100 · 100 = 10000 steps to compute
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
14 / 18
--

---

## Page 70

Multiplying matrices
Multiply matrices A, B
AB[i, j] =
n→1
!
k=0
A[i, k]B[k, j]
Dimensions must be compatible
A : m ↔n, B : n ↔p
AB : m ↔p
Computing each entry in AB is O(n)
Overall, computing AB is O(mnp)
Matrix multiplication is associative
ABC = (AB)C = A(BC)
Bracketing does not change answer
. . . but can a!ect the complexity!
Let A : 1 ↔100, B : 100 ↔1, C : 1 ↔100
Computing A(BC)
BC : 100 ↔100, takes
100 · 1 · 100 = 10000 steps to compute
A(BC) : 1 ↔100, takes
1 · 100 · 100 = 10000 steps to compute
Computing (AB)C
AB : 1 ↔1, takes
1 · 100 · 1 = 100 steps to compute
(AB)C) : 1 ↔100, takes
1 · 1 · 100 = 100 steps to compute
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
14 / 18

---

## Page 71

Multiplying matrices
Multiply matrices A, B
AB[i, j] =
n→1
!
k=0
A[i, k]B[k, j]
Dimensions must be compatible
A : m ↔n, B : n ↔p
AB : m ↔p
Computing each entry in AB is O(n)
Overall, computing AB is O(mnp)
Matrix multiplication is associative
ABC = (AB)C = A(BC)
Bracketing does not change answer
. . . but can a!ect the complexity!
Let A : 1 ↔100, B : 100 ↔1, C : 1 ↔100
Computing A(BC)
BC : 100 ↔100, takes
100 · 1 · 100 = 10000 steps to compute
A(BC) : 1 ↔100, takes
1 · 100 · 100 = 10000 steps to compute
Computing (AB)C
AB : 1 ↔1, takes
1 · 100 · 1 = 100 steps to compute
(AB)C) : 1 ↔100, takes
1 · 1 · 100 = 100 steps to compute
20000 steps vs 200 steps!
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
14 / 18

---

## Page 72

Multiplying matrices
Multiply matrices A, B
AB[i, j] =
n→1
!
k=0
A[i, k]B[k, j]
Dimensions must be compatible
A : m ↔n, B : n ↔p
AB : m ↔p
Computing each entry in AB is O(n)
Overall, computing AB is O(mnp)
Matrix multiplication is associative
ABC = (AB)C = A(BC)
Bracketing does not change answer
. . . but can a!ect the complexity!
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
15 / 18

---

## Page 73

Multiplying matrices
Multiply matrices A, B
AB[i, j] =
n→1
!
k=0
A[i, k]B[k, j]
Dimensions must be compatible
A : m ↔n, B : n ↔p
AB : m ↔p
Computing each entry in AB is O(n)
Overall, computing AB is O(mnp)
Matrix multiplication is associative
ABC = (AB)C = A(BC)
Bracketing does not change answer
. . . but can a!ect the complexity!
Given n matrices M0 : r0 ↔c0,
M1 : r1 ↔c1, . . . , Mn→1 : rn→1 ↔cn→1
Dimensions match: rj = cj→1, 0 < j < n
Product M0 · M1 · · · Mn→1 can be
computed
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
15 / 18
(oM) Men MG

---

## Page 74

Multiplying matrices
Multiply matrices A, B
AB[i, j] =
n→1
!
k=0
A[i, k]B[k, j]
Dimensions must be compatible
A : m ↔n, B : n ↔p
AB : m ↔p
Computing each entry in AB is O(n)
Overall, computing AB is O(mnp)
Matrix multiplication is associative
ABC = (AB)C = A(BC)
Bracketing does not change answer
. . . but can a!ect the complexity!
Given n matrices M0 : r0 ↔c0,
M1 : r1 ↔c1, . . . , Mn→1 : rn→1 ↔cn→1
Dimensions match: rj = cj→1, 0 < j < n
Product M0 · M1 · · · Mn→1 can be
computed
Find an optimal order to compute the
product
Multiply two matrices at a time
Bracket the expression optimally
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
15 / 18

---

## Page 75

Inductive structure
Final step combines two subproducts
(M0 · M1 · · · Mk→1) · (Mk · Mk+1 · · · Mn→1)
for some 0 < k < n
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
16 / 18
moli,lone)
-- Manua
-

---

## Page 76

Inductive structure
Final step combines two subproducts
(M0 · M1 · · · Mk→1) · (Mk · Mk+1 · · · Mn→1)
for some 0 < k < n
First factor is r0 ↔ck→1, second is
rk ↔cn→1, where rk = ck→1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
16 / 18
-
roX(r1
= r
X Cn-1

---

## Page 77

Inductive structure
Final step combines two subproducts
(M0 · M1 · · · Mk→1) · (Mk · Mk+1 · · · Mn→1)
for some 0 < k < n
First factor is r0 ↔ck→1, second is
rk ↔cn→1, where rk = ck→1
Let C(0, n↓1) denote the overall cost
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
16 / 18

---

## Page 78

Inductive structure
Final step combines two subproducts
(M0 · M1 · · · Mk→1) · (Mk · Mk+1 · · · Mn→1)
for some 0 < k < n
First factor is r0 ↔ck→1, second is
rk ↔cn→1, where rk = ck→1
Let C(0, n↓1) denote the overall cost
Final multiplication is O(r0rkcn→1)
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
16 / 18

---

## Page 79

Inductive structure
Final step combines two subproducts
(M0 · M1 · · · Mk→1) · (Mk · Mk+1 · · · Mn→1)
for some 0 < k < n
First factor is r0 ↔ck→1, second is
rk ↔cn→1, where rk = ck→1
Let C(0, n↓1) denote the overall cost
Final multiplication is O(r0rkcn→1)
Inductively, costs of factors are C(0, k↓1)
and C(k, n↓1)
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
16 / 18

---

## Page 80

Inductive structure
Final step combines two subproducts
(M0 · M1 · · · Mk→1) · (Mk · Mk+1 · · · Mn→1)
for some 0 < k < n
First factor is r0 ↔ck→1, second is
rk ↔cn→1, where rk = ck→1
Let C(0, n↓1) denote the overall cost
Final multiplication is O(r0rkcn→1)
Inductively, costs of factors are C(0, k↓1)
and C(k, n↓1)
C(0, n↓1) =
C(0, k↓1) + C(k, n↓1) + r0rkcn→1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
16 / 18

---

## Page 81

Inductive structure
Final step combines two subproducts
(M0 · M1 · · · Mk→1) · (Mk · Mk+1 · · · Mn→1)
for some 0 < k < n
First factor is r0 ↔ck→1, second is
rk ↔cn→1, where rk = ck→1
Let C(0, n↓1) denote the overall cost
Final multiplication is O(r0rkcn→1)
Inductively, costs of factors are C(0, k↓1)
and C(k, n↓1)
C(0, n↓1) =
C(0, k↓1) + C(k, n↓1) + r0rkcn→1
Which k should we choose?
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
16 / 18

---

## Page 82

Inductive structure
Final step combines two subproducts
(M0 · M1 · · · Mk→1) · (Mk · Mk+1 · · · Mn→1)
for some 0 < k < n
First factor is r0 ↔ck→1, second is
rk ↔cn→1, where rk = ck→1
Let C(0, n↓1) denote the overall cost
Final multiplication is O(r0rkcn→1)
Inductively, costs of factors are C(0, k↓1)
and C(k, n↓1)
C(0, n↓1) =
C(0, k↓1) + C(k, n↓1) + r0rkcn→1
Which k should we choose?
Try all and choose the minimum!
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
16 / 18

---

## Page 83

Inductive structure
Final step combines two subproducts
(M0 · M1 · · · Mk→1) · (Mk · Mk+1 · · · Mn→1)
for some 0 < k < n
First factor is r0 ↔ck→1, second is
rk ↔cn→1, where rk = ck→1
Let C(0, n↓1) denote the overall cost
Final multiplication is O(r0rkcn→1)
Inductively, costs of factors are C(0, k↓1)
and C(k, n↓1)
C(0, n↓1) =
C(0, k↓1) + C(k, n↓1) + r0rkcn→1
Which k should we choose?
Try all and choose the minimum!
Subproblems?
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
16 / 18

---

## Page 84

Inductive structure
Final step combines two subproducts
(M0 · M1 · · · Mk→1) · (Mk · Mk+1 · · · Mn→1)
for some 0 < k < n
First factor is r0 ↔ck→1, second is
rk ↔cn→1, where rk = ck→1
Let C(0, n↓1) denote the overall cost
Final multiplication is O(r0rkcn→1)
Inductively, costs of factors are C(0, k↓1)
and C(k, n↓1)
C(0, n↓1) =
C(0, k↓1) + C(k, n↓1) + r0rkcn→1
Which k should we choose?
Try all and choose the minimum!
Subproblems?
M0 · M1 · · · Mk→1 would decompose
as (M0 · · · Mj→1) · (Mj · · · Mk→1)
Generic subproblem is
Mj · Mj+1 · · · Mk
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
16 / 18
Mom ,

---

## Page 85

Inductive structure
Final step combines two subproducts
(M0 · M1 · · · Mk→1) · (Mk · Mk+1 · · · Mn→1)
for some 0 < k < n
First factor is r0 ↔ck→1, second is
rk ↔cn→1, where rk = ck→1
Let C(0, n↓1) denote the overall cost
Final multiplication is O(r0rkcn→1)
Inductively, costs of factors are C(0, k↓1)
and C(k, n↓1)
C(0, n↓1) =
C(0, k↓1) + C(k, n↓1) + r0rkcn→1
Which k should we choose?
Try all and choose the minimum!
Subproblems?
M0 · M1 · · · Mk→1 would decompose
as (M0 · · · Mj→1) · (Mj · · · Mk→1)
Generic subproblem is
Mj · Mj+1 · · · Mk
C(j, k) =
minj<ω↑k [C(j, ω↓1) + C(ω, k) + rjrωck]
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
16 / 18
a

---

## Page 86

Inductive structure
Final step combines two subproducts
(M0 · M1 · · · Mk→1) · (Mk · Mk+1 · · · Mn→1)
for some 0 < k < n
First factor is r0 ↔ck→1, second is
rk ↔cn→1, where rk = ck→1
Let C(0, n↓1) denote the overall cost
Final multiplication is O(r0rkcn→1)
Inductively, costs of factors are C(0, k↓1)
and C(k, n↓1)
C(0, n↓1) =
C(0, k↓1) + C(k, n↓1) + r0rkcn→1
Which k should we choose?
Try all and choose the minimum!
Subproblems?
M0 · M1 · · · Mk→1 would decompose
as (M0 · · · Mj→1) · (Mj · · · Mk→1)
Generic subproblem is
Mj · Mj+1 · · · Mk
C(j, k) =
minj<ω↑k [C(j, ω↓1) + C(ω, k) + rjrωck]
Base case: C(j, j) = 0 for 0 ↑j < n
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
16 / 18

---

## Page 87

Mo
. [M .
-
-
Mmi]
(10, Y
<(in)
O

---

## Page 88

Subproblem dependency
Compute C(i, j), 0 →i, j < n

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18

---

## Page 89

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18

-

---

## Page 90

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal
C(i, j) depends on C(i, k↑1), C(k, j)
for every i < k →j

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18
-
(ii) =cre,-

---

## Page 91

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal
C(i, j) depends on C(i, k↑1), C(k, j)
for every i < k →j

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18

---

## Page 92

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal
C(i, j) depends on C(i, k↑1), C(k, j)
for every i < k →j

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18

---

## Page 93

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal
C(i, j) depends on C(i, k↑1), C(k, j)
for every i < k →j

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18
vo
-
-

---

## Page 94

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal
C(i, j) depends on C(i, k↑1), C(k, j)
for every i < k →j
O(n) dependencies per entry, unlike
LCW, LCS and ED

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18

---

## Page 95

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal
C(i, j) depends on C(i, k↑1), C(k, j)
for every i < k →j
O(n) dependencies per entry, unlike
LCW, LCS and ED
Diagonal entries are base case

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18

---

## Page 96

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal
C(i, j) depends on C(i, k↑1), C(k, j)
for every i < k →j
O(n) dependencies per entry, unlike
LCW, LCS and ED
Diagonal entries are base case
Fill matrix by diagonal, from main
diagonal

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18

---

## Page 97

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal
C(i, j) depends on C(i, k↑1), C(k, j)
for every i < k →j
O(n) dependencies per entry, unlike
LCW, LCS and ED
Diagonal entries are base case
Fill matrix by diagonal, from main
diagonal

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18

O

---

## Page 98

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal
C(i, j) depends on C(i, k↑1), C(k, j)
for every i < k →j
O(n) dependencies per entry, unlike
LCW, LCS and ED
Diagonal entries are base case
Fill matrix by diagonal, from main
diagonal

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18

---

## Page 99

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal
C(i, j) depends on C(i, k↑1), C(k, j)
for every i < k →j
O(n) dependencies per entry, unlike
LCW, LCS and ED
Diagonal entries are base case
Fill matrix by diagonal, from main
diagonal

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18

---

## Page 100

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal
C(i, j) depends on C(i, k↑1), C(k, j)
for every i < k →j
O(n) dependencies per entry, unlike
LCW, LCS and ED
Diagonal entries are base case
Fill matrix by diagonal, from main
diagonal

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18

---

## Page 101

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal
C(i, j) depends on C(i, k↑1), C(k, j)
for every i < k →j
O(n) dependencies per entry, unlike
LCW, LCS and ED
Diagonal entries are base case
Fill matrix by diagonal, from main
diagonal

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18

---

## Page 102

Subproblem dependency
Compute C(i, j), 0 →i, j < n
Only for i →j
Entries above main diagonal
C(i, j) depends on C(i, k↑1), C(k, j)
for every i < k →j
O(n) dependencies per entry, unlike
LCW, LCS and ED
Diagonal entries are base case
Fill matrix by diagonal, from main
diagonal

· · ·
i
· · ·
· · ·
j
· · · n↑1

· · ·
i
· · ·
· · ·
j
· · ·
n↑1
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
17 / 18

---

## Page 103

Implementation
def C(dim):
# dim: dimension matrix,
#
entries are pairs (r_i,c_i)
import numpy as np
n = dim.shape[0]
C = np.zeros((n,n))
for i in range(n):
C[i,i] = 0
for diff in range(1,n):
for i in range(0,n-diff):
j = i + diff
C[i,j] = C[i,i] +
C[i+1,j] +
dim[i][0]*dim[i+1][0]*dim[j][1]
for k in range(i+1,j+1):
C[i,j] = min(C[i,j],
C[i,k-1] + C[k,j] +
dim[i][0]*dim[k][0]*dim[j][1])
return(C[0,n-1])
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
18 / 18
·
J

---

## Page 104

Implementation
def C(dim):
# dim: dimension matrix,
#
entries are pairs (r_i,c_i)
import numpy as np
n = dim.shape[0]
C = np.zeros((n,n))
for i in range(n):
C[i,i] = 0
for diff in range(1,n):
for i in range(0,n-diff):
j = i + diff
C[i,j] = C[i,i] +
C[i+1,j] +
dim[i][0]*dim[i+1][0]*dim[j][1]
for k in range(i+1,j+1):
C[i,j] = min(C[i,j],
C[i,k-1] + C[k,j] +
dim[i][0]*dim[k][0]*dim[j][1])
return(C[0,n-1])
Complexity
We have to fill a table of size
O(n2)
Filling each entry takes O(n)
Overall, O(n3)
Madhavan Mukund
Lecture 26, 20 November 2025
PDSP Lecture 26
18 / 18
Brute force is exponential