import svgwrite
import sys

# definitions

def myLine(image, fromPoint, toPoint, color):
    image.add(image.line(fromPoint, toPoint, stroke=color))

def paintVerticalLine(image, size, i):
    myLine(image, (50 + (i+1)*80, 50), (50 + (i+1)*80, size), "black")

def paintHorizontalLine(image, i):
    myLine(image, (50, 50 + (i+1)*50), (1010, 50 + (i+1)*50), "black")

def myText(image, possition, text, color):
    image.add(image.text(text, insert=possition, fill=color))

def paintTone(image, i, j, tone):
    myText(img, (85 + i*80, 30 + (j + 1)*50), tone, "red")

def writeBarNumber(image, i):
    myText(image, (80 + i*80, 30), str(i+1), "black")

def writeBaseTone(image, i, tone, color):
    myText(image, (30, 80 + i*50), tone, color)

def writeTextUnderPicture(image, i, tones):
    myText(image, (50, i), "tones: " + ", ".join(sorted(set(input_tones))), "black")

def getViolinAttributes():
    tones = [['f', 'f#', 'g', 'g#', 'a', 'a#', 'h', 'c', 'c#', 'd', 'd#', 'e'],
             ['a#', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a'],
             ['d#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'h', 'c', 'c#', 'd'],
             ['g#', 'a', 'a#', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g']]
    default_tuning = ['g', 'd', 'a', 'e']
    size = 0
    return size, 4, tones, default_tuning

def getGuitarAttributes():
    tones = [['f', 'f#', 'g', 'g#', 'a', '#a', 'h', 'c', 'c#', 'd', 'd#', 'e'],
             ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', '#a', 'h'],
             ['g#', 'a', '#a', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g'],
             ['d#', 'e', 'f', 'f#', 'g', 'g#', 'a', '#a', 'h', 'c', 'c#', 'd'],
             ['#a', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a'],
             ['f', 'f#', 'g', 'g#', 'a', '#a', 'h', 'c', 'c#', 'd', 'd#', 'e']]
    default_tuning = ['e', 'h', 'g', 'd', 'a', 'e']
    size = 100
    return size, 6, tones, default_tuning


# handle input

argument = sys.argv[-2]
input_tones = sys.argv[-1]
input_tones = input_tones.split(" ")

# set attributes according to the choosen tool

if argument == '-v': #if guitar is choosen
    size, iterate, tones, tuning = getViolinAttributes()
else:
    size, iterate, tones, tuning = getGuitarAttributes()

img = svgwrite.Drawing(filename='result.svg', size=(1060, 300 + size), debug=True)
img.add(img.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='rgb(255,255,255)'))

color = "black"

paintVerticalLine(img, 250 + size, -1)
for i in range(12):
    paintVerticalLine(img, 250 + size, i)
    writeBarNumber(img, i)

paintHorizontalLine(img, -1)
for string in range(iterate):
    color = "black"
    paintHorizontalLine(img, string)
    if tuning[string] in input_tones:
        color = "red"
    writeBaseTone(img, string, tuning[string], color)

    for bar in range(12):
        color = "red"
        if tones[string][bar] in input_tones:
            paintTone(img, bar, string, tones[string][bar])

writeTextUnderPicture(img, 280 + size, input_tones)
img.save()