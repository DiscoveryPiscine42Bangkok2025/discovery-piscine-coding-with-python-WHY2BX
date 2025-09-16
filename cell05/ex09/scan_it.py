import sys

if len(sys.argv) == 3:
    count = sys.argv[2].split().count(sys.argv[1])
    if count!=0:
        print(count)
    else:
        print("none")
else:
    print("none")