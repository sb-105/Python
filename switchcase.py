'''we caan use switch case to check multiple conditions,python doesnot support switch case statement
but it can be implemented by using dictionary,function or classes'''
a,b=4,2
swtich={
    1:a+b,
    2:a-b,
    3:a**b,
    4:a/b,
    5:a%b
}
print(swtich.get(3))
print(swtich.get(2))
#if the value is string we have to print it in single quotes
switcher={
    'a':"Python"
}
print(switcher.get('a'))
#conditional expressions
#syntax:<expression>if<if_condition>else<else_condition>
age=20
x='can vote' if age>=18 else 'cannot vote'
print(x)

x=y=10
z=1+(x if x>y else y)+2
print(z)