# Solution file
library = {
    "Python": 5,
    "Java": 3
}

book = input("Book name: ")

if book in library:
    print("Quantity:", library[book])
else:
    print("Book not found")