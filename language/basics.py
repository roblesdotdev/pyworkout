# -----------------------------------
# Primitives
# -----------------------------------

print(42)    # int
print(3.14)  # float
print('foo') # str
print(True)  # bool

# -----------------------------------
# Variables
# -----------------------------------

# A variable is a name that refers to value.
# identifier = value

price = 15.0
price_typed: float = 233.50

discount = 0.2

# A expression is a combination of primitives, names, and 
# operators that produces a value.

result = price * (1 - discount)

print(result)

# -----------------------------------
# Aritmetic Operators
# -----------------------------------
# +, -, *, /, //, **, %, -x, +x

# the division / produces a floating point
# the floor division // truncates the result to an integer
# the modulo % returns the remainder of the floor division.

# Commonly used numerical functions

print("abs(-3): ", abs(-3))
print("divmod(12, 2): ", divmod(12, 2))
print("pow(2, 5): ", pow(2, 5))

# Compare numbers with the operators: ==, !=, <, <=, >, >=
# The result of comparison returns a Boolean: True or False
print(3 == 4)

# The 'and', 'or' and 'not' operators can form more complex Boolean expressions.
print(1 == 1 and 33 > 5)

# -----------------------------------
# Conditionals and Control Flow
# -----------------------------------

# The 'while', 'if' and 'else' statements are used for looping and conditional code exec.
a = 32
b = 33
if a > b:
    print("Computer says yes")
else:
    print("Computer says no")

# If you are assigning a value in combination with a test, use a conditional expression.
maxval = a if a > b else b
print(maxval)

counter = 0
while counter < 10:
    if counter == 5:
        # pass -> do nothing
        # continue -> next iteration
        break  # exit
    print(counter)
    counter += 1

# -----------------------------------
# Text Strings
# -----------------------------------

# To define a string literal, enclose it in single, double, or triple quotes

# Strings are stored as sequences of unicode characters index based zero.
a = 'Hello World'
print(len(a))
print(a[0])
print(a[-1])

# To stract a substring, use the slicing operator s[i:j]. from i to j-1
print(a[:5])
print(a[6:])

# F Strings
firstname = "John"
lastname = "Doe"

fullname = f"{firstname} {lastname}"

print("Welcome " + fullname)

# Templates
fname = "{} {}".format(firstname, lastname)

print(fname)

# Common string methods

# s.endswith(prefix [,start[,end]])
# s.find(sub [, start[, end]])
# s.lower()
# s.replace(old, new)
# s.split([separator])
# s.startswith(prefix)
# s.strip([chars])
# s.upper()

# Strings are concatenated with te + operator
print("Hello" + " " + "World")

# -----------------------------------
# Lists
# -----------------------------------

# Lists are an ordered collection of arbitrary objects.
names = ['Bob', 'John', 'Tom']

# Indexed by integers zero based
bob = names[0]    # get the first
names[1] = 'Jane' # Change the second item to 'Jane'
print(names[-1])  # print the last

# Add new item to the end of a list
names.append('Mary')

# Insert a item in the list at a specific position
names.insert(2, 'Gaby')

# Iterates over a list
for name in names:
    print(name)

# An empty list is created with
l1 = []      # common
l2 = list()  # used to performing convertions

# -----------------------------------
# Tuples
# -----------------------------------

# you can pack a collection of values into an immutable object known as tuple.
colors = ('red', 'green', 'blue')
fullname = ('John', 'Doe')
one = (1,)  # trailing comma
empty = ()

# unpack tuples
red, green, blue = colors

# -----------------------------------
# Sets
# -----------------------------------

# A set is an unordered collection of unique objects. 
# Sets are used to find distinct values or to manage problems related to membership. 
empty = set()
names1 = { 'IBM', 'AA' }
names2 = set(['IBM', 'AA', 'IBM', 'CAT'])

# Sets support a standard collection of operations including union, intersection,
# difference, and symetric-difference

# t | s -> union
# t & s -> intersection
# t - s -> difference
# t ^ s -> symetric difference

# common methods

t = set()
t.add('DIS')  # add item
t.update({'JJ', 'AA', 'DIS'}) # add multiple items
t.remove('AA')  # remove or raise KeyError
t.discard('ZZ') # remove if exists

print(t)

# -----------------------------------
# Dictionaries
# -----------------------------------

# Mapping key:value
s = {
        'name': 'Bob',
        'age': 33
    }
sname = s['name']
sage = s['age']

# Insert or modify
s['admin'] = True

# Test membership
if 'admin' in s and s['admin'] == True:
    print('s is admin')

# Safe get value
s.get('admin', False)   # if 'admin' in s else False

# Remove element from dict
del s['admin']

# Create empty dict
ed1 = {}    # for empty set use set()
ed2 = dict()

# s.keys()   -> get list of keys
# s.values() -> get list of values
# s.items()  -> get key-value pair

for k, v in s.items():
    print(f"{k} -> {v}")

# -----------------------------------
# Iteration and Looping
# -----------------------------------

# for statement is used to iterates over a collection of items.
lst = [1, 2, 3]
for n in lst:
    print(f"n in lst -> {n}")

# The range function creates an object that represents a range of integers
# range(i, j [,step])  -> from i up to, but not including, j.

for i in range(1, 4):
    print(f"i in range(1, 4) -> {i}")

dct = { 'name': 'John', 'age': 33 }
for k, v in dct.items():
    print(f"{k} -> {v}")

# -----------------------------------
# Operations with iterables
# -----------------------------------

# - looping with for
# - unpacking variables
# - member check(in, not in)
# - expansion(list, tuple, set)  [lst1, *lst2]

# A variety of built-in functions accept any iterable as input.

# list(s)   -> create a list from s
# tuple(s)  -> create a tuple from s
# set(s)    -> create a set from s
# min(s)    -> min item in s
# max(s)    -> max item in s
# any(s)    -> return True if any item in s is true
# all(s)    -> return True if all items in s are true
# sum(s)    -> sum items
# sorted(s) -> create a sorted list

