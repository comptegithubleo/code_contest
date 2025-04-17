import sys
n = int(input())
for i in range(n):
	input = sys.stdin.readline().rstrip('\n')
	list = [int(x) for x in input.split(" ")]
	list.sort()
	print(" ".join(str(x) for x in list))
