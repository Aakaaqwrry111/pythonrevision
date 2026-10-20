a=27
if a>29:
    print("a is greater than 29")
money=int(input("Enter the amount of money that you are willing to spend:\n"))
if money>=1000:
    print("You'll be able to buy this product")
    
else:
    print("You're not able to buy this product")
    
#PROGRAM TO CHECK IF THE YEAR IS LEAP 
year=int(input("Enter the year:\n"))
if year%400==0:
    print(f"The year {year} is a leap year")
elif year%100==0:
    print(f"The year {year} is not a leap year")
elif year%4==0:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")
#The main logic behind this is that a leap year is a year that is divisible by 4, but not divisible by 100, unless it is also divisible by 400. This means that if a year is divisible by 400, it is a leap year. If it is divisible by 100 but not by 400, it is not a leap year. If it is divisible by 4 but not by 100, it is a leap year. Otherwise, it is not a leap year.