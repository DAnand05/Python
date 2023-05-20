def insertionSort(input, size):
    for i in range(1, size):
        current = input[i]
        j = i-1
        while j >= 0 and current < input[j]:
            input[j+1] = input[j]
            j -= 1
        input[j+1] = current

arr = list(map(int, input("Enter the array: ").split()))
n=len(arr)
insertionSort(arr,n)
print(arr) 