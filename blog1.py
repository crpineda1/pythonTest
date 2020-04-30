# data types

# String
sentence = 'Hi i am a string'

# Numeric

numberrr = 1 # type int
floatt = 2.1 # type float
complexx = 1j # type complex

# Sequence (list = JS array, tuple = JS set?)
array = [1,2,3] #type list
tuplee = (1,2,3) #type set (unique values only) 

array[:2] # [1,2] slice # elements (NOT INDEX)

# Mapping (dictionary = JS array)
dictionary = {"name": "John", "age": 30} #type dict


# setup dict from array with keys for dict
# notice dict.fromkeys() is not camelcase 🤔  


unique_words = ['element1','element2','element3']
word_histogram = dict.fromkeys(unique_words,0)

list_of_lyrics = ['element1','element2','element3','element1','element2','element1']

# for loop (for...in loop)
# hash map - increase word count in dict per occurence  
for word in list_of_lyrics:
  word_histogram[word] = word_histogram[word] + 1

# find the type of of a data type
type('string') # str

# strings
name = "homer simpson" # no need for str??
name.upper() #  'HOME SIMPSON'
'smithers'.capitalize() # 'Smithers'
'hello world'.title() # 'Hello World'

name.endswith('simpson') # true
'charles burns'.endswith('simpson') # false

name.replace('o','0') # 'H0mer Simps0n'

name[:3] # 'geo' -> slice # of characters (same with list)

help(str) #more info on strings and methods (in terminal while running python engine)

# numbers

type(10) # int
type(10.2) #float

# booleans
print bool(100) # True
print bool(0)   # False

# assign empty variable
address = None

# lists

countries = ['Croatia',
 'USA',
 'Argentina',
 'Mexico',
 'USA',
 'Morocco',
 'USA',
 'Finland',
 'Argentina',
 'Italy',
 'Canada',
 'South Korea', 
 'Malta', 
 'Thailand'
]

countries.pop() # 'Thailand' <-  JS pop

countries.index('USA') # 1j <- JS indexOf

unique_countries = set(countries) # creates set w/unique elemeents

len(countries) # 13 <- length function to count elements
len(unique_countries) # 10 <- length function to count elements



