# Solution file
t = (1,2,3,4,5)

first, *middle, last = t

new_tuple = (last, *middle, first)

print(new_tuple)