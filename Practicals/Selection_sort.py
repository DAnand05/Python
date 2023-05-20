def selectionSort(arr,n) :
        for i in range(n) :
            for j in range(i) :
                if arr[i]<arr[j] :
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
                continue

arr = list(map(int, input("Enter the array: ").split()))
n=len(arr)
selectionSort(arr,n)
print(arr) 