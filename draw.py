import svgwrite
from svgwrite import cm, mm

dwg = svgwrite.Drawing(filename='time.svg', size=('100cm', '3000cm'), debug=True)
shapes = dwg.add(dwg.g(id='shapes', fill='red'))
text = dwg.add(dwg.g(font_size=14))
hlines = dwg.add(dwg.g(id='hlines', stroke='blue'))

def drawLine():
    for y in range(100):
        hlines.add(dwg.line(start=(2*cm, (2+y*100)*cm), end=(40*cm, (2+y*100)*cm)))

def drawItem(data, i, offset):
    basey = 20 + data[0] - offset
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
    text.add(dwg.text(str(height)+' us', (120*mm, (basey+height/2)*mm)))
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
    for frame in data:
        seqno = frame[0]
        if seqno not in data2:
            data2[seqno] = [0, 0, 0, 0, 0, 0]
        if frame[1] == "i915_request_queue":
            data2[seqno][0] = frame[2]
        elif frame[1] == "i915_request_add":
            data2[seqno][1] = frame[2]
        elif frame[1] == "i915_request_submit":
            data2[seqno][2] = frame[2]
        elif frame[1] == "i915_request_execute":
            data2[seqno][3] = frame[2]
        elif frame[1] == "i915_request_in":
            data2[seqno][4] = frame[2]
        elif frame[1] == "i915_request_out":
            data2[seqno][5] = frame[2]

def parseTrace(time):
    data = []
    readData(data)
    formatData(data, time)

time = {}
parseTrace(time)

drawLine()

keys = list(time.keys())
keys.sort()
offset = time[keys[0]][0]
for k in keys:
    #print(time[k])
    drawItem(time[k], k, offset)

dwg.save()
