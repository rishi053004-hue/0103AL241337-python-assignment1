# Solution file
balance = 5000
amount = int(input())

if amount > balance:
    raise Exception("Insufficient Balance")

balance -= amount
print("Remaining Balance:", balance)