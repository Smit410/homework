test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("Test Dictionary:", test_dict)

val = int(input("Enter the value you want to check the frequency of: "))
count = 0
for value in test_dict.values():
    if value == val:
        count += 1

print(f"Frequency of {val} is: {count}")
