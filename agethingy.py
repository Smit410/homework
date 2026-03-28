try:
    age = int(input("Enter your age: "))
    if age % 2 == 0:
        print("The age entered is Even.")
    else:
        print("The age entered is Odd.")

except ValueError:
    print("Value Error: Please enter a valid whole number for age. and also...")