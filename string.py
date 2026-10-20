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
#What type of values are considered as False in Python?what is the reason behind it?
#The main reason behind this is that these values are considered as "empty" or "zero" values in Python. For example, 0 and 0.0 represent the absence of a numerical value, False represents the absence of a boolean value, and empty collections (like [], (), and {}) represent the absence of any elements. None represents the absence of any value at all. Therefore, when these values are evaluated in a boolean context, they are considered as False.
#
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
#What is NaN in Python? NaN stands for "Not a Number" and it is a special floating-point value that represents undefined or unrepresentable numerical results, such as the result of dividing zero by zero. In Python, NaN is represented by the float('nan') expression. It is important to note that NaN is not equal to any value, including itself, which can lead to unexpected behavior in comparisons and calculations.
#for example
import math
print(bool(math.nan))  # why is it True? because NaN is not equal to any value including itself, so it is considered as a truthy value in Python.Also because we consider any value valse if it is equal to zero or doesn't have any value but NaN is not equal to zero or any other value so it is considered as a truthy value in Python.
#difference between implicit and explicit type conversion in Python
#Implicit type conversion, also known as type coercion, is when Python automatically converts one data
#type to another without the need for explicit instructions from the programmer. This usually happens when performing operations between different data types, and Python will convert one of the operands to match the other. For example, if you add an integer and a float, Python will implicitly convert the integer to a float before performing the addition.
#Explicit type conversion, on the other hand, is when the programmer explicitly converts one data type to another using built-in functions like int(), float(), str(), etc. This requires the programmer to specify the desired data type for the conversion. For example, if you want to convert a string to an integer, you would use int("123") to explicitly convert the string "123" to the integer 123.