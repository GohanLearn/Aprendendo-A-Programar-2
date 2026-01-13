#Below, there are some examples of variable names and their values in Python:
nameTest = "Jonathan" #Put any thing here
print(nameTest) #Here we go

country = "9abcdABCD"
print(country)

#Rule 1: A name of variable must be significant or descriptive.
#Rule 2: A name of variable must start with a letter (a-z, A-Z) or an underscore (_)
#Rule 3: A variable name can't start with a number
#Rule 4: A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Rule 5: Variable names are case-sensitive (age, Age and AGE are three different variables)
#Rule 6: Variable names can't be the same as reserved words or keywords in Python (like print, for, if, else, import, etc)
#Rule 7: A value, if it's a string, must be enclosed in single quotes (' ') or double quotes (" ")

  #Below, there are data storage examples:
name = "John"
age = 23
bodyTemperature = 98.4

  #Below, there are numerics examples (Int, Float and Complex)
 #int:
numberInt = 5
ageInt = 25

 #float:
temperature = 35.6
rateOfInterest = 2.5

 #complex (more utilized in Cientifical Computation):
numberComplex = 5 + 3j
print(numberComplex)

  #Below, there are Strings examples:
stringExample = "Caracters"
firstName = "John"
lastName = "Doe"
print(firstName)
print(lastName)

  #Below, there are multiple lines strings example:
quote = """ Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.
- John Woods """
print(quote)

  #Below, there are true or false examples (Boolean, also called "bool"):
isLoggedIn = False
print(5>10) #This will print False
print(5<10) #This will print True

  #Below, there are type() function examples:
print(type(name)) #This will print the type of the variable "name" (string or str)
print(type(age)) #This will print the type of the variable "age" (int)
print(type(bodyTemperature)) #This will print the type of the variable "bodyTemperature" (float)

  #Below, there are input() examples:
input("Please enter your name:") #The user response will not be stored, we need to store it in a variable
username = input("Please enter your name:") #Here we go :)
print(username)
print(type(username))
#Testing
print("--------------------Login test bellow:")
user = input("Enter your name:")
ageUser = input("Enter your age:")
print(user)
print(ageUser)
print(type(user))
print(type(ageUser)) #For a simple reason, there will appear "string", we will solve it using Type Conversion
print("---------------Type Conversion")
#Type Conversion example:
ageUser = int(input("Enter your age:"))
print(ageUser)
print(type(ageUser))