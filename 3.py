
n = int(input("enter a number: "))
ans = []
for k in range(1, 19):   
    d = 10**k + 1
    if n % d == 0:
        ans.append(n // d)
        if ans:
            ans.sort()
            print(len(ans))
            print(*ans)
        else:
            print(0)
