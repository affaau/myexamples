import random
import time

for _ in range(20):
    print("\r{: <16}{: <16}".format(random.randint(0,1000), random.randint(0,1000)), end="")
    time.sleep(0.4)

print("")

