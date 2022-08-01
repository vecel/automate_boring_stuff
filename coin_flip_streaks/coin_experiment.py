# What are the chances to get 6 tails or 6 heads in a row in 100 following coin flips?
# Evaluate chances to get [STREAK] tails or heads in a row in [FLIPS] following coin flips
import random

STREAK = 5
FLIPS = 10

TRIES = 10000

def symulate() -> str:
    result = ''
    for i in range(FLIPS):
        if random.randint(0, 1) == 1:
            result += 'T'
        else:
            result += 'H'
    return result

number_of_streaks = 0
for i in range(TRIES):
    test = symulate()

    if 'T' * STREAK in test or 'H' * STREAK in test:
        number_of_streaks += 1

print(f'Chances to have {STREAK} tails or heads in a row, in {FLIPS} ' \
    f'following coin flips are approximately {round(number_of_streaks / TRIES * 100, 2)} %')