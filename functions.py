def hello():
    print("Hello world")
    
    
def call_name(name):#name is a parameter here
    print(f"Hello {name}")
hello()
call_name("Aakarshan")#The thing inside the small bracket is called argument 
def palindrome(string):
    checker=str()
    for i in range(len(string)-1,-1,-1):
        checker+=string[i]
    if checker==string:
        return True
    else:
        return False
print(palindrome("naman"))
        
    


