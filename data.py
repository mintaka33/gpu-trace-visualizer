
base = 919760
data = []
with open('time.txt') as f:
    for line in f:
        a = int(line) - base
        data.append(a)

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