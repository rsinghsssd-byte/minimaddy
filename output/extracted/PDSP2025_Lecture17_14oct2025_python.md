## Page 1

Lecture 17, 14 October 2025
String formatting -- positional arguments
x = 7
y = 22
message = "First one is {1}, second one is {0}"
message.format(x,y)
'First one is 22, second one is 7'
x = 7
y = 22
message1 = "First one is {1}, second one is {0}. To repeat, first one is
message1.format(x,y)
'First one is 22, second one is 7. To repeat, first one is 22.'
Raising an exception in List()
Inserting a negative value raises ValueError
Use string formatting to add negative value to error message
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
            raise ValueError("Negative input:{0}".format(v))
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
        if v < 0:
            raise ValueError("Negative input:{0}".format(v))
        if self.isempty():
In [1]:
Out[1]:
In [2]:
Out[2]:
In [3]:

---

## Page 2

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
            raise ValueError("Negative input:{0}".format(v))
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

        while temp.next != None:
          temp = temp.next
          selflist.append(temp.value)

---

## Page 3

return(str(selflist))
l = List([1,-2,3])
print(l)
--------------------------------------------------------------------------
-
ValueError                                Traceback (most recent call las
t)
Cell In[4], line 1
----> 1 l = List([1,-2,3])
     2 print(l)
Cell In[3], line 6, in List.__init__(self, initlist)
     4 self.next = None
     5 for x in initlist:
----> 6     self.append(x)
     7 return
Cell In[3], line 39, in List.append(self, v)
    38 def append(self,v):
---> 39     self.appendr(v)
    40     return
Cell In[3], line 29, in List.appendr(self, v)
    27 def appendr(self,v):   # append, recursive
    28     if v < 0:
---> 29         raise ValueError("Negative input:{0}".format(v))
    30     if self.isempty():
    31         self.value = v
ValueError: Negative input:-2
String formatting with output specification
"Value {0:8.2f}".format(747.3)
'Value   747.30'
"Value {0:6.2f} {0:27.7f}".format(99999999947.3444,22)
'Value 99999999947.34         99999999947.3444061'
Modifying behaviour of print()
x = 5
y = 7
print(x,y)
print(y)
5 7

x = 5
y = 7
print(x,y,sep=":")
In [4]:
In [5]:
Out[5]:
In [6]:
Out[6]:
In [7]:
In [8]:

---

## Page 4

5:7
l = list(range(20))
for x in l:
    print(x,end=", ")
print("Where are we?")
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, Wher
e are we?
for x in l:
    print(x,end=", ")
print()
print("Where are we?")
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
Where are we?
Working with files
Reading files
Open a file in mode "r"
fh = open("oz.txt","r")
read() returns a string with the entire file
Note the \n characters indicating end of line ("new line")
contents = fh.read()
contents
'I met a traveller from an antique land\nWho said: Two vast and trunkles
s legs of stone\nStand in the desaet. Near them, on the sand,\nHalf sun
k, a shattered visage lies, whose frown,\nAnd wrinkled lip, and sneer of
cold command,\nTell that its sculptor well those passions read\nWhich ye
t survive, stamped on these lifeless things,\nThe hand that mocked them
and the heart that fed:\nAnd on the pedestal these words appear:\n"My na
me is Ozymandias, King of Kings:\nLook on my works, ye Mighty, and despa
ir!"\nNo thing beside remains. Round the decay\nOf that colossal wreck,
boundless and bare\nThe lone and level sands stretch far away. \n'
After reading the file, we are at the end
End of file is indicated by read() returning the empty string
fh.read()
''
fh.read()
''
In [9]:
In [10]:
In [11]:
In [12]:
In [13]:
Out[13]:
In [14]:
Out[14]:
In [15]:
Out[15]:

---

## Page 5

