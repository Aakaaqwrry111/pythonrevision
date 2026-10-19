n=int(input("Enter a number:\n"))
for i in range (1,n+1):
    print("Hello World")

for i in range(1,n+1):
    print(i)
    
for i in range(n,0,-1):
    print(i)

for i in range(1,11):
    print(f"{n}*{i}={n*i}\n")


prod=1
for i in range(1,n+1):
    prod=(prod)*i
print(f"The factorial is {prod}")

sum=0
for i in range(n+1):
    sum=i+sum
print(f"The sum is {sum}")

esum=0
osum=0
for i in range(n+1):
    if i%2==0:
        esum+=i
    else:
        osum+=i 
print(f"The sum of even numbers is {esum} and odd number is {osum}")

print("Here are the factors listed below:")
for i in range(1,n+1):
    if n%i==0:
        print(i)
        
primechecker=0
for i in range(1,n+1):
    if n%i==0:
        primechecker=primechecker+i
         
if primechecker==n+1:
    print(f"{n} is a prime number")
else:
    print(f"{n} is a composite number")

facsum=0
for i in range(1,n):
    if n%i==0:
        facsum=facsum+i
if facsum==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")

word=input("Enter any string:\n")

#STRING CONCATINATION
rev=str()
for i in range(len(word)-1,-1,-1):
    rev=rev+word[i]
print("The reverse is",rev)
if rev==word:
    print(word+" is a palindrome")
else:
    print("It is not a palindrome")







    