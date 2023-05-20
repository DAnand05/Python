def binarySearch(arr,n,num):
    s = 0
    e = n-1
    while s < e :
        mid = (s+e)//2
        print(type(num))
        print(type(mid))
        if arr[mid] == int(num) :
            return mid
            
        if arr[mid] < int(num):
            s = mid+1
        elif arr[mid] > int(num):
            e = mid       
    return -1

arr = list(map(int, input("Enter the sorted array: ").split()))
num = int(input("Enter the target element: "))
val = binarySearch(arr,len(arr),num)

if val == -1:
    print(f"{num} not found in the array")
else:
    print(f"{num} found at index {val}")