To re-read the file, we have to close it and open it again
fh.close()
readline() reads one line
Unlike input() , the line that is read includes the terminating `\n'
fh = open("oz.txt","r")
line1 = fh.readline()
line1
'I met a traveller from an antique land\n'
readlines() returns the entire file as a list of lines
Each line is terminated by \n
fh.close()
fh = open("oz.txt","r")
alllines = fh.readlines()
alllines
['I met a traveller from an antique land\n',
'Who said: Two vast and trunkless legs of stone\n',
'Stand in the desaet. Near them, on the sand,\n',
'Half sunk, a shattered visage lies, whose frown,\n',
'And wrinkled lip, and sneer of cold command,\n',
'Tell that its sculptor well those passions read\n',
'Which yet survive, stamped on these lifeless things,\n',
'The hand that mocked them and the heart that fed:\n',
'And on the pedestal these words appear:\n',
'"My name is Ozymandias, King of Kings:\n',
'Look on my works, ye Mighty, and despair!"\n',
'No thing beside remains. Round the decay\n',
'Of that colossal wreck, boundless and bare\n',
'The lone and level sands stretch far away. \n']
readlines() returns the lines from the current position
In the following example, the list returned is from the second line onwards
fh.close()
fh = open("oz.txt","r")
line1 = fh.readline()      # Read first line
alllines = fh.readlines()  # From second line onwards
alllines
In [16]:
In [17]:
Out[17]:
In [18]:
Out[18]:
In [19]:

---

## Page 6

['Who said: Two vast and trunkless legs of stone\n',
'Stand in the desaet. Near them, on the sand,\n',
'Half sunk, a shattered visage lies, whose frown,\n',
'And wrinkled lip, and sneer of cold command,\n',
'Tell that its sculptor well those passions read\n',
'Which yet survive, stamped on these lifeless things,\n',
'The hand that mocked them and the heart that fed:\n',
'And on the pedestal these words appear:\n',
'"My name is Ozymandias, King of Kings:\n',
'Look on my works, ye Mighty, and despair!"\n',
'No thing beside remains. Round the decay\n',
'Of that colossal wreck, boundless and bare\n',
'The lone and level sands stretch far away. \n']
Stripping white space
We can strip off leading and trailing "white space" (blank, tab, newline) from a string
rstrip() removes trailing whitespace
Note that strings are immutable, so the function returns a new string, leaving the
original untouched
teststr = "   abc    \n"
teststr
'   abc    \n'
teststr.rstrip()
'   abc'
teststr
'   abc    \n'
lstrip() removes leading whitespace
teststr.lstrip()
'abc    \n'
strip() removes whitespace at both ends
teststr.strip()
'abc'
Can use these to quickly remove \n from lines that we read from a file
In the first loop below, there is a blank line between actual lines because of the \n
in the input line followed by the newline inserted by print()
Out[19]:
In [20]:
Out[20]:
In [21]:
Out[21]:
In [22]:
Out[22]:
In [23]:
Out[23]:
In [24]:
Out[24]:

---

## Page 7

fh.close()
fh = open("oz.txt","r")
for l in fh.readlines():
    print(l)
I met a traveller from an antique land
Who said: Two vast and trunkless legs of stone
Stand in the desaet. Near them, on the sand,
Half sunk, a shattered visage lies, whose frown,
And wrinkled lip, and sneer of cold command,
Tell that its sculptor well those passions read
Which yet survive, stamped on these lifeless things,
The hand that mocked them and the heart that fed:
And on the pedestal these words appear:
"My name is Ozymandias, King of Kings:
Look on my works, ye Mighty, and despair!"
No thing beside remains. Round the decay
Of that colossal wreck, boundless and bare
The lone and level sands stretch far away.
If we strip each line before printing, the blank lines are eliminated
fh.close()
fh = open("oz.txt","r")
for l in fh.readlines():
    print(l.rstrip())
I met a traveller from an antique land
Who said: Two vast and trunkless legs of stone
Stand in the desaet. Near them, on the sand,
Half sunk, a shattered visage lies, whose frown,
And wrinkled lip, and sneer of cold command,
Tell that its sculptor well those passions read
Which yet survive, stamped on these lifeless things,
The hand that mocked them and the heart that fed:
And on the pedestal these words appear:
"My name is Ozymandias, King of Kings:
Look on my works, ye Mighty, and despair!"
No thing beside remains. Round the decay
Of that colossal wreck, boundless and bare
The lone and level sands stretch far away.
Writing files
In [25]:
In [26]:

---

## Page 8

Open a file in mode "w"
Opening a non-existent file for reading generates an error
Opening a non-existent file for writing creates a new file
If the file already exists, write will overwrite the contents
infile = open("newfile.txt","r")
--------------------------------------------------------------------------
-
FileNotFoundError                         Traceback (most recent call las
t)
Cell In[27], line 1
----> 1 infile = open("newfile.txt","r")
File ~/python-venv/lib/python3.13/site-packages/IPython/core/interactivesh
ell.py:343, in _modified_open(file, *args, **kwargs)
   336 if file in {0, 1, 2}:
   337     raise ValueError(
   338         f"IPython won't let you open fd={file} by default "
   339         "as it is likely to crash IPython. If you know what you ar
e doing, "
   340         "you can use builtins' open."
   341     )
--> 343 return io_open(file, *args, **kwargs)
FileNotFoundError: [Errno 2] No such file or directory: 'newfile.txt'
outfile = open("newfile.txt","w")
outfile.close()
fh.write(s) writes the string s to the file associated with file handle fh
Need to add \n ourselves to ensure the end of line
fh.writelines(sl) writes a list of strings ls
Again, we need to ensure \n is present at the end of each string in the list
The name of the function is misleading
It is more accurate to call it writestrings() since we have to insert \n
manually
The following loop copies the input to the output
Each line that is read includes the \n
Hence each line that is written also has the corresponding \n
However, after this loop, typically the output file will be empty
Need to close the file handle for the buffer to be "flushed" to the disk
infile = open("oz.txt","r")
outfile = open("newfile.txt","w")
for l in infile.readlines():
    outfile.write(l)
In [27]:
In [28]:
In [29]:
In [30]:

---

## Page 9

outfile.close()
Close all file handles when you are done with them
infile = open("oz.txt","r")
outfile = open("newfile.txt","w")
for l in infile.readlines():
    outfile.write(l)
infile.close()
outfile.close()
We can also read all the lines into a list using readlines() and write them out
using writelines()
infile = open("oz.txt","r")
outfile = open("newfile.txt","w")
contents = infile.readlines()
outfile.writelines(contents)
infile.close()
outfile.close()
Appending output
We can append our writes at the end of a file
Open the file with mode "a" instead of "w"
After the following, newfile.txt should have two copies of oz.txt
infile = open("oz.txt","r")
outfile = open("newfile.txt","a")
contents = infile.readlines()
outfile.writelines(contents)
infile.close()
outfile.close()
There are other functions we have not discussed
fh.seek(n) moves to position n in the file
After reading a file, use fh.seek(0) to return to the start
fh.read(n) reads n characters from the current position
infile = open("oz.txt","r")
c1 = infile.read()
infile.seek(0)
c2 = infile.read(20)
c1
In [31]:
In [32]:
In [33]:
In [34]:
In [35]:
In [36]:

---

## Page 10

'I met a traveller from an antique land\nWho said: Two vast and trunkles
s legs of stone\nStand in the desaet. Near them, on the sand,\nHalf sun
k, a shattered visage lies, whose frown,\nAnd wrinkled lip, and sneer of
cold command,\nTell that its sculptor well those passions read\nWhich ye
t survive, stamped on these lifeless things,\nThe hand that mocked them
and the heart that fed:\nAnd on the pedestal these words appear:\n"My na
me is Ozymandias, King of Kings:\nLook on my works, ye Mighty, and despa
ir!"\nNo thing beside remains. Round the decay\nOf that colossal wreck,
boundless and bare\nThe lone and level sands stretch far away. \n'
c2
'I met a traveller fr'
Out[36]:
In [37]:
Out[37]: