import sys
n = int(input())

line = list(sys.stdin.readline().rstrip('\n'))

for i in range(n-1):
    tmp = list(sys.stdin.readline().rstrip('\n'))

    for j in range(len(tmp)):
        if tmp[j] != ' ':
            line[j] = tmp[j]

print(''.join(line))