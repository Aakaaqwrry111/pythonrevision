a=1
while a<31:
    print(a)
    a=a+1
num=int(input("Enter any multidigit number:"))
while num>0:
    pnum=int(num)%10
    print(pnum)
    num=num//10
    
    
