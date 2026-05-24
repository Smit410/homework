even_squares = []
odd_squares = []

# Change 1 and 11 to whatever numbers you want
for num in range(1, 11):
    square = num * num
    
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("Even squares:", even_squares)
print("Odd squares:", odd_squares)
