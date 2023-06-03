# ----------------------------------
# GENERATORS
# ----------------------------------

# If a function uses the 'yield' keyword, it defines an object known as a generator.
# The primary use of generator is to produce values for use in iterators.

def countdown(n):
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1


for x in countdown(10):
    print('T-minus', x)


# You normally don’t call next() on a generator directly, but use the for 
# statement or some other operation that consumes the items.

# A generator function produces items until it returns. This raises a 
# StopIteration exception that terminates a for loop.

# >>> next(c)
# Counting down from 10
# 10
# >>> next(c)
# 9

# ----------------------------------
# Restartable generators
# ----------------------------------

# Normally a generator function executes only once. If you want an object that
# allows repeated iteration, define it as a class and make the `__iter__` method
# a generator:

class countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1


