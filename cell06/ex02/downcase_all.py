import sys

var = sys.argv[1::]
def downcase_it(string):
    if len(string)!=0:
        for i in string:
            i = i.lower()
            print(i)
        return string
    else:
        print("none")

downcase_it(var)