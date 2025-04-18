import random
import string
from decimal import *

filename="test"
total = 0
goal = 392422818
goal = 1471611
lineNumber = 0
content = ""

with open(filename + ".in", "w") as f:
    while total < goal:

        randomLetter1 = random.choice(string.ascii_letters).upper()
        randomLetter2 = random.choice(string.ascii_letters).upper()
        serialnumber = random.randrange(100000, 999999)
        total += serialnumber
        print(total)
        content += f"{randomLetter1}{randomLetter2}{serialnumber}\n"
        print(randomLetter1 + randomLetter2 + str(serialnumber))
        lineNumber += 1

    f.write(f"{lineNumber}\n")
    f.write(content)

with open(filename + ".ans", "w") as f:
    total = str(total)[:1] + "." + str(total)[1:]
    f.write(f"{total}\n")
    print(total)


print("number of lines " + str(lineNumber))