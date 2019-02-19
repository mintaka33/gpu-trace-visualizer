import svgwrite
from svgwrite import cm, mm

dwg = svgwrite.Drawing(filename='time.svg', size=('100cm', '10000cm'), debug=True)
shapes = dwg.add(dwg.g(id='shapes', fill='red'))
text = dwg.add(dwg.g(font_size=14))

def drawItem(data, i):
    basey = 20 + data[0]
    height = (data[1]-data[0])
    text.add(dwg.text(str(i), (80*mm, basey*mm)))
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
        if "i915_request" in w:
            tag = w.split(':')[0]
        if "seqno" in w:
            idx = w.split('=')[1].split(',')[0]
    return [int(idx), tag, int(ret)]

def readData(data):
    with open('log.txt') as f:
        tag = 'ring=2'
        for line in f:
            if tag in line:
                a = getTiming(line)
                data.append(a)

def formatData(data, data2):
    curIdx = data[0][0]
    group = [curIdx, 0, 0, 0, 0, 0, 0]
    for frame in data:
        if curIdx == frame[0]:
             if frame[1] == "i915_request_queue":
                group[1] = frame[2]
             elif frame[1] == "i915_request_add":
                group[2] = frame[2]
             elif frame[1] == "i915_request_submit":
                group[3] = frame[2]
             elif frame[1] == "i915_request_execute":
                group[4] = frame[2]
             elif frame[1] == "i915_request_in":
                group[5] = frame[2]
             elif frame[1] == "i915_request_out":
                group[6] = frame[2]
        else:
            data2.append(group)
            curIdx = frame[0]
            group = [curIdx, 0, 0, 0, 0, 0, 0]

def parseTrace(time):
    data = []
    readData(data)
    formatData(data, time)

time = []
parseTrace(time)

i = 0
for t in time:
    drawItem(t, i)
    i = i + 1
dwg.save()
