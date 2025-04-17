import random
import string
import math

filename="secret1"
lineNumber = 0
content = ""
MIN = 15600000000000000
MAX = 17000000000000000
minimum = MAX

with open(filename + ".in", "w") as f:
    for i in range(0, random.randrange(200, 300)):
        price = random.randrange(MIN, MAX)
        price = math.ceil(price)
        price = price * 10**-16
        if price < minimum:
            minimum = price
        content += f"{price}\n"
        lineNumber += 1

    f.write(f"{lineNumber}\n")
    f.write(content)

with open(filename + ".ans", "w") as f:
    f.write(f"{minimum}\n")
    print(minimum)


print("number of lines " + str(lineNumber))