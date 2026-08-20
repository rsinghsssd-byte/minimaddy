## Page 1

PDSP 2025, Lecture 08, 2 September 2025
Nested collections
List of lists, list of tuples, dictionary whose values are lists ...
matchlist is a list of tuples
Use two indices to extract a value
matchlist[3] is ("Jaipur","RR","LSG","RR","RR",194)
matchlist[3][1] is "RR"
matchlist = [
    ("Chennai","RCB","CSK","RCB","CSK",174),
    ("Mohali","DC","PK","PK","PK",175),
    ("Kolkata","KKR","SRH","SRH","KKR",209),
    ("Jaipur","RR","LSG","RR","RR",194),
    ("Ahmedabad","GT","MI","MI","GT",169),
    ("Bengaluru","PK","RCB","RCB","RCB",177),
    ("Chennai","CSK","GT","GT","CSK",207),
    ("Hyderabad","SRH","MI","MI","SRH",278),
    ("Jaipur","RR","DC","DC","RR",186),
    ("Bengaluru","RCB","KKR","KKR","KKR",183),
    ("Lucknow","LSG","PK","LSG","LSG",200),
    ("Ahmedabad","SRH","GT","SRH","GT",163),
    ("Visakhapatnam","DC","CSK","DC","DC",192),
    ("Mumbai","MI","RR","RR","RR",126),
    ("Bengaluru","LSG","RCB","RCB","LSG",182),
    ("Visakhapatnam","KKR","DC","KKR","KKR",273),
    ("Ahmedabad","GT","PK","PK","PK",200),
    ("Hyderabad","CSK","SRH","SRH","SRH",166),
    ("Jaipur","RCB","RR","RR","RR",184),
    ("Mumbai","MI","DC","DC","MI",235),
    ("Lucknow","LSG","GT","LSG","LSG",164),
    ("Chennai","KKR","CSK","CSK","CSK",138),
    ("Mohali","SRH","PK","PK","SRH",183),
    ("Jaipur","RR","GT","GT","GT",197),
    ("Mumbai","RCB","MI","MI","MI",197),
    ("Lucknow","LSG","DC","LSG","DC",168),
    ("Mohali","PK","RR","RR","RR",148),
    ("Kolkata","LSG","KKR","KKR","KKR",162),
    ("Mumbai","CSK","MI","MI","CSK",207),
    ("Bengaluru","SRH","RCB","RCB","SRH",288),
    ("Kolkata","KKR","RR","RR","RR",224),
    ("Ahmedabad","GT","DC","DC","DC",90),
    ("Mohali","MI","PK","PK","MI",193),
    ("Lucknow","CSK","LSG","LSG","LSG",177),
    ("Delhi","SRH","DC","DC","SRH",267),
    ("Kolkata","KKR","RCB","RCB","KKR",223),
    ("Mohali","PK","GT","PK","GT",143),
    ("Jaipur","MI","RR","MI","RR",180),
    ("Chennai","CSK","LSG","LSG","LSG",211),
    ("Delhi","DC","GT","GT","DC",225),
    ("Hyderabad","RCB","SRH","RCB","RCB",207),
    ("Kolkata","KKR","PK","PK","PK",262),
    ("Delhi","DC","MI","MI","DC",258),
    ("Lucknow","LSG","RR","RR","RR",197),
    ("Ahmedabad","GT","RCB","RCB","RCB",201),
    ("Chennai","CSK","SRH","SRH","CSK",213),
    ("Kolkata","DC","KKR","DC","KKR",154),
    ("Lucknow","MI","LSG","LSG","LSG",145),
    ("Chennai","CSK","PK","PK","PK",163),
    ("Hyderabad","SRH","RR","SRH","SRH",202),
    ("Mumbai","KKR","MI","MI","KKR",170),
    ("Bengaluru","GT","RCB","RCB","RCB",148),
    ("Dharamsala","CSK","PK","PK","CSK",168),
    ("Lucknow","KKR","LSG","LSG","KKR",236),
    ("Mumbai","SRH","MI","MI","MI",174),
    ("Delhi","DC","RR","RR","DC",222),
    ("Hyderabad","LSG","SRH","LSG","SRH",166),
    ("Dharamsala","RCB","PK","PK","RCB",242),
In [1]:

---

## Page 2

("Ahmedabad","GT","CSK","CSK","GT",232),
    ("Kolkata","KKR","MI","MI","KKR",158),
    ("Chennai","RR","CSK","RR","CSK",142),
    ("Bengaluru","RCB","DC","DC","RCB",188),
    ("Delhi","DC","LSG","LSG","DC",209),
    ("Guwahati","RR","PK","RR","PK",145),
    ("Mumbai","LSG","MI","MI","LSG",215),
    ("Bengaluru","RCB","CSK","CSK","RCB",219),
    ("Hyderabad","PK","SRH","PK","SRH",215),
    ("Ahmedabad","SRH","KKR","SRH","KKR",160),
    ("Ahmedabad","RCB","RR","RR","RR",173),
    ("Chennai","SRH","RR","RR","SRH",176),
    ("Chennai","SRH","KKR","SRH","KKR",114)
]
List of venues where each team played played IPL 2024
Initially, build a dictionary of dictionaries
Outer keys are team names
Inner dictionary keys are venues where team played
Finally, convert dictionary of dictionaries into dictionary of lists
def get_venues(l):
    venues = {}
    for m in l:
        venue,team1,team2 = m[0],m[1],m[2]
        for t in team1,team2:
            if t in venues:
                venues[t][venue] = 1
            else:
                venues[t] = {venue:1}  # Create a dictionary for venues[t]
                                       # Equivalent to
                                       #   venues[t] = {}
                                       #   venues[t[[venue] = 1
    venuelists = {}
    for t in sorted(venues):           # Scan teams in alphabetical order
        venuelists[t] = sorted(list(venues[t]))  # Sort venues in alphabetical order
    return(venuelists)
