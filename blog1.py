# data types

# String
str sentence = 'Hi i am a string'

# Numeric

int number = 1
float floatt = 2
complex complexx = 1j

# Sequence (list = JS array, tuple = JS set?)
list array = [1,2,3]
tuple tuplee = (1,2,3) #not sure why this would be useful over a list 

# Mapping (dictionary = JS array)
dict dictionary = {name: "John", age: 30}


# setup dict from array with keys for dict
# notice dict.fromkeys() is not camelcase 🤔  


list unique_words = ['element1','element2','element3']
word_histogram = dict.fromkeys(unique_words,0)


# for loop (for...in loop)
# hash map - increase word count in dict per occurence  
for word in list_of_lyrics:
  word_histogram[word] = word_histogram[word] + 1

