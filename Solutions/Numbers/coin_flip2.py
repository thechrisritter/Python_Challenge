# Coin Flip 2
# Performs "Coin Flip" in fewer lines.

import random

flips = [ random.randint(0, 1) for i in range(100) ]
heads = flips.count(0)
tails = flips.count(1)
for s in flips:
	msg = "Heads" if s==1 else "Tails"
	print(msg)
print("Heads count=%d, Tails count=%d" % (heads, tails))
input()
