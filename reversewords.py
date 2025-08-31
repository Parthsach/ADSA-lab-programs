s="welcome to India"
chars=list(s)
n=len(chars)
def reversewords(chars,left,right):
    while left<right:
        chars[left],chars[right]=chars[right],chars[left]
        left+=1
        right-=1
reversewords(chars,0,n-1)
start=0
for end in range(n+1):
    if end==n or chars[end]==' ':
        reversewords(chars,start,end-1)
        start=end+1
print(''.join(chars))