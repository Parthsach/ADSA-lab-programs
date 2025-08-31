list=[0,1,0,2,1,0,1,3,2,1,2,1]
leftmax=[0]*len(list)
rightmax=[0]*len(list)
water=0
leftmax[0]=list[0]
for i in range(1,len(list)):
    leftmax[i]=max(leftmax[i-1],list[i])    
rightmax[len(list)-1]=list[len(list)-1]
for i in range(len(list)-2,-1,-1):
    rightmax[i]=max(rightmax[i+1],list[i])      
for i in range(len(list)):
    water+=min(leftmax[i],rightmax[i])-list[i]
print(water)
