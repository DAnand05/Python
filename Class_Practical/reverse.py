#Reverse
n=int(input("Enter the number : "))
rev=0
while n > 0:
    temp=int(n%10)
    rev=(rev*10)+temp
    n=int(n/10)
print(rev)