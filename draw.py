import svgwrite
from svgwrite import cm, mm

dwg = svgwrite.Drawing(filename='time.svg', size=('100cm', '10000cm'), debug=True)
shapes = dwg.add(dwg.g(id='shapes', fill='red'))

def drawItem(data):
    basey = data[0]
    height = (data[1]-data[0])
    shapes.add(dwg.rect(insert=(100*mm, basey*mm), size=(10*mm, height*mm), fill='blue', stroke='red', stroke_width=1))
    basey = basey + height
    height = (data[2]-data[1])
    shapes.add(dwg.rect(insert=(100*mm, basey*mm), size=(10*mm, height*mm), fill='blue', stroke='red', stroke_width=1))
    basey = basey + height
    height = (data[3]-data[2])
    shapes.add(dwg.rect(insert=(100*mm, basey*mm), size=(10*mm, height*mm), fill='blue', stroke='red', stroke_width=1))
    basey = basey + height
    height = (data[4]-data[3])
    shapes.add(dwg.rect(insert=(100*mm, basey*mm), size=(10*mm, height*mm), fill='blue', stroke='red', stroke_width=1))
    basey = basey + height
    height = (data[5]-data[4])
    shapes.add(dwg.rect(insert=(100*mm, basey*mm), size=(10*mm, height*mm), fill='green', stroke='red', stroke_width=1))
    basey = basey + height

def getTiming(line):
        ret = '0'
        l = line.split(' ')
        for w in l:
            if ":" in w and "." in w:
                ret = ''.join(w.split(':')[0].split('.'))
        return int(ret)

data = []
with open('mpeg2vldemo-trace.txt') as f:
    base = 0
    tag = 'ring=2'
    for line in f:
        if tag in line:
            a = getTiming(line)
            if base == 0:
                base = a
            data.append(a-base)

time = []
count = 0
group = []
for d in data:
    group.append(d)
    count = count + 1
    if count%6 == 0:
        time.append(group)
        group = []

for t in time:
    print(t)
    drawItem(t)
dwg.save()
