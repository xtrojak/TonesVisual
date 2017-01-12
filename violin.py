import svgwrite
import sys

def myLine(image, fromPoint, toPoint, color):
	image.add(image.line(fromPoint, toPoint, stroke=color))

def myText(image, possition, text, color):
	image.add(image.text(text, insert=possition, fill=color))

img = svgwrite.Drawing(filename='result_violin.svg', size=(1060, 300), debug=True)
img.add(img.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='rgb(255,255,255)'))

input_tones = sys.argv[-1]
input_tones = input_tones.split(" ")

default_tuning = ['g', 'd', 'a', 'e']
tuning = default_tuning

tones = [['f', 'f#', 'g', 'g#', 'a', 'a#', 'h', 'c', 'c#', 'd', 'd#', 'e'],
         ['a#', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a'],
         ['d#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'h', 'c', 'c#', 'd'],
         ['g#', 'a', 'a#', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g']]
         

color = "black"

# paint strings
myLine(img, (50, 50), (1010, 50), color)
for i in range(4):
    color = "black"
    myLine(img, (50, 50 + (i+1)*50), (1010, 50 + (i+1)*50), color)
    if tuning[i] in input_tones:
        color = "red"
    myText(img, (30, 80 + i*50), tuning[i], color)

color = "black"

# paint bars
myLine(img, (50, 50), (50, 250), color)
for i in range(12):
    myLine(img, (50 + (i+1)*80, 50), (50 + (i+1)*80, 250), color)
    myText(img, (80 + i*80, 30), str(i+1), color)

color = "red"

# paint tones
for string in range(4):
    for bar in range(12):
        if tones[string][bar] in input_tones:
        	myText(img, (85 + bar*80, 30 + (string + 1)*50), tones[string][bar], color)

myText(img, (50, 280), "tones: " + ", ".join(sorted(input_tones)), color)
img.save()