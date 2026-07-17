"""           """"""      Data Types in Python      """"""

               """"""""""""""""  01 Strings      """"""""""""""""


1.  Str == >> String in Python => docs.python.org/3/library/stdtypes.html#string-methods


"""
# name = input("Enter your Full Name : ") # I just do => Enter your Full Name : Asif              Nawaz  
# print(f"Your full Name is : {name}") # Output will be => Your full Name is : Asif              Nawaz 

"""

####   STRIPE METHOD ####

Point to be Noted as like i just add the spaces same retun in the output which is really Ugly to see in Database
to remove white spaces from the string we use the string buikt in method stripe

# Input = > Enter your Full Name :           Asif             
# Output = > Your full Name is : Asif

####     Capitalize METHOD  ####

Only first later of the statement becoe capital 

# Input => Enter your Full Name : asif nawaz
# Output => Your name is : Asif nawaz

####     TITLE METHOD   ####

First letter of each word become capital 

# Input => Enter your Full Name : asif nawaz jutt
# Output => Your name is : Asif Nawaz Jutt

"""
# name = name.strip() # Remove white  spaces from the leftand right of the string 
# print(f"Your full Name is : {name}")

# name = name.capitalize()
# print(f"Your name is : {name}")

# name = name.title() # Input =>  Enter your Full Name : asif nawaz jutt
# print(f"Your name is : {name}") # Output => Your name is : Asif Nawaz Jutt

"""
Combine multiple methods on the same line
=> To combine multiple methods on the same line we use .strip().title().capitalize() and so on

"""
# name = name.strip().title()
# print(f"Your Name is : {name}")

"""
One anOther way is to Perform/Apply all the methods on the time when we try to get an Input this is probably ugly 
when the statement is too long

"""

# hobby = input("What's your hobby Dear One ? ").strip().title() # Input => What's your hobby Dear One ?   footBall , cricket , badminton      
# print(f"Your hobby is : {hobby}") # Output => Your hobby is : Football , Cricket , Badminton

"""
Split => split is a method to break a main into sub strings just like suppose we get user nam eand than 
split/break it into First Name and Last Name 

"""

# fatherName = input("Enter Your Father Name : ") # Input => Enter Your Father Name : Haq Nawaz
# first , last = fatherName.split(" ") # Applied split method to Break complete string into subStrings
# print(f"First Name of Your Father is : {first}") # First Name of Your Father is : Haq
# print(f"Last Name of Your Father is : {last}") # Last Name of Your Father is : Nawaz
# print(f"First Name of Your Father is : {first} and Last Name is : {last}") # First Name of Your Father is : Haq and Last Name is : Nawaz

"""

# #               """"""""""""""""     02    Integer       """"""""""""""""



# # int => Integer in Python => Work woth numbers without using instead of decimals
 

# + => Use for Sum or Addition of values
# - => Use for Substruction or Sub of values
# * => Use for Multiplications of values
# / => Use for Devision of values
# % => Use for Use to find module or Remainder of values


"""

c = 10 # Input 01
d = 5  # Input 02

# s = c + d # Output => Addition of Inputs ===>> 15
# s = c - d # Output => Substruction of Inputs ===>> 5
# s = c * d # Output => Multiplication of Inputs ===>> 50
# s = c / d # Output => Devisio of Inputs ===>> 2
s = c % d # Output => Module of Inputs ===>> 0

print(f"Your Result is = {s}")

"""

# **********************    Values taken by User and than perform Operators    **********************

""" 

x = input("Enter value of x : ") # Input => 112
y = input("Enter value of y : ") # Input => 3
z = x + y # Add both x and y
print(f"The sum of values is {z}") # Output => 1123 => This is bcz the concatination of string it's takes values as string not as integer

"""
#  ***********      Solution # 01     ***********

"""
x = input("Enter value of x : ") # Input => 112
y = input("Enter value of y : ") # Input => 3
z = int(x) + int(y) # Add both x and y as an integer
print(f"The sum of values is {z}") # Output => 115 => Which is correct bcz we use int data type to make sure it's integer not string

#  ***********      Solution # 02  (Recomanded)     ***********

x = int(input("Enter value of x : ")) # Input => 12  => Get input as an integer when user pass a value
y = int(input("Enter value of y : ")) # Input => 3 => Get input as an integer when user pass a value
z = x + y  # Add Both Values 
print(f"The sum of values is {z}") # Output will be => 15 

"""

# ******************     Arithmatic Operators     ******************

"""

a = int(input("Enter Your First Number : ")) # Input 01
b = int(input("Enter Your Second Number : ")) # Input 02

# r = a + b # Output => Addition of Inputs ===>> 15
# r = a - b # Output => Substruction of Inputs ===>> 5
# r = a * b # Output => Multiplication of Inputs ===>> 50
# r = a / b # Output => Devisio of Inputs ===>> 2
r = a % b # Output => Module of Inputs ===>> 0

print(f"Your Result is = {r}")

"""

#               """"""""""""""""     IMNPORTANT NOTE       """"""""""""""""

x = int(input("Enter Your First Number : ")) # Input 01
y = int(input("Enter Your Second Number : ")) # Input 02 
z = x + y # Add Both Values
print(f"The sum of values is {z}") # Output will be => 15

# We can also combine this 4 lines code into a single by doing

# print(int(input("Enter Your First Number : ")) + int(input("Enter your Second Number : ")))


#               """"""""""""""""     03    Float       """"""""""""""""

# docs.python.org/3/library/functions.html#round

# float => Float in Python => Float is a type of data in which we use decimal points instead of only complete numbers

"""
x = float(input("Enter your Previous CGPA : " ))
y = float(input("Enter your current GPA : "))
z = float((x + y) / 2)

print(f"Your current CGPA is {z}")


# We can assign that's how mach muximum numbers we need after the decimal point 

x = 2
y = 3
z = x / y
print(f"{z:.3f}")

# Get the rounded value of the float number

x = float(input("Entre your first number : "))
y = float(input("Entre your second number : "))
z = round(x + y)
print(f"{z:,}")

# *********** Boolean Data Type in Python ***********   
# Boolean is a data type in python which can only have 2 values True or False

is_raining = True
print(is_raining)

is_sunny = False
print(is_sunny)

# *********** List Data Type in Python *********** 
# List is a data type where we contain multiple values all in the same place all in the same variable