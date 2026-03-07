num = int(input("Enter decimal number: "))
binary = ""

if num == 0:
    binary = "0"

while num > 0:
    binary = str(num % 2) + binary
    num = num // 2

print("Binary:", binary)
