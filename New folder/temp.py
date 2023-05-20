'''x = 10

message = "x is greater than 5" if x > 5 else "x is less than or equal to 5"

print(message)'''

# Take input from user
marks = []
for i in range(5):
    mark = float(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)

# Calculate total marks and percentage
total_marks = sum(marks)
percentage = (total_marks / 500) * 100

# Determine the grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Print the result
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")