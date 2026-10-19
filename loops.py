a=range(1,21,1)
for i in a:
    print(i)
num=int(input("Which table do you want to print?\n"))
c=range(1,11,1)
for i in c:
    print(f"{num}*{i}={num*i}")
#NOW LET'S LOOK AT LOOPS FOR STRINGS 
#THE KEY PRINCIPLE IS USING THE LENGTH OF THE STRING AS ITERATION COUNT
name="Aakarshan"
for i in range(len(name)):
    print(name[i])
    
for i in range(1,21):
    if i==56:
        break
    print(i)
else:
    print("The loop has ended successfully")
