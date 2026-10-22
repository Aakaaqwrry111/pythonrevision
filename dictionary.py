#We use key and value pairs for dictionary
#Traversing in dictionary 
#We can traverse both the keys and values in dictionaries, but the default loop is set on keys, and you can access the values because of the keys. 
#So technically, you can traverse both keys and values at the same time. 
d={10:100,20:200,30:300,40:400}
for i in d:
    print(d[i])
    
d.clear()
print(d)
a=[1,2,3,4,5]
b=a
b[0]=100
print(a)
#TO PERFORM SHALLOW COPY INSIDE THE DICTIONARY 
a1={1:2,3:4,5:6}
b1=a1.copy()
print(b1)
b1[0]=100

print(a1)
#PROGRAM TO MERGE 2 DICTIONARIES

for i in a1:
    a1[i]=b1[i]
print(b1)

 #Iteration 1:
 #i = 40

# Statement: d1[i] = d2[i] evaluates to d1[40] = d2[40]

# Since 40 is not yet a key in d1, it adds a new key-value pair to d1.

# d2[40] is 400

# Updated d1: {10: 100, 20: 200, 30: 300, 40: 400}

# Iteration 2:
# i = 50

# Statement: d1[50] = d2[50]

# d2[50] is 500

# Updated d1: {10: 100, 20: 200, 30: 300, 40: 400, 50: 500}

# Iteration 3:
# i = 60

# Statement: d1[60] = d2[60]

# d2[60] is 600

# Updated d1: {10: 100, 20: 200, 30: 300, 40: 400, 50: 500, 60: 600}
sum=0
for i in b1:
    sum+=b1[i]
print("The sum is",sum)
#TO COUNT THE FREQUENCIES OF EACH ELEMENT INSIDE A LIST
l=[1,1,1,1,1,1,1,2,2,2,2,2,4,4,5,5,5,5,5,5]
diction={}
for i in l:#THIS IS ITEM BASED LOOP NO NEED TO ACCESS THE ELEMENTS USING INDEX
    if i in diction.keys():
        diction[i]+=1
    else:
        diction[i]=1
print(diction)
#Write a Python program to combine two dictionaries by adding values for the common keys. 
d1={1:20,2:30,4:60}
d2={1:30,5:60,4:90}
for i in d1:
    if i in d2.keys():
        d2[i]+=d1[i]
    else:
        d2[i]=d1[i]
print(d2)