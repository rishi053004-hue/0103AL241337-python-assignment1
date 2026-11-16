# Solution file
n = 5

# Triangle
for i in range(1, n + 1):
    print("*" * i)

# Pyramid
for i in range(n):
    print(" " * (n - i) + "*" * (2 * i + 1))

# Diamond
for i in range(n):
    print(" " * (n - i) + "*" * (2 * i + 1))

for i in range(n - 2, -1, -1):
    print(" " * (n - i) + "*" * (2 * i + 1))