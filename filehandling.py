'''file handling-- which is used to store,read and modify data permanently on disk using python
we use a builtin function open() function with different modes
modes:
r--- read()
w--- write() #it does 2 activites: create a file//if already exists it overrides
a--- appends(adds to end)
x--- create(error if exists)
Trainer saves session summaries:
simulate a dialy routine of a trainer who:
1.writea new summary each day.
2. reads past summaries.
3. appends additional notes later.'''

#creating summary from scratch
summary="""Day1:Summary:
-Topic:File handling in python
-covered-open(),read,write(),append()
-activity:Real-time trainer use case."""
with open("Daily_summary.txt","w") as file:
    file.write(summary)
print("File created successfully")

#reading the report(read mode 'r')
#Trainer want to review what was written previously
with open("Daily_summary.txt",'r') as file:
    SB=file.read() #SB is a variable name which is used to store the reading and to print ot on the terminal
print("Reading Daily summary.\n")
print(SB)

#Appending the file
#adding/updating the file
extra_notes="""
Trainer's note:
-students asked good question
-need to repeat file modes tomorrow"""
with open("Daily_summary.txt",'a') as f:
    f.write(extra_notes)
print("File appended succesfully.")
print(SB)

#final reading to confirm.
with open("Daily_summary.txt",'r') as file:
    Updated_SB=file.read() #SB is a variable name which is used to store the reading and to print ot on the terminal
print("Reading Daily summary.\n")
print(Updated_SB)