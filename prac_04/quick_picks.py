import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45

amount_of_picks = int(input("How many quick  picks? "))
while amount_of_picks < 0:
    print("Invalid amount")
    amount_of_picks = int(input("How many quick picks? "))

for i in range(amount_of_picks):
    quick_pick = []
    for n in range(NUMBERS_PER_LINE):
        number = random.randint(MIN, MAX)
        while number in quick_pick:
            number = random.randint(MIN, MAX)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join("{:2}".format(number) for number in quick_pick))

