n = int(input("Enter a number: "))


odd_numbers = [i for i in range(n) if i % 2 != 0]

print(f"Odd numbers under {n}: {odd_numbers}")

fruits = ["apple", "banana", "cherry", "date"]


updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Original list:", fruits)
print("Updated list: ", updated_fruits)
