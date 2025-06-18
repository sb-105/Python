'''strings can be said as sequential data
it is immutable
access both positive and negative indexes
Methods:
'''
import string
'''print(string.ascii_letters) #(a--z and A---Z)
print(string.ascii_lowercase) #(a--z)
print(string.ascii_uppercase) #(A--Z)
print(string.punctuation) #prints all special characyers 
print(string.digits) #(0--9)
print(string.hexdigits)#(0123456789abcdefABCDEF)
print(string.octdigits)#(0--7)
SB='hello'
print(SB.endswith('o'))
print(SB.startswith('H'))
print(SB.replace('l','t')) #string is immutable but while using replace it takes another string and original string is unchanged
print('100'.isdigit()) #return true when string contain numbers
print('hi'.isalpha()) #return true when string only contains alphabets
print('72'.isdecimal()) #defaultly python takes decimal value as 72.0 
print('hi7'.isalnum()) #alphanumeric-- contains both letters and numbers
print('Hello world'.istitle())
print(SB.upper()) #convert into uppercase letters
print('HELLO'.lower()) #convert into lowercase letters
print(SB.swapcase()) #if it is in uppercase return lowercase and also vice-versa
print('Python'.partition('t')) #('Py', 't', 'hon') return the value in tuple
print('Hello'.index('l')) #return first index value 
print('Hello'.rindex('l')) #returns last index value
print('sb\nanjali\nsuddhapusa'.splitlines()) #return the value in list
print('python cython'.find('th')) #return the lowest index in substring --->2
print('python'.capitalize()) #return the first letter as capital
print('python cython'.rfind('th')) #return the highest index in substring --->9
print(len('python'))
print(max('python'))
print(min('python'))

#slicing
s='Python'
print(s[:]) 
print(s[:5]) #print upto index 5
print(s[2:]) #starts from index 2
print(s[3:6]) #print index 3 to 6
print(s[-4:-2]) #reverse indexing
print(s[::2]) #print string with a step value--->Pto
print(s[::-1])#reverse the string
print(s[1:6:3])

#operations on string
str1='Welcome'
print(str1*2) #string repetition
print(str1[:6]+'Coder')'''


#Assignment:
#Operations on strings:
#1. Check whether a character is a vowel or consonant.
import string
char=input("Enter a character:")
vowels=['a','e','i','o','u']
char=char.lower()
if char in vowels:
    print("The character is vowel")
else:
    print("The character is constant")


#2.Check whether a character is a alphabet or not.
char=input("Enter a character:")
if char.isalpha():
    print("The Character is alphabet")
else:
    print("The character is not alphabet")
    

#3. Find the ASCII value of a character
x=input("Enter a value:")
a=print(ord(x)) #builtin function used to find ascii value
print(chr(67)) #used to find the ascii letter based on the value


#4.Length of the string without using strlen() function.
str='SomaSekhar'
print(len(str))

c=0
for char in str:
    c+=1
print(c)
#5. Toogle each character in a string.
print(str.swapcase())

#6. Count the number of vowels.
str1=input("Enter a String:")
str1=str1.lower()
count=0
for char in str1:
    if char in vowels:
        count+=1
print(count)
#7. Remove the vowels from a string.
new=''
cnt=0
for char in str1:
    if char not in vowels:
        new +=char
        cnt+=1
print(new)
print(cnt)

#8, check if the given string is palindrome or not.
a=input("Enter a string:")
a=a.lower()
if a==a[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
#9. Print the given string in reverse order.
print(str1[::-1])
#10. Remove all the characters from string except alphabets.
string=input("Enter a string:")
b=''
for char in string:
    if char.isalpha():
        b+=char
print(b)

