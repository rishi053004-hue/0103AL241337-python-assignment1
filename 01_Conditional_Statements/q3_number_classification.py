# Solution file
n = int(input("Enter number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

print("Even" if n % 2 == 0 else "Odd")

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")