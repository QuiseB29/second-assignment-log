# Corrected Code for Decision at the Crossroad
number = float(input("Enter a number: "))  # Convert input to a float to handle decimal numbers

if number > 0:
    print("The number is positive.")
elif number == 0:  # Use '==' for comparison, not '='
    print("The number is zero.")
elif number < 0:  # Corrected 'else' syntax and added 'elif'
    print("The number is negative.")

# Task 1: Identify the Greatest
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}.")

# Task 2: Identify the Smallest
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Finding the smallest number
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print(f"The smallest number is {smallest}. The largest number is {largest}.")



# Task 1: Leap Year Checker
year = int(input("Enter a year: "))

# Leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")




