import sys

arg = sys.argv[1::]
arr=[]
if len(arg)==2:
    for i in range(int(arg[0]), int(arg[1])+1):
        arr.append(i)
    print(arr)
else:
    print("none")