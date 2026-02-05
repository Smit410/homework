num = int(input("Enter a number: "))


if num < 0:
    num = -num

count = 0


if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10   # Remove last digit
        count += 1

print("Total digits:", count)