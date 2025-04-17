import sys
n = int(sys.stdin.readline().rstrip('\n'))
minimum = sys.stdin.readline().rstrip('\n')

for i in range(n-1):
    line = sys.stdin.readline().rstrip('\n')
    if float(line) < float(minimum):
        minimum = line

print(minimum)