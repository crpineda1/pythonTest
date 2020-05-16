# Python Basics


# String

sentence = 'Hi i am a string'
type(sentence) # return <class 'str'>

# Numeric

num = 1 # type int
type(num) # return <class 'int'>
num = 2.1 # type float
type(num) # return <class 'float'>
num = 1j # type complex
type(num) # <class 'complex'>

# Boolean

boolean = True # type boolean
type(boolean) # return <class 'bool'>

bool(100) # returns True
bool(0) # returns False

# Empty Variables (None type)
var = None
type(var) # return <class 'NoneType'>



# Collections (list = JS array, tuple = JS set?)

this_list = [1,2,3] #type list (ordered/indexed & changable)
type(this_list) # return <class 'list'>
this_tuple = (1,2,3) #type tuple (ordered/indexed & UNchangable) 
type(this_tuple) # return <class 'tuple'>
this_set = {1,2,3} #type set (unique values only) 
type(this_set) # return <class 'set'>

collection = [4,1,2,3,3]
tuple(collection) # return (4,1,2,3,3)
set(collection) # return {1,2,3,4}
list(set(collection)) # return [1,2,3,4]


array[:2] # [1,2] slice # elements (NOT INDEX)

# Mapping (dictionary = JS array)
dictionary = {"name": "John", "age": 30} #type dict


# setup dict from array with keys for dict
# notice dict.fromkeys() - methods not camelcase 🤔
 
this_list = [4, 1, 2, 3, 3]
dict.fromkeys(this_list) # returns {4: None, 1: None, 2: None, 3: None}

unique_words = ['element1','element2','element3']
word_histogram = dict.fromkeys(unique_words,0) # return {'element1': 0, 'element2': 0, 'element3': 0}

list_of_lyrics = ['element1','element2','element3','element1','element2','element1']

# for loop (same as JS for...in loop)
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

name.strip() # removes leading and trailing spaces (same as JS trim) or chaacters specified
name.strip('hn') # returns "omer simpso" (leading h & trailing n removed)

help(str) #more info on strings and methods (in terminal while running python engine)


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
  return -1 if len(results) == 0 else min(results) # ternary <result 1><if condition><result 2/else>

print ("expect 3",minimumDistances([7,1,3,4,1,7]))
print ("expect 1",minimumDistances([7,3,3,4,1,7]))
print ("expect 5",minimumDistances([7,2,3,4,1,7]))
print ("expect -1",minimumDistances([9,2,3,4,1,7]))
print ("expect 2",minimumDistances([7,4,3,4,1,7]))

# filter -> applies filtering function to each element in iterable object (list, etc)
# filter ( function, iterable ) -> returns list with elements that match condition 

numbers = [0,1,2,3,4,5]

def above3(n):  # filter function
  if n>3:
    return True
  else:
    return False

filter(above3,numbers) # returns [4,5]
filter(None,numbers) # returns only truthy values e.g.:[1,2,3,4,5]


# map -> applied function to modify each element iterable object
# map(Function, Sequence) -> returns same size list with modified elements

names = ['Homer', 'Marge', 'Bart', 'Maggie', 'Lisa']

def addSimpson(str):           # fucntion to modify elements 
  return str + " Simpson"

print map(addSimpson,names) # returns ['Homer Simpson', 'Marge Simpson',...]
print map(None,names) # returns unmodified list
print map(list,names) # returns "listified" (split strings to lists) elements  (list of lists) e.g.: [['H', 'o', 'm', 'e', 'r'], ['M', 'a', 'r', 'g', 'e'],...]


# lambda custom functions
# when you need a quick & simple modification that doesn't need an formal function (similar to JS anonymous function () => {})

numbers = [1, 3, 8, 9, 11, 20]

def addfive(num):
  return num + 5

print map(addfive,numbers)
print map(lambda x: x+5,numbers)

from restaurants import yelp_restaurants   # import data from restaurants.py (adjacent file)

restaurants = map(lambda restaurant: dict(name = restaurant["name"],          # create a list of restaurant objects (type dict) with only info we want
                                          price = restaurant["price"], 
                                          is_closed = restaurant["is_closed"], 
                                          review_count = restaurant["review_count"]),
                                          yelp_restaurants)                           # ref imported list from restaurants.py


print restaurants  # prints new list of restaurants 
