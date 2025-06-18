n=int(input("enter a value:"))
sum_div=0
for i in range(1,n):
    if n%i==0:
        sum_div+=i
if sum_div>n:
    print("abundant")
else:
    print(" not abundant")

