import svgwrite
from svgwrite import cm, mm

dwg = svgwrite.Drawing(filename='visual.svg', size=('100cm', '1000cm'), debug=True)
shapes = dwg.add(dwg.g(id='shapes', fill='red'))
text = dwg.add(dwg.g(font_size=14))
hlines = dwg.add(dwg.g(id='hlines', stroke='blue'))

def drawLineX():
    for y in range(100):
        text.add(dwg.text(str(y), (1*cm, (2+y*10)*cm)))
        hlines.add(dwg.line(start=(2*cm, (2+y*10)*cm), end=(40*cm, (2+y*10)*cm)))

def drawLineY():
    for x in range(16):
        text.add(dwg.text('engine'+str(x), ((7.5+x*2)*cm, 1*cm)))
        hlines.add(dwg.line(start=((8+x*2)*cm, 1*cm), end=((8+x*2)*cm, 1000*cm)))

def drawItem():
    for y in range(100):
        for x in range(16):
            shapes.add(dwg.rect(insert=((8+x*2)*cm, (3+y*10)*cm), size=(1*cm, 4*cm), fill='blue', stroke='red', stroke_width=1))

drawLineX()
drawLineY()
drawItem()

dwg.save()