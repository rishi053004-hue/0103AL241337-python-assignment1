# Solution file
s = input("Enter string: ")

clean = s.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
