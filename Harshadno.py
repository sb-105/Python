#Harshad number-the number which is divisible by sum of its digits!!
n=21
temp=n
sum=0
while(temp):
   r=temp%10
   temp=temp//10
   sum+=r
if n%sum==0:
   print("Harshad number ")
else:
   print("Not a harshad number")