get_venues(matchlist)
In [2]:
In [3]:

---

## Page 3

{'CSK': ['Ahmedabad',
 'Bengaluru',
 'Chennai',
 'Dharamsala',
 'Hyderabad',
 'Lucknow',
 'Mumbai',
 'Visakhapatnam'],
'DC': ['Ahmedabad',
 'Bengaluru',
 'Delhi',
 'Jaipur',
 'Kolkata',
 'Lucknow',
 'Mohali',
 'Mumbai',
 'Visakhapatnam'],
'GT': ['Ahmedabad',
 'Bengaluru',
 'Chennai',
 'Delhi',
 'Jaipur',
 'Lucknow',
 'Mohali'],
'KKR': ['Ahmedabad',
 'Bengaluru',
 'Chennai',
 'Kolkata',
 'Lucknow',
 'Mumbai',
 'Visakhapatnam'],
'LSG': ['Bengaluru',
 'Chennai',
 'Delhi',
 'Hyderabad',
 'Jaipur',
 'Kolkata',
 'Lucknow',
 'Mumbai'],
'MI': ['Ahmedabad',
 'Delhi',
 'Hyderabad',
 'Jaipur',
 'Kolkata',
 'Lucknow',
 'Mohali',
 'Mumbai'],
'PK': ['Ahmedabad',
 'Bengaluru',
 'Chennai',
 'Dharamsala',
 'Guwahati',
 'Hyderabad',
 'Kolkata',
 'Lucknow',
 'Mohali'],
'RCB': ['Ahmedabad',
 'Bengaluru',
 'Chennai',
 'Dharamsala',
 'Hyderabad',
 'Jaipur',
 'Kolkata',
 'Mumbai'],
'RR': ['Ahmedabad',
 'Chennai',
 'Delhi',
 'Guwahati',
 'Hyderabad',
 'Jaipur',
 'Kolkata',
 'Lucknow',
 'Mohali',
 'Mumbai'],
'SRH': ['Ahmedabad',
Out[3]:

---

## Page 4

'Bengaluru',
 'Chennai',
 'Delhi',
 'Hyderabad',
 'Kolkata',
 'Mohali',
 'Mumbai']}
