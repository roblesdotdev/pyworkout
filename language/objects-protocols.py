
# -------------------------------------
# Object Identity and Type
# -------------------------------------

# The built-in function id() returns the identity of an object. The identity is 
# an integer that usually corresponds to the object’s location in memory. The is 
# and is not operators compare the identities of two objects. type() returns the 
# type of an object. 

def compare(a, b):
    if a is b:
        print('Same object')
    if a == b:
        print('Same value')
    if type(a) is type(b):
        print('Same type')


# A subtype is a type defined by inheritance. It carries all of the features of the 
# original type plus additional and/or redefined methods. 

items = list()

if isinstance(items, list):
    items.append('foo')


class MyList(list):
    def removeall(self, val):
        return [i for i in self if i != val]


items = MyList([1, 2, 2, 3, 4, 2])
x = items.removeall(2)
print(x)

# -------------------------------------
# None for Optional or Missing Data
# -------------------------------------

# Sometimes programs need to represent an optional or missing value. None is a special 
# instance reserved for this purpose. None is returned by functions that don’t 
# explicitly return a value. None is also frequently used as the default value of 
# optional arguments, so that the function can detect whether the caller has actually 
# passed a value for that argument. None has no attributes and evaluates to False in 
# Boolean expressions.

def foo(value = None):
    if value is None:
        # some stuff
        pass


# -------------------------------------
# Object Protocol
# -------------------------------------

# Methods related to object initialization, destruction, and representation.

# __init__(self [*args [,**kwargs]])

# __del__(self)

# __repr__(self)

# The __repr__() method, called by the built-in repr() function, creates a string 
# representation of an object that can be useful for debugging and printing.


# -------------------------------------
# Comparison Protocol
# -------------------------------------

# __bool__(self)        -> truth-value testing

# __eq__(self, other)   -> self == other


# -------------------------------------
# Conversion Protocol
# -------------------------------------

# __str__(self)       

# __int__(self)

# __float__(self)


# -------------------------------------
# Container Protocol
# -------------------------------------

# __getitem__(self, key)          -> self[key]
 
# __setitem__(self, key, value)   -> self[key] = value

# __delitem__(self, key)          -> del self[key]

# __contains__(self, obj)         -> obj in self






