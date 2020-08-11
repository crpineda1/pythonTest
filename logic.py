  

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

