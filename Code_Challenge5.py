factor = 1
a = eval(input("Enter your number: "))

for i in range (a,0,-1):
    factor *= i 

print("The factorial of the number", a, " is ", factor)