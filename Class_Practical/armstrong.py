#Armstrong.py

num=int(input("Enter the number to check, if it's Armstrong: "))
sum=0
temp=num
while temp>0 :
    val=temp%10
    sum+=(val*val*val)
    temp//=10

if sum==num :
    print("Entered number is an Armstrong number.")
else :
    print("Entered number is not an Armstrong number.")