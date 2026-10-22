a=int(input("Enter a number "))
try:
    b=10/a
    print(b)
except Exception as err:
    print(f"An error has occured as {err}")
else:
    print("There was no any exceptions ")#This runs only when there is no any exception or it is the child of try 
finally:
    print("I will run no matter what")
print("The division has been completed")    
