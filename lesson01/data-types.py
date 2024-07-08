# String data types

# Literal assignment

first = "John"
last = "Adesiyan"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function

laptop = str("dell")
print(type(laptop))
print(type(laptop) == str)
print(isinstance(laptop, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"

# casting a number to a string
year = str(1996)
print(type(year))

statement = "I love music from the " + year + "s."
print(statement)

# multiple lines
multilines = '''
Hey, John is learing python     

And he wants to be a backend dev   eloper too          
                                          Awesome guy!
                                          
'''

print(multilines)

# escaping special characters

message = "Hey today July 3rd 2024, it's raining! \t And i'm working on my pc \n\nGod's love!!"
affirmation = 'Money comes to me easily and i\'m blessed everyday.\t \nGod is good!'
print(message)

# String method

print(first.lower())
print(first.upper())

print(affirmation.replace("everyday", "all day"))
print(affirmation.title())
print(affirmation)

print(len(affirmation))
multilines += "                    "
multilines = "           " + multilines
print(len(multilines))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "*"))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Cake".ljust(16, ".") + "$3".rjust(5))
print("Salad".ljust(10, ".") + "$10".rjust(9))

# String index value
print(first[0])
print(first[-1])
print(first[0:])
print(first[1:-1])

# Some method return boolean data
print(first.startswith("J"))
print(first.endswith("p"))

# Boolean data type
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

# Numeric data types

# Integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.915
y = float(1.14)
print(type(gpa))


# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in function for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1  ))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number
zipcode = "10001"
zipCode = int(zipcode)
print(type(zipCode))

