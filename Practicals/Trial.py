print(1234/10)
print (1234//10)
for i in range(6):
    for j in range(i):
        print("*", end = " ")
    print()
val=int(input("Enter the value: "))
print(type(val))
'''base=int(input("Enter the base: "))
exp=int(input("Enter the exponent: "))

res=1
for i in range(abs(exp)):
    res*=base
if exp < 0:
    print(1/res)
else:
    print(res)'''