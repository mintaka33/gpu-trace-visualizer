
data = []

def getTiming(line):
        ret = '0'
        l = line.split(' ')
        for w in l:
            if ":" in w and "." in w:
                ret = ''.join(w.split(':')[0].split('.'))
        return int(ret)

with open('mpeg2vldemo-trace.txt') as f:
    base = 0
    tag = 'ring=2'
    for line in f:
        if tag in line:
            a = getTiming(line)
            if base == 0:
                base = a
            data.append(a-base)

print(data)

time = []
count = 0
group = []
for d in data:
    group.append(d)
    count = count + 1
    if count%6 == 0:
        time.append(group)
        group = []

print(time)