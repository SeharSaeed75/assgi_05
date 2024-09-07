#using conditional statement

# Q 01: even or odd
print("Even or Odd")
num = int (input("Enter a Number = "))
if num % 2 == 0:
    print( num , "is a Even.")
else:
    print (num , "is a Odd.") 
print("-------------------------------------------------------------- \n")   

# Q 02: positive , negative or zero.
print("Check Positive, Nagetive, Zero.")
num1 = int (input("Enter a Number = "))

if num1 > 0 :
    print( num1 , "is a positive number.")
elif num1 < 0: 
     print( num1 , "is a negative number.")
else:
     print("The " , "'", num1 , "'" , "is a Zero.")
print("-------------------------------------------------------------- \n")

# Q 03: Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and print statement for each case.
print("Check 2 and 3.")
def divisible():
    x = int (input("Enter a Number = "))

    if (x % 2 == 0) and (x % 3 == 0):
        print(x , "is divisible by both 2 and 3.")
    elif x % 2 == 0:
        print(x , "is divisible by 2.")
    elif x % 3 == 0:
        print(x , "is divible by 3.")
    else:
        print(x , "is not divisble by both 2 and 3.")
divisible()
print("-------------------------------------------------------------- \n")

# - Take the user age.
# -- If the age is 18 or above:
# -- Ask if they have a nationality of "Pakistani".
#  ---If yes, print "You are eligible to vote."
# ---If no, print "Please obtain a valid ID to vote
print("Check eligible to vote by Age and Nationality.")
def nationality():
    name = str (input("Enter your name ="))
    age = int (input("Enter your age ="))
    nationality = (input("Enter your nationality ="))
    if age >= 18:
        if nationality == "pakistan":
            print("YES, I have Nationality of Pkaistan. ")
            print("Eligible to vote")
        else:
            print("Please obtain a valid ID to vote.")
nationality()
print("-------------------------------------------------------------- \n")

#  Write a program that takes the age of a person as input and determines whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years), or senior citizen (60 years and above).
print("Check classification of person by Age")
def person():
    age = int (input("Enter your age ="))
    if age <= 12:
        print("You are Child.")
    elif age >12 and age <=19:
        print("You are Teeage.")
    elif age >19 and age <=59:
        print("You are Adult.")
    else:
        print("You are Senior Citizen.")
person()
print("-------------------------------------------------------------- \n")

# Enter a month (as a number between 1 and 12). Print the number of days in that month. Assume a non-leap year.
print("Days in a Month")
def month():
    month = int (input("Enter a number(1-12) month = "))
    if month in (1 , 3 , 5 , 7 , 8 , 10 , 12 ):
        print( month , "Month has 31 Days.")
    elif month ==2:
        print( month , "Month has 28 Days.")
    elif month in (4 , 6 , 9 ,11):
        print( month , "Month has 30 Days.")
    else:
        print("Enter the valid number.")
month()
print("-------------------------------------------------------------- \n")

# Check if a year is a leap year or not.
print("Check Leap Year.")
def leap_year():
    year = int (input("Enter the year = "))
    if (year % 4 == 0 and year % 400 == 0 and year % 100 != 0):
        print(year , "is a leap year")
    else:
        print(year , "is not a leap year")
leap_year()