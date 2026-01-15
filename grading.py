print("-New Zealand Grading System-")

name = input("Enter student name: ")
score = float(input("Enter score (0-100): "))

if score >= 80:
    grade = "Excellence"  
elif score >= 65:
    grade = " Merit"  
elif score >= 50:
    grade = "Achieved"  
else:
    grade = "Not Achieved"

print(name, "got grade", grade, "Niceuuuuuu")