# Coin flip
# flips a coin 100 times and tells the user
# how many times it lands on heads or tails.

import random

flips = 0
heads = 0
tails = 0
while flips < 100:
    flips += 1
    coin = random.randint(0, 1)
    if coin == 0:
        print("Heads")
        heads += 1
    if coin == 1:
        print("Tails")
        tails += 1
total = flips
print("The coin was flipped", total, "times.")
print("It landed on heads", heads, "times.")
print("It landed on tails", tails, "times.")

input()
