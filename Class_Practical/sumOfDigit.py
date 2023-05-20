#Sum of digits
n=int(input("Enter the number : "))
sum=0
while n > 0:
    temp=int(n%10)
    sum+=temp
    n=n/10
print(sum)