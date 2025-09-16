var1 = int(input("Enter the first number:"))
var2 = int(input("Enter the second number:"))
var3 = var1*var2

print("%d x %d = %d" %(var1, var2, var3))
if var3>0:
    print("The result is positive.")
elif var3<0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
