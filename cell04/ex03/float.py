var = input("Give me a number: ")
num = float(var)

if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")