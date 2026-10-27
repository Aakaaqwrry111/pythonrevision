from pathlib import Path

print("Press 1 for reading a file")
print("Press 2 for creating a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")


def readfileandfolder():
    path=Path('') #REPRESENTS THE CURRENT WORKING DIRECTORY
    items=list(path.rglob('*'))
    #print(items) it prints items without numbering and sorting
    for i, items in enumerate(items):#enumerate starts the loop from 0 by default
        print(f"{i+1}: {items}")

def createfile():
    readfileandfolder()
    name=input("Please enter your filename :-\n")
    p=Path(name)#This converts the filename string into a Path object
    with open(p,'w') as fs:#with ensures the file is closed when the block exits 
        data=input("Write something:-\n")
        fs.write(data)
        
    
    

check=int(input("Enter your response- \n"))
if check==1:
    readfileandfolder()
