import svgwrite
from svgwrite import cm, mm

(baseX, baseY, stepX, stepY) = (2, 2, 2, 10)
(numH, numV) = (100, 16)
(lineOffsetX, lineOffsetY) = (baseX + 6, baseY-0.5)
(endX, endY) = (lineOffsetX+numV*stepX, lineOffsetY+numH*stepY)
(svgWidth, svgHeigh) = (endX+2, endY+2)

dwg = svgwrite.Drawing(filename='visual.svg', size=(svgWidth*cm, svgHeigh*cm), debug=True)
shapes = dwg.add(dwg.g(id='shapes', fill='red'))
text = dwg.add(dwg.g(font_size=14))
hlines = dwg.add(dwg.g(id='hlines', stroke='blue'))

def drawLineH():
    for y in range(numH):
        text.add(dwg.text(str(y), ((baseX/2)*cm, (baseY+y*stepY)*cm)))
        hlines.add(dwg.line(start=(baseX*cm, (baseY+y*stepY)*cm), end=(endX*cm, (baseY+y*stepY)*cm)))

def drawLineV():
    for x in range(numV):
        text.add(dwg.text('engine'+str(x), (((lineOffsetX-0.5)+x*stepX)*cm, lineOffsetY*cm)))
        hlines.add(dwg.line(start=((lineOffsetX+x*stepX)*cm, lineOffsetY*cm), end=((lineOffsetX+x*stepX)*cm, endY*cm)))

def drawRect():
    (rectOffsetY, rectSizeH, rectSizeV) = (3, 1, 4)
    for y in range(numH):
        for x in range(numV):
            shapes.add(dwg.rect(insert=((lineOffsetX+x*stepX)*cm, (lineOffsetY+rectOffsetY+y*stepY)*cm), size=(rectSizeH*cm, rectSizeV*cm), fill='blue', stroke='red', stroke_width=1))

drawLineH()
drawLineV()
drawRect()

dwg.save()