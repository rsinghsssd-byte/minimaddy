## Page 1

Programming and Data Structures with Python 2025
Assignment 2
2 Oct 2025, due 9 Oct 12 Oct 2025
Polynomials
Let us consider polynomials in a single variable x with integer coefficients — for instance, 3x4−17x2−3x+5.
Our goal is to write a Python class to represent such polynomials.
Note that any such polynomial is a collection of pairs of the form (coefficient,exponent), where no two
pairs have the same second component (exponent). For instance, the polynomial above consists of the
pairs (3, 4), (−17, 2), (−3, 1) and (5, 0).
Choose a suitable representation, including one for the zero polynomial, and write a class Polynomial
with the following features.
• The constructor should take a list of (coefficient,exponent) pairs [(c1,e1),(c2,e2),...,(cn,en)]
and create the corresponding polynomial c1xe1 + c2xe2 + · · · cnxen. In this list, the exponents need
not be distinct. If no list is provided, create the zero polynomial.
• The class should have a function iszero() such that p.iszero() returns True precisely when p
represents the zero polynomial.
• Given polynomials p and q, the expressions p+q, p-q and p*q should return polynomials for the
sum, difference and product of p and q, respectively.
• Given polynomials p and q, the comparisons p < q, p <= q, p > q, p >= q, p == q and p != q
should return sensible values. To compare polynomials, use lexicographic ordering with respect
to (exponent,coefficient). In other words, first compare the highest exponent. If these are equal,
compare the coefficient of the highest exponent. If these are again equal, go to the next smaller
terms in each polynomial and apply the same rule.
• print(p) should print a sensible representation of p without any zero coefficients. For instance, if
p represents 3x4 −17x2 −3x + 5, print(p) could produce 3xˆ4 - 17xˆ2 - 3x + 5.
Instructions
• Submit your solution through Moodle as a single Python notebook
• Add documentation to explain at a high level what your code is doing
• Show some sample executions