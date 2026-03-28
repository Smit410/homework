base = int(input("Enter the base number: "))
exponent = int(input("Enter the power (n): "))
result = 1
for i in range(exponent):
    result = result * base
print(f"{base} raised to the power of {exponent} is: {result}")