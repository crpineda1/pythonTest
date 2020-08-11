print('hello world')

sentence = "abcdefghijklmnopqrxtuvwxyz"

sub1 = sentence[0]
sub2 = sentence[0:2]
sub3 = sentence[:2]
sub4 = sentence[4:]

sub5 = sentence[0:26:2]
sub6 = sentence[1:26:2]

print(sub1)
print(sub2)
print(sub3)
print(sub4)
print(sub5)
print(sub6)

print(sentence.upper())

msg = "hello world"
print(msg.split())
print(msg.split('o')) # specify split 

user_name = 'recruit'
action = 'run'
print('the {} needs to {}'.format(user_name,action))
print('the {a} needs to {b}'.format(a=user_name,b=action)) #specify which one
print('the {b} needs to {a}'.format(a=user_name,b=action)) #specify w/order

num = 123.45678
print('the code is {}'.format(num))
print('the code is {:.2f}'.format(num)) #round 2 decimals

my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5) #immutable - for info that shouldn't be changed (usernames, dates, etc)
# fun fact - items of dictionaries ("dict.items()") returns list of tuples since info cannot be changed e.g.: dict.items([('a',1),('b',2)])

my_list[2] = 6
# my_tuple[2] = 6 # type error
my_list.append(6)
# my_tuple.append(6) # type error

print(my_list)
print(my_tuple)

my_set = set()
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_set.add(1)
print(my_set)

myfile = open('test_file.txt')
line = myfile.read() # returns contents in one line
print("read1",line)

myfile.seek(0) # sends reader to position 0 (beginning of file)
lines = myfile.readlines() # returns contents as a list with each line as an element
print("read2",lines)
myfile.close() # must close to python doesn't keep open

with open('test_file.txt') as myfile: # can set diff modes (write, write binary, etc)
  text = myfile.read()
  myfile.seek(0)
  text1 = myfile.readlines()
print("read3",text)
print("read4",text1)

with open('test2.txt', mode='w') as file2: # overwrites file
  file2.write('written line')
with open('test2.txt') as file2:
  new_lines = file2.read()
print("read5",new_lines)

