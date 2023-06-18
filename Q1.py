numb = int(input("Enter a number : "))
count = 0
if numb != 0:
    while numb != 0:
        numb = int(numb/10)
        count += 1
else:
    count += 1
print("The number of digits is : ", count)
