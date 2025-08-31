list=[1,2,3,4,6,3,7,6,2]
list2=[]
list3=[]
"""i=0
for i in range(len(list)):
    if list[i]%2!=list[i-1]%2:
        print(list[i])
        """
for i in list :
    if i%2==0:
        list2.append(0)
else:
    list2.append(1)
for i in list2:
    if i!=i-1:
        list3.append(list[i])
        i+=1
print(len(list3))
        

