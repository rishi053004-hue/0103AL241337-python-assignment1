# Solution file
n = int(input("Enter number: "))
sq = n * n

if str(sq).endswith(str(n)):
    print("Automorphic")
else:
    print("Not Automorphic")