# Read number of test cases
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    max_val = max(arr)
    count = 0

    for x in arr:
        if x != max_val:
            count += 1

    print(count)
