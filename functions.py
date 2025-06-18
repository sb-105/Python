'''Functions are used to do some tasks
TYPES:userdefined,builtin,lambda/anonymous,recursive..
1)userfedined function:used 'def'keyword to define
Syntax:def fun_name(Parameter):
---------------
--------------
fun_name()
pass by value and pass by refrence:
by default in python the parameters are passed in pass by reference only---it means if we call any variable if already existed it will in the function also
Ex:def fun(x):
    x[0]=20
    list=[10,12,13]
    print(list)---herelist will be printed
    fun(list)----here the fun is called and list is updated....
parameter-->the value which passed at defining the function name
argument-->the value which was passed during calling the function

return---> it is a keyword which return the value from function

Function Arguments:
1)default argument-->The values are passed at function defining// if any values is not passed at function calling it will defaultly take the value at function defination...
Ex:  def fun(x,y=10):
        print("x",x)
        print("y",y)
    fun(10)

2)Required argumnets:these argumnets values must be passed in correct number and order during function call
def fun(name,age,marks):
    print("Nmae:",name)
    print("age:",age)
    print("marks:",marks)
fun('SB',22,98)---correct way of passing with same parameters and argumnets..

3)keyword argumnets:the keywords are mentioned during function call along with values.these are passed by value
These keywords are mapped with function arguments
def stud(first,last):
    print("first:",first)
    print("last:",last)
stud(last='pro',first='Python')

4)variable arguments:very useful when u dont know the exact number of arguments to be passed to a function
Ex: def myfun(*argv):
        for arg in argv:
            print(arg)
    myfun('hi','hello')
**Loop works only for checking same condition multiple times 
Recursive function:calling same fun again and again and by defaultly python takes 1000 recursion only...
Ex:Factorial of a number
    def factorial(n):
        if n==1:
            return 1
        else:
            return(n*factorial(n-1))'''
import sys  #sys is a module which contains setrecursionlimit to exceeds the recursions
sys.setrecursionlimit(5000)
def factorial(n):
    if n==1:
        return 1
    else:
        return(n*factorial(n-1))
print(factorial(1000))

'''Anonymous function:these functions are called anonymous because these are not declared using def keyword
we can use 'lambda' keyword to define anonymous fun
Ex: sum of two numbers using lambda function
sum=lambda a,b:a+b
print(sum(10,19))

Scope of variables:
global variable:can be accessed outside of function
local variable:can be accessed only inside of function 
Ex:
name='python' #Global variable
def f():
    name='pro'#Local variable
    print(name)
print(name)
f()'''