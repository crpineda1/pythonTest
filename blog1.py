# data types

# String
sentence = 'Hi i am a string'

# Numeric

numberrr = 1 # type int
floatt = 2.1 # type float
complexx = 1j # type complex

# Sequence (list = JS array, tuple = JS set?)
this_list = [1,2,3] #type list (ordered & changable)
this_tuple = (1,2,3) #type tuple (ordered & UNCHANGEABLE) 
this_set = (1,2,3) #type set (unique values only) 

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


# iterate thru loops

for country in countries:
  print(country) # prints each country -> just JS for...in loop
print("this is now outside of loop")

countries = ['Croatia', 'USA', 'Argentina', 'France', 'Brazil', 'Japan', 'Vietnam', 'Israel']

for index in [0,1,2,3,4,5,6,7]:
  print(index)            # prints each number in array
  print(countries[index]) # prints each country (numbers doubles as index)

for x in range(len(countries)):    # range object creates list of numbers from 0(default & optional) to max-1 (same as indices for an array)
  print (x,cities[x],countries[x]) # prints each based on range

print(range(len(countries))) # prints array indices

countries.append('mexico')
cities.append('mexico city')

for x in range(len(countries)):   # range updated to include mexico
  print(x,cities[x],countries[x]) # prints including mexico


# iterate thru dictionary
# python cannot interate direcly thru a dictionary so we need to convert it to a list

example_dictionary = {'first_name': "Terrance", 'last_name': "KOAR", 'favorite_language': "Python"} 
print(example_dictionary) # prints dictionary
print(example_dictionary.items()) #creates list of sets of key,values pairs <- for interation

for key,value in example_dictionary.items(): #creates list with all key/cvalue pairs so you can iterate
  print (key,value)

for key in example_dictionary.keys(): # creates list of keys 
  print (key,example_dictionary[key])  # prints each key and value from dictionary


# functions

new_employees = ['steven', 'jan', 'meryl']

def greet_employees(): # declare function with def (define?)
  welcome_messages = []
  for name in new_employees:
    print name.title()
    welcome_messages.append("Hi "+name.title()+"!")
    print "last line inside for loop"
  return welcome_messages # there is no "end" or closing brackets, function ends when you start new line in same line as "def"
print ("this line is outside the function but before execution")
print greet_employees() #execute/call function 
print ("this line is outside the function and after execution")


# function with logic

def minimumDistances(a):
  map = {}
  results = []
  i = 0                                 # must create i outside for...in loop
  for num in a:
    if str(num) in map:                 # check for existence
      results.append(i-map[str(num)])   # note: variable must be string to search in dict
    else:
      map[str(num)] = i
    i += 1                              # don't forget to increase i
  
  if len(results) > 0:
    return min(results)
  else:
    return -1

print ("expect 3",minimumDistances([7,1,3,4,1,7]))
print ("expect 1",minimumDistances([7,3,3,4,1,7]))
print ("expect 5",minimumDistances([7,2,3,4,1,7]))
print ("expect -1",minimumDistances([9,2,3,4,1,7]))
print ("expect 2",minimumDistances([7,4,3,4,1,7]))

# filter -> takes filtering function and iterable object (list, etc)
# filter ( function, iterable ) -> returns list function with items that match condition 

numbers = [0,1,2,3,4,5]

def above3(n):
  if n>3:
    return True
  else:
    return False

filter(above3,numbers) # returns [4,5]

filter(None,numbers) # returns all truthy values e.g.:[1,2,3,4,5]

