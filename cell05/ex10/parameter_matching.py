import sys

if len(sys.argv) == 2:
    inp = input("What was the parameter?: ")
    if inp==sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")