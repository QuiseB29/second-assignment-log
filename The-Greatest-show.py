var1 = int(input("Enter a number"))
num1 = 10
num2 = 4
num3 = 2


if num1 >= num2 and num1 >= num3:
    print(num1)
    
elif num2 >= num1 and num2 >= num3:
    print(num2)
    
else:
    print(num3)



var1 = int(input("Enter a number"))
num1 = 10
num2 = 4
num3 = 2

if num1 <= num2 and num1 <= num3:
    print(num1("The Least"))
    
elif num2 <= num1 and num2 <= num3:
    print(num2("The Least"))
    
else:
    print(num3)
    
# Checking equality 

check_equality = (num1, num2, num3)

if num1 == num2 == num3:
    print("They are equal")
    
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Two of these are equal")
    
else:
    print("All Three are different")