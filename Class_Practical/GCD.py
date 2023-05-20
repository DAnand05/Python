#GCD
num1=int(input("Enter the small number : "))
num2=int(input("Enter the large number : "))
res=0
for i in range(1, num2+1):
    if((num1%i==0) and (num2%i==0)):
        res=i
    else:
        continue
print(res)