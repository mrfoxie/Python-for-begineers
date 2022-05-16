#!/usr/bin/env python3
# We will ask user there birth year, and then we will calculate it so that we can find out how old the user is.

birth_year = input('Birth year: ')
age = 2022 - birth_year
print(age)

# Well if you have run the program then you have got error like below
# Birth year: 1997
# Traceback (most recent call last):
#   File "./06. Fun Time.py", line 5, in <module>
#     age = int(2022) - birth_year
# TypeError: unsupported operand type(s) for -: 'int' and 'str'

# this is because that we can't subtract integer with sting value so what we will do is we will wrap birth_year with int function, and you will get like this.
# int(birth_year)

# your new code will be look like this
# you can comment above code to make this run properly
birth_year = input('Birth year: ')
# Here you can add type command to check what kind of output does birth_year give you in the print statement
# just uncomment the line and check it
# print(type(birth_year)) # it will allow you to see what kind of output is it whether it's a str or int
age = 2022 - int(birth_year)
# print(type(age))
print(age)
