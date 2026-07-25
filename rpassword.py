import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
all_characters = lower + upper + digits

password_length = 8

password_list = [
    random.choice(lower),
    random.choice(upper),
    random.choice(digits)
]

for _ in range(password_length - 3):
    password_list.append(random.choice(all_characters))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)
