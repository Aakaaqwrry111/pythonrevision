from pathlib import Path
import os

print("Press 1 for reading a file")
print("Press 2 for creating a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check=int(input("Enter your response-\n"))


def readfileandfolder():
    path=Path('') #REPRESENTS THE CURRENT WORKING DIRECTORY
    items=list(path.rglob('*'))
    #print(items) it prints items without numbering and sorting
    for i, items in enumerate(items):#enumerate starts the loop from 0 by default
        print(f"{i+1}: {items}")

def createfile():
 try:
    readfileandfolder()
    name=input("Please enter your filename :-\n")
    p=Path(name)#This converts the filename string into a Path object
    if not p.exists():
    
     with open(p,'w') as fs:#with ensures the file is closed when the block exits 
         data=input("Write something:-\n")
         fs.write(data)
     print("FILE CREATED SUCESSFULLY")
    else:
        print("this fie already exists")
 except Exception as err:
     print(f"An error occured as {err}")
             
def readfile():
    try:
        readfileandfolder()
        name=input("Which file do you want to read?")
        p=Path(name)
        if p.exists() and p.is_file():#FILE HUNAPARYO DIRECTORY HAINA
            with open(p,'r') as fs:
                data=fs.read
                print(data)
            print("Readed Successfully") 
        else:
            print("the file doesn't exist")
    
    except Exception as err:
       print(f"The error has occured as {err}")

def updatefile():
    try:
      readfileandfolder()
      name=input("which file do you want to update?")
      p=Path(name)
      if p.exists() and p.is_file():
          with open(p,'a') as fs:
              data=input("Enter the content that you want to update into that file:\n")
              fs.write(data)
          print("File updated successfully")
      else:
          print("The file doesn't exist")
      
    except Exception as err:
        print(f"An error has occured as {err}")
    
def deletefile():
    try:
        readfileandfolder()
        name=input("Enter the name of the file that you want to delete:\n")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("The file has been removed sucessfully")
        else:
            print("The file doesn't exist")
    except Exception as err:
        print(f"An error has occured as {err}")

    

if check==1:
    readfile()
if check==2:
    createfile()
if check==3:
    updatefile()
if check==4:
    deletefile()
