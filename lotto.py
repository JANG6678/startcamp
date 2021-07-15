import random

numbers = range(1,46)

print(random.sample(numbers,7))
lotto = random.sample(numbers,7)

print('로또 번호는', lotto)