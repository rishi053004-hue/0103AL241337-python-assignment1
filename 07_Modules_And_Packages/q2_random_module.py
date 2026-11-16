# Solution file
import random
import string

otp = random.randint(1000, 9999)

password = ''.join(
    random.choices(string.ascii_letters + string.digits, k=8)
)

numbers = random.sample(range(1, 100), 5)

print(otp)
print(password)
print(numbers)