## Page 1

PDSP 2025, Lecture 11, 11 September 2025
Scope and global variables
The scope of a variable refers to the portion of the program where its value is
available
If we refer to a value that is not defined in a function, it is looked up in the
global context
def f():
    y = x + 22
    print(y)
    return
x = 7
f()

As soon as we assign a variable a value inside a function, all instances of that
variable are treated as local to the function
This decision is static based on the program text. In the code below, we cannot
be sure that the assignment x = 33 will execute, but Python still denotes x
to be local to f()
Though the check is based on the static program text, the error is flagged only
when the function executes. The definition of f() does not trigger an error
though the problem is evident in the text of the function.
def f():
    y = x + 22
    print(y)
    if y > 1000:
        x = 33
    return
x = 7
f()
In [1]:
In [2]:
In [3]:
In [4]:

---

## Page 2

--------------------------------------------------------------------------
-
UnboundLocalError                         Traceback (most recent call las
t)
Cell In[4], line 2
     1 x = 7
----> 2 f()
Cell In[3], line 2, in f()
     1 def f():
----> 2     y = x + 22
     3     print(y)
     4     if y > 1000:
UnboundLocalError: cannot access local variable 'x' where it is not associ
ated with a value
This static check applies even if it is impossible for the local assignment to be
executed
def checky():
    y = x + 2
    return
    if False:
        x = 7
x = 8
checky()
--------------------------------------------------------------------------
-
UnboundLocalError                         Traceback (most recent call las
t)
Cell In[6], line 2
     1 x = 8
----> 2 checky()
Cell In[5], line 2, in checky()
     1 def checky():
----> 2     y = x + 2
     3     return
     4     if False:
UnboundLocalError: cannot access local variable 'x' where it is not associ
ated with a value
More examples of using global values within a function without redefining the
variable
def display_count():
    print(count)
    return
def display_upto_count():
    for i in range(count):
In [5]:
In [6]:
In [7]:
In [8]:

---

## Page 3

print(count+i)
    return
If we call display_count() without a global definition for count we get an
error
display_count()
--------------------------------------------------------------------------
-
NameError                                 Traceback (most recent call las
t)
Cell In[9], line 1
----> 1 display_count()
Cell In[7], line 2, in display_count()
     1 def display_count():
----> 2     print(count)
     3     return
NameError: name 'count' is not defined
If count is available in the global context, the two functions work as expected
count = 7
display_count()

display_upto_count()

If we try to update count inside the function, both occurrences become local
The occurrence on the right hand side of the assignment generates an error
because its value is now undefined
Once again, this static error is only triggered at run-time when the function
executes
def increment_local(k):
    count = count+k
    return
increment_local(2)
In [9]:
In [10]:
In [11]:
In [12]:
In [13]:
In [14]:

---

## Page 4

--------------------------------------------------------------------------
-
UnboundLocalError                         Traceback (most recent call las
t)
Cell In[14], line 1
----> 1 increment_local(2)
Cell In[13], line 2, in increment_local(k)
     1 def increment_local(k):
----> 2     count = count+k
     3     return
UnboundLocalError: cannot access local variable 'count' where it is not as
sociated with a value
Reassigning a variable within a function disconnects it from the external
variable with the same name
def reset_local(k):
    count = k
    return
reset_local(77)
count

We can declare a variable to be global to override Python's default scope
rules
global tells Python to treat the variable inside the function as one from the
global context
def increment_global(k):
    global count
    count = count+k
    return
increment_global(8)
display_count()

The default rule about local scope applies to mutable values as well
def concat_local():
    l1 = l1 + l2
    return
l1 = [1,2,3]
l2 = [4,5,6]
concat_local()
In [15]:
In [16]:
In [17]:
Out[17]:
In [18]:
In [19]:
In [20]:
In [21]:
In [22]:

---

## Page 5

--------------------------------------------------------------------------
-
UnboundLocalError                         Traceback (most recent call las
t)
Cell In[22], line 3
     1 l1 = [1,2,3]
     2 l2 = [4,5,6]
----> 3 concat_local()
Cell In[21], line 2, in concat_local()
     1 def concat_local():
----> 2     l1 = l1 + l2
     3     return
UnboundLocalError: cannot access local variable 'l1' where it is not assoc
iated with a value
def concat_global():
    global l1
    l1 = l1 + l2
    return
l1 = [1,2,3]
l2 = [4,5,6]
concat_global()
l1, l2
([1, 2, 3, 4, 5, 6], [4, 5, 6])
We can define a value inside a function and "export" it outside by declaring it
global
del(l1)
del(l2)
def concat_global():
    global l1
    l1 = [1,2,3]
    l1 = l1 + l2
    return
l2 = [4,5,6]
concat_global()
l1
[1, 2, 3, 4, 5, 6]
The following would work with dynamic scoping -- based on execution of
program
init() defines b and then calls seta() , so with dynamic scoping, b
is known to seta()
In [23]:
In [24]:
In [25]:
Out[25]:
In [26]:
In [27]:
In [28]:
In [29]:
Out[29]:

---

## Page 6

Python uses static scoping -- based on text of program -- so this code generates
an error
Most languages use static scoping because dynamic scoping makes it hard to
reason about correctness
def seta():
    a = b + 5
    print(a)
def init():
    b = 7
    seta()
init()
--------------------------------------------------------------------------
-
NameError                                 Traceback (most recent call las
t)
Cell In[30], line 9
     6     b = 7
     7     seta()
----> 9 init()
Cell In[30], line 7, in init()
     5 def init():
     6     b = 7
----> 7     seta()
Cell In[30], line 2, in seta()
     1 def seta():
----> 2     a = b + 5
     3     print(a)
NameError: name 'b' is not defined
In [30]: