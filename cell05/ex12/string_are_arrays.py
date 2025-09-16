import sys

if len(sys.argv[1::])==1:
    count=sys.argv[1].count('z')
    print("z"*count)
    if count==0:
        print("none")
else:
    print("none")