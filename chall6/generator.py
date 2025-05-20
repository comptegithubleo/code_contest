import random
import math 

filename = "sample"
nbr_paths = 3
nbr_nodes_min = 2
nbr_nodes_max = 4


max_path = 99999
index = 0
smallest_path = 0

with open(filename + ".in", "w") as f:
    f.write(f"{nbr_paths}\n")

    minimum_path = 99999
    for k in range(nbr_paths):

        nodes = []
        for j in range(random.randint(nbr_nodes_min, nbr_nodes_max)):
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            nodes.append((x, y))

        # from random points, constructs the shortest path of points
        x = 0
        y = 0
        path = [(0,0)]
        for i in range(len(nodes)-1):
            minimum = 9999
            for j in range(len(nodes)):
                #print("checking node: " + str(nodes[j]))
                distance = math.sqrt(pow(nodes[j][0] - x, 2) + pow(nodes[j][1] - y, 2))
                #print("distance: " + str(distance) + " from: " + str(x) + "," + str(y))
                if distance < minimum:
                    #print("found new minimum: " + str(distance))
                    minimum = distance
                    index = j
            
            #print("added node: " + str(nodes[index]))
            x = nodes[index][0]
            y = nodes[index][1]
            path.append(nodes[index])
            nodes.remove(nodes[index])

        # from the shortest path of those random points, computes the length
        x = 0
        y = 0
        print(path)
        length = 0
        for i in range(len(path)):
            length += math.sqrt(pow(path[i][0] - x, 2) + pow(path[i][1] - y, 2))
            #print("length: " + str(length) + " from: " + str(x) + "," + str(y) + " to : " + str(path[i][0]) + "," + str(path[i][1]))
            x = path[i][0]
            y = path[i][1]
            if i != len(path)-1:
                f.write(f"({path[i][0]},{path[i][1]});")
            else:
                f.write(f"({path[i][0]},{path[i][1]})\n")

        print("total length: " + str(length))



with open(filename + ".ans", "w") as f:
    print("ok")
    #f.write(f"{",".join(str(x) for x in solution)}")