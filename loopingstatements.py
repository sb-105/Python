'''loops are traditionally used when u have a block of code which you want to repeat a fixed number of times..'''
#while-->if iterations are based on condition 
i=0
while i<=3:
    print("python")
    i+=1
print("end of loop")

#for-->if iterations are based on sequence
#range--> if it has single parameter it means stop,if it has 2 parameters one is start and stop and if it has 3 parameters one is start,stop and other one is step value
for i in range(2,20,4):
    print("python")
    print("End loop")
print("end")

#nested loop---> a loop inside a loop
a=0
for i in range(2):
    for j in range(1,4):
        print(a,end="")
    print()
    a+=1

#Loop control statements-->break,continue,pass
#break statement is used to terminate the loop
for i in range(3,7):
    if i==5:
        print("break")
        break
    else:
        print(i)

#continue statement is used to skip the iteration
for i in range(3,7):
    if i==5:
        print("break")
        continue
    else:
        print(i)

#pass satements does nothing but it is used when we create a method that u dont want to implement yet
#loop
for i in range(3,7):
    if i==5:
        pass
#function
def fun():
    pass
fun()