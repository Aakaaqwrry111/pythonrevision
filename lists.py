#LIST TRAVERSING
#TRAVERSING MEANING=TO PASS MOVE OR TRAVEL ACROSS
a=["aakarshan",11,17,True,print("Hello World"),print("Jay Sambhu")]
for i in range(len(a)):
    print(a[i])

for i in a:
    print(i)
#To find methods of function in python we use print(dir(function()))
#For ex-
for i in range(len(dir(a))):
    print(dir(a)[i])
#Append
a.append("Hehehehe ")
print(a)
#Insert is more developed version of append method where user can append the element according to the desired index
a.insert(1,"tsk")  
print(a)
#list.insert(index,)
help(list)