# Syntax in python 

print("Hello, World")

# How to print a single or a doublr quotation marks in the statement

# print("Hello my all "Friends" ") #SyntaxError: invalid syntax. Is this intended to be part of the string
# To Solve this =>>  Use sinlge quotationa nd than use double quotaion in the statement or vice versa or use can also use escape technique

# print('Hello my all "Friends"') # Output will be => Hello my all "Friends"
# print("Hello EveryOne in this 'Community'") # Output will be => Hello EveryOne in this 'Community' 
# print("This statement use \"Escape Technique\"") # Output will be => This statement use "Escape Technique"

# Get input from user side 

# input("Enter anything ? ")

# Variable in python

"""

name = input("What's your name ? ")
print (name)

"""
# Print the value of taken input

"""
age = ("What's your age ? ")
print("your enter age is : " , age)

"""

# Coortination in python

"""
Edu = input("What's your Qualification ? ")
print ("Your Qualification is :  " + Edu)

"""

# Latest way to access multiple variables in a single print statement

"""

location = input("Where you from ? ") # let i just enter the location Sahiwal
# print("you are from {location}") # Output will be => you are from ${location}

# Format (F) string the new feature in Python programming Add f just after opening the parenthesis 

print(f"you are from {location}") # Output will be => you are from Sahiwal

"""

# END variable in Python

# program = input("What's your Dept. : ")

# There are 2 Senirio in end values 

#1. end="/n" => Break the line and Moves to the next line  

"""
print("your Dept. is : ", end="\n") 
print(program) 

# Output will be 
What's your Dept. : SE
your Dept. is : 
SE

"""
# 2. end="" => Continue on the same line =>  Working on the same line even multiple console happening

"""
print("your Dept. is : ", end="") 
print(program)

# Output will be 
What's your Dept. : SE
your Dept. is : SE

"""
# Documentation = docs.python.org/3/library/functions.html#print