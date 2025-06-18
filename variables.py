#variables--Assigning and reassigning variables,only hold one value at a time
x=5
y='hello'
#reassigning the variables
x=10
print(x,y)
#multiple assignments
a,b,c=1,2,3
print(b)
#swapping variables
#method1:using temp variable
name="python"
name2="programming"
temp=name
name=name2
name2=temp
print(name,name2)
#method2:pythonic way
n1,n2="python","pro"
n1,n2=n2,n1
print(n1,n2)
#deleting a variable
z=7
print(z)
del z
print(z)