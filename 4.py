arr = [12, 3, 4, 0, 8, 7, 9, 10]
low = 0
high = len(arr) - 1
turn = 1
sumser = 0
sumdima = 0

while low <= high:  
    if turn % 2 != 0:  
        if arr[low] >= arr[high]:
            sumser += arr[low]
            low += 1
        else:
            sumser += arr[high]
            high -= 1
    else:  
        if arr[low] >= arr[high]:
            sumdima += arr[low]
            low += 1
        else:
            sumdima += arr[high]
            high -= 1
    turn += 1

print(sumser, sumdima)
