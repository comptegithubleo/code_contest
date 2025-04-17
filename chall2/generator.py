import random
import string
from decimal import *

filename="sample2"
total = 0
goal = 392422818
goal = 112987531
lineNumber = 0
content = ""

with open(filename + ".in", "w") as f:
    while True:
        serialnumber = random.randrange(100000, 999999)
        total += serialnumber
        if total >= goal:
            total -= total - goal + random.randrange(-3, 3)
            goal = total
            print(total)
            break

        randomLetter1 = random.choice(string.ascii_letters).upper()
        randomLetter2 = random.choice(string.ascii_letters).upper()

        content += f"{randomLetter1}{randomLetter2}{serialnumber}\n"
        lineNumber += 1

    f.write(f"{lineNumber}\n")
    f.write(content)

with open(filename + ".ans", "w") as f:
    goal = goal*10**-8
    f.write(f"{goal}\n")
    print(goal)


print("number of lines " + str(lineNumber))