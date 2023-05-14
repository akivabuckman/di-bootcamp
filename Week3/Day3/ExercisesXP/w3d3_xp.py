# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.
#
# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look
# at the doc method on google for help.

def xp1():
    class Number:
        """this is the documentation for the class"""

        def __init__(self, value):
            """this is the documentation for the __init__ method"""
            self.value = value

        def __abs__(self):
            return abs(self.value)

        def __int__(self):
            return int(self.value)

    example = Number(-3.6)
    print(abs(example))
    print(int(example))
    print(Number.__doc__)
    print(Number.__init__.__doc__)


# 🌟 Exercise 2: Currencies
# Instructions
#
#
# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
#
# >>> str(c1)
# '5 dollars'
#
# >>> int(c1)
# 5
#
# >>> repr(c1)
# '5 dollars'
#
# >>> c1 + 5
# 10
#
# >>> c1 + c2
# 15
#
# >>> c1
# 5 dollars
#
# >>> c1 += 5
# >>> c1
# 10 dollars
#
# >>> c1 += c2
# >>> c1
# 20 dollars
#
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>


def xp2():
    class Currency:
        def __init__(self, currency, amount):
            self.currency = currency
            self.amount = amount

        # Your code starts HERE

        def __str__(self):
            return f"{self.amount} {self.currency}s"

        def __int__(self):
            return int(self.amount)

        def __repr__(self):
            return f"{self.amount} {self.currency}s"

        def __add__(self, other):
            if isinstance(other, Currency):
                if self.currency != other.currency:
                    raise TypeError(f'Cannot add between Currency type {self.currency} and {other.currency}')
                else:
                    return self.amount + other.amount

            else:
                return self.amount + int(other)

        def __iadd__(self, other):
            if isinstance(other, Currency):
                if self.currency != other.currency:
                    raise TypeError('Cannot add between Currency type <dollar> and <shekel>')
                else:
                    self.amount += other.amount
                    return self

            else:
                self.amount += other
                return self

    c1 = Currency('dollar', 5)
    c2 = Currency('dollar', 10)
    c3 = Currency('shekel', 1)
    c4 = Currency('shekel', 10)

    print(str(c1))
    print(int(c1))
    print(repr(c1))
    print(c1 + 5)
    print(c1 + c2)
    print(c1)
    c1 += 5
    print(c1)
    c1 += c2
    print(c1)
    print(c1 + c3)

xp1()
xp2()
