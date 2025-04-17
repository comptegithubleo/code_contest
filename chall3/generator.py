import random
import string

filename="secret"
nbrLists = random.randrange(3,6)
goal = ""
for i in range(0, 10):
    if round(random.random()):
        goal += random.choice(string.ascii_letters).upper()
    else:
        goal += str(random.randrange(0, 10))


with open(filename + ".in", "w") as f:
    list_of_lists = [[' ' for i in range(0, len(goal))] for _ in range(nbrLists)]

    for i in range(len(goal)):
        list_of_lists[random.randrange(0, nbrLists)][i] = goal[i]

    f.write(f"{nbrLists}\n")
    for i in range(nbrLists):
        list_of_lists[i] = ''.join(list_of_lists[i])
        f.write(f"{list_of_lists[i]}\n")

with open(filename + ".ans", "w") as f:
    f.write(f"{goal}\n")
    print(goal)
