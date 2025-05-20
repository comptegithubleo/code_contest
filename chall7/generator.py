import random

bag_size = 60000 #cm3 = 40L

def get_solution_from(t, items):
    solution = []
    for i in range(len(t)):
        if t[i] == 1:
            solution.append(items[i])
    
    return solution

def bag_space_for(t, items):
    total = 0
    for i in range(len(t)):
        if t[i] == 1:
            #print("adding item " + str(items[i]))
            total += items[i]
    
    return bag_size - total

def next(t):
    i = len(t)-1
    while i >= 0 and t[i] == 1:
        t[i] = 0
        i = i - 1
    if i == -1:
        return 0
    t[i] = 1
    return 1

def main():
    filename = "secret1"
    nbr = 5
    total = 0
    items = []

    while total < bag_size / 3:
        item = int(random.randrange(1000, 4000))
        total += item
        items.append(item)

    for i in range(int(len(items)/2)):
        item = int(random.triangular(70000))
        total += item
        items.append(item)

    t = [0]*len(items)

    minimum = bag_size
    solution = []
    while next(t):
        #print(t)
        space_left = bag_space_for(t, items)
        if space_left < 0 or space_left > bag_size:
            #print("bounds error with: " + str(space_left))
            continue
        elif space_left > minimum:
            #print("already found smaller than " + str(space_left))
            continue
        else:
            #print("guessed " + str(space_left))
            minimum = space_left
            solution = get_solution_from(t, items)
        print(solution)    
    random.shuffle(items)
    random.shuffle(solution)
    print(items)
    print(minimum)
    print(solution)
    print(sum(solution))

    with open(filename + ".in", "w") as f:
        f.write(f"{len(items)}\n")
        f.write(f"{"\n".join(str(x) for x in items)}")

    with open(filename + ".ans", "w") as f:
        f.write(f"{",".join(str(x) for x in solution)}")

main()