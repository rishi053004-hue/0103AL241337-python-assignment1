# Solution file
students = {
    "A": 70,
    "B": 50,
    "C": 25
}

topper = max(students, key=students.get)
average = sum(students.values()) / len(students)

failures = [s for s,m in students.items() if m < 33]

print("Topper:", topper)
print("Average:", average)
print("Failures:", failures)