arr1 = [2, 8, 9, 48, 8, 22, -12, 2]
arr2=[]
arr3=[]
for i in arr1:
    j = i+2
    arr2.append(j)
    if j > 5:
        arr3.append(j)
print("original arr: ", arr2)
print("new arr: ", set(arr3))