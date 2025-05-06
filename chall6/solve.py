import sys

n = int(input())

units = ["Hz", "daHz", "hHz", "kHz", "MHz", "GHz"]



for i in range(n):
    tmp = sys.stdin.readline().rstrip('\n')

    if tmp.endswith('daHz'):
        all_frequencies.append(float(''.join(tmp[:-4])) * 10**-5)
    elif tmp.endswith('hHz'):
        all_frequencies.append(float(''.join(tmp[:-3])) * 100)
    elif tmp.endswith('kHz'):
        all_frequencies.append(float(''.join(tmp[:-3])) * 1000)
    elif tmp.endswith('MHz'):
        all_frequencies.append(float(''.join(tmp[:-3])) * 1000000)
    elif tmp.endswith('GHz'):
        all_frequencies.append(float(''.join(tmp[:-3])) * 1000000000)
    elif tmp.endswith('Hz'):
        all_frequencies.append(float(''.join(tmp[:-2])))
    else:
        print("couldn't parse unit")
    
    print(all_frequencies)
