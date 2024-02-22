year = int(input("Enter a year"))

if (year %4 == 0) and (year%100 != 0 ):
    print("It is a leap year")
    
elif (year%100 == 0):
    print("its a century year")

else:
    print("Not a leap year")
  
    # Letting the user know if the year is in the past, present, future.

date_time = "Future"
date_time2 = "Past"
date_time3 = "Present"

if (year > 2024):
    print(date_time,)
    
elif (year < 2024):
    print(date_time2)
    
else:
    print(date_time3)