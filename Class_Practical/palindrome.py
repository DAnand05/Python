#Palindrome.py

num=int(input("Enter a number to check, if it's palindrome : "))
if num<0 :
    print("Number is not palindrome.")
    exit()
val=0
temp=num
while temp>0 :
    val=val*10+(temp%10)
    #print("val = ",val,", temp = ",temp ,"\n")          #to check result iteration-wise
    temp//=10
if val==num :
    print("Number is palindrome.")
else :
    print("Number is not palindrome.")