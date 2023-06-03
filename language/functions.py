
# ------------------
# Functions
# ------------------

# Functions are a fundamental building block of most python programs.

# Functions are defined with def statement

def add(x, y):
    return x + y

# ------------------
# Default arguments
# ------------------

def split(line, delimiter=','):
    # statements

# The parameter with default value and all the paramenters that follow
# are optional. It is not posible to specify a parameter with no default
# value after any parameter with a default value.

# NOTE: only use immutable objects for default argument values
# numbers, strings, booleans, None...
# def func(val, items=[]): <------------- NO

def func(val, items=None):
    if items is None:
        items = []
    items.append(val)
    return items

# ------------------
# Variadic arguments
# ------------------

# a function can accept a variable number of arguments
# if an * is used as a prefix on the last parameter name.

def product(first, *other):
    result = first
    for x in other:
        returns = result * x
    return result

product(10, 20)  # -> 200
product(2, 3, 4, 5) # -> 120

# ------------------
# Keyword arguments
# ------------------

# function arguments can be supplied by explicitly naming each
# parameter and define a value.
# To force this listing parameters after * argument or just
# by including a single * in the definition.
def read_data(filename, *, debug=False):
    #...

def product(first, *values, scale=1):
    # ...

read_data('data.csv', debug=True)
product(2, 3, scale=3)

# ------------------
# Variadic keyworkd arguments
# ------------------

# if the last argument is prefixed with **, all the additional kw ars
# are placed in a dictionary and passed to the function.
def make_table(data, **params):
    fgcolor = params.pop('fgcolor', 'black')
    bgcolor = params.pop('bgcolor', 'white')

    # something

make_table(items, bgcolor='gray')

# ------------------
# Functions with all inputs
# ------------------

# By using * and **, you can write a function that accepts any combination
# of arguments.
def func(*args, **kwargs):
    # ...

    
# ------------------
# Doc, Name and Annotations
# ------------------

def factorial(n: int) -> int:
    """
    Computes n factorial. For example:

    >>> factorial(6)
    120
    >>>
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# The name of a function can be obtained via the `__name__` attr.
# This is useful for debugging.
print(factorial.__name__)

# It is common for the first statement of a function to be a doc string.
# Is stored on the `__doc__` attr
print(factorial.__doc__)

# Functions can also be annotated with type hints.
# Third party tools and code checkers migh use hints.
print(factorial.__annotations__)

# ------------------
# The lambda Expression
# ------------------

# Anonymous - unamed - function can be defined with a lambda expression:

# lambda args: expression
# args is a comma separated list of arguments.
# expression is an expression involving this args.

a = lambda x, y: x + y
r = a(3, 5)  # 8

# One of the main uses of lambda is to define small cb functions.
result = sorted(words, key=lambda word: len(set(word)))

# ------------------
# High Order Functions
# ------------------

# Functions can be passed as arguments, placed in data structures and
# returned by other functions.

def after(seconds, func):
    time.sleep(seconds)
    func()

def greeting():
    print("Hello, World")

after(10, greeting)  # prints "Hello, World" after 10 seconds

