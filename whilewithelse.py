'''while  with else clause: 
the else clause is only executed when while condition becomes false.if you break out of the loop or an exception is raised,it will not be executed..'''
i=0
while i<=3:
    print("Python")
    i+=1
    break
else:
    print("endloop")