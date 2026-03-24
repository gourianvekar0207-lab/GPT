import array as arr
ary=arr.array('i',[1,2,3,4,5,6,7,8,9])
ary2=arr.array('d',[1,2,3,4,5,6,7,8,9])
print("elements of array 1")
for i in range(len(ary)):
    print(ary[i])
print("elements of array 2")
for d in range(len(ary2)):
    print(ary2[d])
print("insertion")
ary.insert(0,10)
print("updated array is :",ary)
ary.remove(2)
print("array value removed :",ary)
print(ary[1:5])
print(ary[2])
ary.clear()

















