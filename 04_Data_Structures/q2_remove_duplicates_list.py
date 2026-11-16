# Solution file
lst = [1,2,3,2,4,1,5]

result = []

for item in lst:
    if item not in result:
        result.append(item)

print(result)