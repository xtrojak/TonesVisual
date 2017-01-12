import svgwrite
import sys

def myLine(image, fromPoint, toPoint, color):
    image.add(image.line(fromPoint, toPoint, stroke=color))

def myText(image, possition, text, color):
    image.add(image.text(text, insert=possition, fill=color))

isGuitar = sys.argv[-2]
input_tones = sys.argv[-1]
input_tones = input_tones.split(" ")

tones_guitar = [['f', 'f#', 'g', 'g#', 'a', '#a', 'h', 'c', 'c#', 'd', 'd#', 'e'],
                ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', '#a', 'h'],
                ['g#', 'a', '#a', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g'],
                ['d#', 'e', 'f', 'f#', 'g', 'g#', 'a', '#a', 'h', 'c', 'c#', 'd'],
                ['#a', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a'],
                ['f', 'f#', 'g', 'g#', 'a', '#a', 'h', 'c', 'c#', 'd', 'd#', 'e']]

tones_violin = [['f', 'f#', 'g', 'g#', 'a', 'a#', 'h', 'c', 'c#', 'd', 'd#', 'e'],
                ['a#', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a'],
                ['d#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'h', 'c', 'c#', 'd'],
                ['g#', 'a', 'a#', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g']]

default_guitar_tuning = ['e', 'h', 'g', 'd', 'a', 'e']
default_violin_tuning = ['g', 'd', 'a', 'e']
tuning = default_violin_tuning
tones = tones_violin

xsize = 300
iterate = 4
line = 250
text = 280
if isGuitar == '-g': #if guitar is choosen
    xsize = 400
    iterate = 6
    line = 350
    text = 380
    tuning = default_guitar_tuning
    tones = tones_guitar

img = svgwrite.Drawing(filename='result.svg', size=(1060, xsize), debug=True)
img.add(img.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='rgb(255,255,255)'))

color = "black"

# paint vertical lines
myLine(img, (50, 50), (50, line), color)
for i in range(12):
    myLine(img, (50 + (i+1)*80, 50), (50 + (i+1)*80, line), color)
    myText(img, (80 + i*80, 30), str(i+1), color)

myLine(img, (50, 50), (1010, 50), color) # paint horizontal line
for string in range(iterate):
    color = "black"
    myLine(img, (50, 50 + (string+1)*50), (1010, 50 + (string+1)*50), color)  # paint horizontal lines
    if tuning[string] in input_tones:
        color = "red"
    myText(img, (30, 80 + string*50), tuning[string], color)  # paint main tones

    for bar in range(12):
        color = "red"
        if tones[string][bar] in input_tones:
            myText(img, (85 + bar*80, 30 + (string + 1)*50), tones[string][bar], color)  # paint other tones

myText(img, (50, text), "tones: " + ", ".join(sorted(input_tones)), "black")    # write text under picture
img.save()