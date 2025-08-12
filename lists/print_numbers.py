arr = [1,2,3,4,5,6,7,8,9,10]
for i in range(2,len(arr)):
    if arr[i-2]+1 == arr[i-1] and arr[i-1]+1 == arr[i]:
        print(arr[i-2],arr[-1],arr[i])


