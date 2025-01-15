marks = []

print("Enter the marks of 10 students:")
for i in range(10):
    mark = float(input(f"Student {i + 1}: "))
    marks.append(mark)

print("\nMarks of 10 students are:")
for i, mark in enumerate(marks, start=1):
    print(f"Student {i}: {mark}")
