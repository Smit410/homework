base = int(input("Enter the base number: "))
n = int(input("Enter the number of powers (n): "))
result = 1
for i in range(n):
    result = result * base
    power = i + 1
    print(base, "raised to the power of", power, "is", result)