Matrices
Matrix is a list of lists
Each row is a list of values [v1,v2,...vm]
Matrix is a list of rows [ row1, row2, ..., rown ]
Transpose a matrix
Columns of original matrix are rows of transpose
If input is square, can swap M[i][j] and M[j][i]
If not square, need to construct transpose of correct dimension
def transpose(mat):
    # Extract dimensions of input -- assume well-formed, non-empty
    nrows = len(mat)
    ncols = len(mat[0])
    # Create an empty matrix for the transpose
    trmat = []
    for i in range(ncols):
        trmat.append([])
    # Populate the transpose -- append each M[i][j] to row j of transpose
    for i in range(nrows):
        for j in range(ncols):
            trmat[j].append(mat[i][j])
    return(trmat)
m = [[0,3],[1,4],[2,5]]
mt = transpose(m)
m, mt
([[0, 3], [1, 4], [2, 5]], [[0, 1, 2], [3, 4, 5]])
Strings
Also sequences, of characters
String values can be enclosed in single or double quotes
'Chennai' or "Chennai"
Allows a value that has a quote to be easily embedded
"Fermat's Last Theorem"
'He said, "Thank you!"
If you need to use both single and double quotes inside the string, use a triple quote!
'''He said, "That's great!"'''
s = '''He said, "That's great!"'''
s
'He said, "That\'s great!"'
Python prefers to render strings using single quote
Embedded quotes are "escaped" using \ to remove their special meaning
Like lists and tuples, can access elements of a string by position, or by slices
In [4]:
In [5]:
In [6]:
Out[6]:
In [7]:
In [8]:
Out[8]:

---

## Page 5

s = "hello"
s[1]
'e'
s[2:4]
'll'
Some languages have a separate type char for a single character
A string is then a sequence of char
In Python, there is only the string type str
A single character is the same as a string of length 1
s[1] == "e"  # Logically speaking, s[1] is a single character
True
Concatenate strings using +
s = "hello"
t = "there"
s+t, s, t
('hellothere', 'hello', 'there')
Like tuples, cannot update parts of a string directly
s[3] = "p"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[15], line 1
----> 1 s[3] = "p"
TypeError: 'str' object does not support item assignment
Instead, assemble a new string from the old one
s = s[0:3] + "p" + s[4:]
s
'helpo'
Can iterate over strings and check membership, like lists
For iteration, no distinction between a string "xyz" and the list ["x","y","z"]
def vowel(c):
    return(c in "aeiou")
vowel("a"),vowel("b"),
(True, False)
For stringx x in s seems to be interpreted as substring membership
vowel("ae"),vowel("ai"),vowel("io")
(True, False, True)
In [9]:
In [10]:
Out[10]:
In [11]:
Out[11]:
In [12]:
Out[12]:
In [13]:
In [14]:
Out[14]:
In [15]:
In [16]:
In [17]:
Out[17]:
In [18]:
In [19]:
Out[19]:
In [20]:
Out[20]:

---

## Page 6

Standard example of filtered iteration
def countvowels(s):
    count = 0
    for c in s:
        if vowel(c):
            count = count+1
    return(count)
countvowels("hello")

x in s expects x to be a string if s is a string
vowel(7)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[23], line 1
----> 1 vowel(7)
Cell In[18], line 2, in vowel(c)
     1 def vowel(c):
----> 2     return(c in "aeiou")
TypeError: 'in <string>' requires string as left operand, not int
vowel("7")
False
vowel("there")
False
We have seen that list() and int() can be use to convert values from one type to another
Likewise str() converts its argument to a string
Almost any value converts sensibly into a "readable" representation
print(v) implicitly converts v to str(v) to display on screen
str([1,2,3])
'[1, 2, 3]'
str(77)
'77'
Can convert a string to a number if the contents can be intepreted sensibly
int('77')

int('hello')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[29], line 1
----> 1 int('hello')
ValueError: invalid literal for int() with base 10: 'hello'
int('77.5')  # 77.5 is a number, but not an int
In [21]:
In [22]:
Out[22]:
In [23]:
In [24]:
Out[24]:
In [25]:
Out[25]:
In [26]:
Out[26]:
In [27]:
Out[27]:
In [28]:
Out[28]:
In [29]:
In [30]:

---

## Page 7

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[30], line 1
----> 1 int('77.5')  # 77.5 is a number, but not an int
ValueError: invalid literal for int() with base 10: '77.5'
float('77.5')
77.5
float('77')
77.0
In [31]:
Out[31]:
In [32]:
Out[32]: