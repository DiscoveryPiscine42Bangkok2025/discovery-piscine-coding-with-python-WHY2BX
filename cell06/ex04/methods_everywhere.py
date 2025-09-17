import sys

arg = sys.argv[1::]

def shrink(string):
    print(string[0:8])

def enlarge(arr):
    for i in range(len(arr), 9):
        arr+="Z"
    print(arr)

for i in arg:
    if len(i)<1:
        print("none")
    elif len(i)<8:
        enlarge(i)
    elif len(i)>8:
        shrink(i)
    else:
        print(i)