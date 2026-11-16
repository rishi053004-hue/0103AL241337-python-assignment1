# Solution file
a = int(input())
b = int(input())

small = min(a, b)
hcf = 1

for i in range(1, small + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

lcm = (a * b) // hcf

print("HCF =", hcf)
print("LCM =", lcm)