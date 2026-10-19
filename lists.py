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
#help(list.insert)
#insert(self, index, object, /)
l=[1,2,3,4,5,6,7]
for i in range(len(l)):
    if l[i]>0:
        print(l[i])
sum=0
total_elements=0
for i in range(len(l)):
    sum+=l[i]

print(sum)
print(i+1)
average=sum/(i+1)
print(f"The average is {average}")
largest=l[0]
for i in range(len(l)):
    if l[i]>largest:
        largest=l[i]
        index=i
print(f"The largest number is {largest} and the index is {i} ")
