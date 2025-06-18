#write a program to check whether the given number is strong number or not 

#logic a number that is equal to the sum of factorial of its individual digits is called strong number#
n=145
temp=n
sum=0
f=[0]*10
f[0]=1
f[1]=1
for i in range(2,10):
    f[i]=f[i-1]*i
while(temp):
   r=temp%10
   temp=temp//10
   sum+=f[r]
if(sum==n):
   print("strong number")
else:
 print("not strong number")
