# Coin Flip 2
# Performs "Coin Flip" in significantly less lines.

import random

samples = [ random.randint(0, 1) for i in range(100) ]
heads = samples.count(0)
tails = samples.count(1)
for s in samples:
	msg = "Heads" if s==1 else "Tails"
	print(msg)
print("Heads count=%d, Tails count=%d" % (heads, tails))
input("\n\nPress the enter key to exit.")
