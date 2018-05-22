print("Hello, world")

cow = "moo"
dog = "woof"
# print(cow)

# if(fjfhf) {

# } else {

# }

# This is an if else
if cow == "moo" and dog == "woof":
  print(cow)
elif cow == "Woof":
  print("WTF?")
else:
  print ("The end")

print( "A cow says {0}. A dog says {1}".format(cow, dog))

num = 3
num_str = "3"
#print( num + num_str) #Throws error
print( str(num) + num_str) #Throws not error
print( num + int(num_str)) #Throws not error

# collections
# objects and arrays are no more
# lists, tuples, sets, dictionaries

# list
# mylist = [] or list()
junkbox = ["scissors", 3, True, {"key": "value"}]
print(junkbox[1])
junkbox.append("more shit")
print(junkbox)
junkbox.extend([456, False])
# or
junkbox += ["longer", 3.78, "wow!"]
print(junkbox)
del(junkbox[2])

# len(list_name) gives you the length

# Slicing is done like this
# new_list = old_list[2:5]
# gives you the 2nd through 4th indexes(so, from index 2 UP TO 5)

# set must contain unique items
myset = set()
unique_list = {"scissors", 3, True}
print(unique_list)
unique_list.add("monkey")
print(unique_list)
unique_list.add(3)
print(unique_list)

# tuples are immutable
zoo = ("dog", "monkey", "chicken", "bird", "cuttlefish")
print(zoo[3])
zooList = list(zoo)
zooList.extend(["python", "bat", "mongoose"])
zoo = tuple(zooList)
print(zoo)
# del(zoo[3]) Throws error

# dictionaries
foo = {}
foo["name"] = "Fred"
print(foo)

foo["nested_vals"] = { "name": "Larry", "age": 45}
print(foo)
print("nested vals!!!", foo["nested_vals"]["age"])

# loops
for junk in junkbox:
  print(junk)

# for animal in zoo:
#   for junk in junkbox:
#     print( "I like {0}s and {1}s".format(animal, junk))

# Looping through a dictionary
# for x in foo.keys()
# for x in foo.values()
# for x, y in foo.items() <— gives you both keys and values(note 2 vars)

# functions
def do_something(foo="monkeys"):
  if foo == "monkeys":
    print("I like " + foo)
    return
  print("Something else " + foo)

do_something("chickens")
do_something()