import svgwrite
from svgwrite import cm, mm

dwg = svgwrite.Drawing(filename='time.svg', size=('10000cm', '10cm'), debug=True)
shapes = dwg.add(dwg.g(id='shapes', fill='red'))

def drawItem(data):
    basex = data[0]
    width = (data[1]-data[0])
    shapes.add(dwg.rect(insert=(basex*mm, 10*mm), size=(width*mm, 1*mm), fill='blue', stroke='red', stroke_width=1))
    basex = basex + width
    width = (data[2]-data[1])
    shapes.add(dwg.rect(insert=(basex*mm, 10*mm), size=(width*mm, 1*mm), fill='blue', stroke='red', stroke_width=1))
    basex = basex + width
    width = (data[3]-data[2])
    shapes.add(dwg.rect(insert=(basex*mm, 10*mm), size=(width*mm, 1*mm), fill='blue', stroke='red', stroke_width=1))
    basex = basex + width
    width = (data[4]-data[3])
    shapes.add(dwg.rect(insert=(basex*mm, 10*mm), size=(width*mm, 1*mm), fill='blue', stroke='red', stroke_width=1))
    basex = basex + width
    width = (data[5]-data[4])
    shapes.add(dwg.rect(insert=(basex*mm, 10*mm), size=(width*mm, 1*mm), fill='green', stroke='red', stroke_width=1))
    basex = basex + width

base = 157473
data = []
with open('time.txt') as f:
    for line in f:
        a = int(line) - base
        data.append(a)
#print(data)

time = []
count = 0
group = []
for d in data:
    group.append(d)
    count = count + 1
    if count%6 == 0:
        time.append(group)
        group = []
#print(time)

for t in time:
    print(t)
    drawItem(t)
dwg.save()
