# Solution file
start = int(input("Start: "))
end = int(input("End: "))

for i in range(start, end + 1):
    if str(i) == str(i)[::-1]:
        print(i)
