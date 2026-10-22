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
