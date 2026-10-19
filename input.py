name="Aakarshan"
age="23"
print("My name is ",name,"and my age is",age)
#formatting string using f-string
print(f"My name is {name} and my age is {age}")
#raw string 
#what are raw strings in Python? Raw strings are a way to define string literals in Python where backslashes are treated as literal characters and not as escape characters. This is useful when dealing with strings that contain a lot of backslashes, such as file paths or regular expressions. In a raw string, the backslash is not interpreted as an escape character, so it is treated as a normal character. To create a raw string, you can prefix the string literal with the letter 'r' or 'R'. For example, r"C:\Users\Username\Documents" is a raw string that represents the file path "C:\Users\Username\Documents" without interpreting the backslashes as escape characters.
print(r"Hello \n World")
#Using input function to take input from user
name_1=input("hello what is your name?")
print(f"hello {name_1} nice to meet you")

age_1=input("hello what is your age?")
print(f"hello {name_1} you are {int(age_1)} years old")