import sys
n = int(input())

total = 0
for i in range(n):
    line = sys.stdin.readline().rstrip('\n')
    total += int(line[2:])

print(str(total)[:1] + "." + str(total)[1:])