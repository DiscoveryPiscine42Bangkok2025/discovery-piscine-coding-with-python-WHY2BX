import sys
word=sys.argv[1::]

if len(word)>0:
    for i in word:
        match i:
            case i if i.endswith("ism"):
                continue
            case _:
                print(i+"ism")
else:
    print("none")
        