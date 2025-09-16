var = input()
for i in var:
    if i.isupper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")