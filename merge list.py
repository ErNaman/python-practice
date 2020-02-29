def merge(a,b):
    l3=[]
    l3.append(a)
    l3.append(b)
    print("merged list is:- ",l3)
size=int(input(print("enter size of list:- ")))
l1=[]
l2=[]
for x in range(size):
    item=int(input(print('insert value in list1:- ')))
    l1.append(item)
for x in range(size):
    item=int(input(print('insert value in list2:- ')))
    l2.append(item)
merge(l1,l2)
