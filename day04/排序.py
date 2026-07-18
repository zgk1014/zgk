l1=[22,11,33,55,44]
l1.sort()
print(l1)



l1.sort(reverse=False)
print(l1)


l1.sort(reverse=True)
print(l1)



l2=["bc","abc","zyxl","h"]
l2.sort()
print(l2)


l2.sort(key=len)
print(l2)
l2.sort(key=len,reverse=True)
print(l2)



def get_data(t1):
    return t1[1]

l3=[(1,3),(2,2),(5,1),(3,9)]
l3.sort()
print(l3)

l3.sort(key=get_data)
print(l3)
l3.sort(key=get_data,reverse=True)
print(l3)




