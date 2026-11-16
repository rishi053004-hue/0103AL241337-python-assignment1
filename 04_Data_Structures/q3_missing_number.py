# Solution file
lst = [1,2,3,5]

n = len(lst) + 1

expected = n * (n + 1) // 2

print(expected - sum(lst))