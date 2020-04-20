# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
from datetime import date
import random

print(random.random())
print(int(random.random()*10))
# 2) Use the datetime library together with the random number to generate a random, unique value.


year = random.randint(0, 2020)
month = random.randint(1, 12)
day = random.randint(1, 30)

random_date = date(year, month, day)
print(random_date)
