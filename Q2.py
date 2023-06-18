n = input("Enter a number : ")
if n.isalpha():
    print("Please enter a number!")
elif n.isnumeric():
    z = int(n)+1
    fact = 1
    for i in range(1,z):
        fact = int(fact*i)
    print("The factorial of ",n," is : ",fact)
else:
    print("Enter a valid number!")