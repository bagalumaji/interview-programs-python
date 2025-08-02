arr = [1, 2, 2, 3, 4, 4, 5, 5]
p1 = 0
p2 = 1
while p2 < len(arr):
    if arr[p1] != arr[p2]:
        p1 = p1 + 1
        arr[p1] = arr[p2]

    p2 = p2 + 1

for i in range(0, p1 + 1):
    print(arr[i])
