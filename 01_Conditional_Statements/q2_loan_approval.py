# Solution file
salary = int(input("Salary: "))
credit = int(input("Credit Score: "))
age = int(input("Age: "))

if salary >= 30000 and credit >= 700 and 21 <= age <= 60:
    print("Approved")
elif salary >= 25000 and credit >= 650:
    print("Conditionally Approved")
else:
    print("Rejected")