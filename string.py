a="hello brother"
b="Sher Coder"

#0123=Positive Indexing 
#-4-3-2-1=Negative indexing 
print(a[1])
#string slicing 
#b[start point:end point:step]
print(b[5:6:1]) 

#TYPE CONVERSIONS
#int float str list tuple set dict
a=12
a=str(a)
print(type(a))
#BOOLEAN
#SOME FALSEY VALUES ARE 0,0.0,False,[],(),{},None THEY ALWAYS EVALUATE TO FALSE
#FOR EXAMPLE
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(False))  # False
print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False
print(bool(None))  # False+
#Except these values other values are truthy and they evaluate to True
#there are also some special values like NaN(Not a Number) which is also considered as False
#for example
import math
print(bool(math.nan))  # False