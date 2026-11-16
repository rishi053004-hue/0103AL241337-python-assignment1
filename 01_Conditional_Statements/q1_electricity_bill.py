# Solution file
units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 200 * 7 + (units - 300) * 10

if bill > 2000:
    bill += bill * 0.05

print("Bill Amount =", bill)

print("rishi")