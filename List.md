## Python list functions

# list
print("my list is \n") <br />
lst=[1,2,3,4,5]
print(lst)
# remve with item
lst.remove(1) <br />
print(lst)
# remove with index
lst.remove(lst[len(lst)-1]) <br />
print(lst)
# Append item last of list
lst.append(5) <br />
print(lst)
# append item in between or initial of list
lst.insert(0,1) <br />
lst.insert(2,2.5) <br />
print(lst)
# update list
lst[5]=4.5 <br />
print(lst)
# add list
a=[2,3,4] <br />
b=[5,7] <br />
a=b+a <br />
print(a)
# sum list
print(sum(a))
# count number of occurance of ite in lst
a=['A',4,'a',6,4,1,2,2,'A'] <br />
print("A occurs no of time in list :", a.count('A'))
# get index of item
print(a.index(6))
# get the min and max item of list
a=[6,7,2,9,1] <br />
print(min(a)) <br />
print(max(a))

# Sort string
a.sort(reverse=True) <br />
print(a) <br />
a.sort(reverse=False) <br />
print(a)

#  delete with index or random
print(a.pop(1)) <br />
print(a.pop())

# delete with item
a.remove(6) <br />
print(a)

# copy a list
lst2=[1,5,7,4,9,10] <br />
lst1=lst2.copy()
