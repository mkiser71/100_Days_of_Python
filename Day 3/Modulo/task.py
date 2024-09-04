#Determine if a number is odd/even using modulo.

userNumber = int(input("Enter a number to see if it's odd or even."))
oddEven = (userNumber % 2)
if oddEven == 0:
    print("You typed an even number.")
else:
    print("You typed an odd number.")