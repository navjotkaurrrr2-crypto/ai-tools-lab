def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


marks = [80, 75, 90, 85, 70]

average = calculate_average(marks)

print("Marks:", marks)
print("Average:", average)