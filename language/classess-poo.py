
# ----------------------------------------
# Classess
# ----------------------------------------

# New objects are defined using the class statement. A class typically consists
# of a collection of functions that make up the methods.

class Account:
    '''
    A simple bank account
    '''
    owner: str
    balance: float

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f'Account({self.owner!r}, {self.balance!r})'

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount


# The functions defined inside a class are known as methods. An instance method is 
# a function that operates on an instance of a class, which is passed as the first
# argument(self).

# The __init__() and __repr__() methods are special or magic methods. The __init__
# is used to initialize state when new instance is created. The __repr__ methods 
# returns a string representation of the class.

# Instances: created by calling the object class as a function.

a = Account('Guido', 1000.0)
b = Account('Eva', 100.0)

# methods of the class are accessing using the dot(.) operator

a.deposit(100.0)
b.withdraw(20.0)

# It's important to emphatize that each instance has its own state.
print(vars(a))
print(vars(b))

# ----------------------------------------
# Operator Overloading and protocols
# ----------------------------------------

class AccountPortfolio:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __len__(self):
        return len(self.accounts)

    def __getitem__(self, index):
        return self.accounts[index]

    def __iter__(self):
        return iter(self.accounts)


port = AccountPortfolio()
port.add_account(a)
port.add_account(b)

print(len(port))  # 2

for account in port:
    print(account)

# ----------------------------------------
# Inheritance
# ----------------------------------------

# Inheritance is a mechanism for creating a new class that specializes or modifies 
# the behavior of an existing class. The original class is called a base class, 
# superclass, or parent class. The new class is called a derived class, child class, 
# subclass, or subtype. When a class is created via inheritance, it inherits the 
# attributes defined by its base classes. However, a derived class may redefine 
# any of these attributes and add new attributes of its own.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f'Account({self.owner!r}), {self.balance!r})'


class EvilAccount(Account):
    def __init__(self, owner, balance, factor):
        super().__init__(owner, balance)
        self.factor = factor

    def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.factor * super().inquirity()
        else:
            return super().intuirity()


# ----------------------------------------
# Inheritance VS Composition
# ----------------------------------------

# One concern with inheritance is what’s known as implementation inheritance. 
# To illustrate, suppose you wanted to make a stack data structure with push 
# and pop operations. A quick way to do that would be to inherit from a list 
# and add a new method to it:

class Stack(list):
    def push(self, item):
        self.append(item)

# s = Stack()
# s.push(1)
# s.push(2)
# s.pop() 

# Sure enough, this data structure works like a stack, but it also has every other 
# feature of lists—insertion, sorting, slice reassignment, and so forth. This is 
# implementation inheritance—you used inheritance to reuse some code upon which 
# you built something else, but you also got a lot of features that aren’t pertinent 
# to the problem actually being solved. Users will probably find the object strange. 
# Why does a stack have methods for sorting?

# A better approach is composition. Instead of building a stack by inheriting from 
# a list, you should build a stack as an independent class that happens to have a 
# list contained in it. The fact that there’s a list inside is an implementation 
# detail.

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)



# ----------------------------------------
# Static Methods
# ----------------------------------------

# A static method is just a ordinary function that happens to be defined inside a class.

class Ops:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def mul(x, y):
        return x * y

# Ops.add(3, 4)
# Ops.mul(3, 3)

# ----------------------------------------
# Properties
# ----------------------------------------

# A property is a special kind of attribute that intercepts attribute access and 
# handles it via user-defined methods.

class SomeClass:
    @property
    def a(self):
        print('Getting a')

    @property.setter
    def a(self, value):
        print('Setting a', value)

    @attr.deleter
    def a(self):
        print('Deleting a')


# s = SomeClass()
# s.a          # Getting a
# s.a = 13     # Setting a 13
# del s.a      # Deleting a


