  

if 1==2:
  print("this is true")
elif 1==1:
  print("this is equal")
else:
  print("this is false")

x = 0
while x < 3:
  print('X is currently {}'.format(x))
  print('still less than 3, add 1 to x')
  x += 1
  print("\n")

print('Welcome Agent')
passcode = 0

while passcode != 123:
  passcode  = int(input('Please provide passcode:')) # string input default, must specify integer

  if passcode !=123:
    print('WRONG')
    print('TRY AGAIN')

print("ACCEPTED")


x = 0

while x <10:
  print(x)
  x = x+1

  if x==3:
    print ("break")
    break


tup = (1,2,3,4,5)

for n in tup:
  print('tup',n)

list_of_tups = [(1,2),(3,4),(5,6)]
for x,y in list_of_tups: # tuple unpacking (for output of other data stuctures)
  print('list tuple',x)
  # print(y)
  print('\n')

d = {'a':1,'b':2,'c':3}
for key,value in d.items():
  print('dict key ', key)
  print('dict value ', value)

for k in d:
  print('key', k)
  print('value',d[k])

for num in range(0,11,2): # range of #s (start,non-inclusive end, skip)
  print(num) 

print(list(range(0,11))) # prints list of nums

index = 0
for letter in 'abcde':
  print('At index {} the letter is {}'.format(index,letter))
  index += 1

for index,letter in enumerate('abcde'): # assigns an index to string/list/etc
  print('At index {} the letter is {}'.format(index,letter))

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

for item in zip(mylist1,mylist2): #creates tuple of pairs of both lists (like a zipper)
  print(item)

print(3 in [1,2,4])
print(2 in (1,2,3))
print('a' in {'a':1,'b':2})
print(1 in {'a':1,'b':2})

from random import shuffle



mylist = [1,2,'c','e']
print(mylist)
shuffle(mylist) # in place shuffle items in list
print(mylist)
shuffle(mylist)
print(mylist)
shuffle(mylist)
print(mylist)

from random import randint
randint(0,100) # generates random int 0-99
print(randint(0,100))
print(randint(0,100))
print(randint(0,100))
print(randint(0,100))
print(randint(0,100))
print(randint(0,100))

print( 1 == 1 and 2 == 2)
print( 1 == 1 or 2 == 2)
print( 1 != 1 and 2 != 2)
print( 1 != 1 or 2 != 3)



