import os #os is a module which help to create directories
#reading and creating a file
with open("sample.txt",'w') as f:
    f.write("HI WELCOME TO PYTHON!")
print("file created successfully")
with open("sample.txt",'r') as f:
    content=f.read()
    print(content)
#append data
with open("sample.txt",'a') as f:
    f.write("\n This line is Appended")
#read line by in line
with open("sample.txt",'r') as f:
    for line in f: #for loop is used to read line by line
        print(line.strip()) #strip is used to remove spaces'''

#Creating directories

os.makedirs("file_oops_practise/data/reports",exist_ok=True) #makedirs is used to make directories
print("Directories created succesfully")

with open("file_oops_practise/data/sample.txt",'w') as f:
    f.write("HI WELCOME TO PYTHON!")
print("file created successfully")
with open("file_oops_practise/data/sample.txt",'r') as f:
    content=f.read()
    print(content)
#append data
with open("file_oops_practise/data/sample.txt",'a') as f:
    f.write("\n This line is Appended")
#read line by in line
with open("file_oops_practise/data/sample.txt",'r') as f:
    for line in f: #for loop is used to read line by line
        print(line.strip()) #strip is used to remove spaces'''

#listing all files and folders
print("content of data:",os.listdir('file_oops_practise'))
#rename a file
os.rename("file_oops_practise/data/sample.txt","File_oops_practise/data/sample_renamed.txt")
#removing a file
os.remove('file_oops_practise/data/sample_renamed.txt') #to remove a file u have to comment the rename part because if file already exists
