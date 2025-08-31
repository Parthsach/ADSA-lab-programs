n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("_").split()))

leaders = []

max_from_right = arr[-1]
leaders.append(max_from_right)

for i in range(n-2, -1, -1):
    if arr[i] > max_from_right:
        leaders.append(arr[i])
        max_from_right = arr[i]

leaders.reverse()6
print(*leaders)
