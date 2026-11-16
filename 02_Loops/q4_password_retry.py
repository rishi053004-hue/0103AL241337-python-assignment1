# Solution file
password = "admin123"

for i in range(3):
    p = input("Enter Password: ")

    if p == password:
        print("Access Granted")
        break
else:
    print("Blocked")