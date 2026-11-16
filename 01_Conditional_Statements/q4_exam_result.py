# Solution file
marks = []
for i in range(5):
    marks.append(int(input(f"Subject {i+1}: ")))

if min(marks) < 33:
    print("Fail")
else:
    percentage = sum(marks) / 5

    if percentage >= 60:
        print("First Division")
    elif percentage >= 50:
        print("Second Division")
    elif percentage >= 40:
        print("Third Division")
    else:
        print("Fail")