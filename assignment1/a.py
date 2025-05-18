a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Addition:\t",a+b)
print("Subtraction:\t",a-b)
print("Multiplication:\t",a*b)

if float(b)!= int(0):
    c=a/b
else:
    c= "Cannot divide by zero"

print("Division:\t",c)