import svgwrite
import sys

def myLine(image, fromPoint, toPoint, color):
	image.add(image.line(fromPoint, toPoint, stroke=color))

def myText(image, possition, text, color):
	image.add(image.text(text, insert=possition, fill=color))

img = svgwrite.Drawing(filename='hmatnik.svg', size=(1060, 400), debug=True)
img.add(img.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='rgb(255,255,255)'))

input_tones = sys.argv[-1]
input_tones = input_tones.split(" ")

default_tuning = ['e', 'h', 'g', 'd', 'a', 'e']
tuning = default_tuning

tones = [['f', 'f#', 'g', 'g#', 'a', 'b', 'h', 'c', 'c#', 'd', 'd#', 'e'],
         ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'b', 'h'],
         ['g#', 'a', 'b', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g'],
         ['d#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'b', 'h', 'c', 'c#', 'd'],
         ['b', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a'],
         ['f', 'f#', 'g', 'g#', 'a', 'b', 'h', 'c', 'c#', 'd', 'd#', 'e']]

color = "black"

# paint strings
myLine(img, (50, 50), (1010, 50), color)
for i in range(6):
    color = "black"
    myLine(img, (50, 50 + (i+1)*50), (1010, 50 + (i+1)*50), color)
    if tuning[i] in input_tones:
        color = "red"
    myText(img, (30, 80 + i*50), tuning[i], color)

color = "black"

# paint bars
myLine(img, (50, 50), (50, 350), color)
for i in range(12):
    myLine(img, (50 + (i+1)*80, 50), (50 + (i+1)*80, 350), color)
    myText(img, (80 + i*80, 30), str(i+1), color)

color = "red"

# paint tones
for string in range(6):
    for bar in range(12):
        if tones[string][bar] in input_tones:
        	myText(img, (85 + bar*80, 30 + (string + 1)*50), tones[string][bar], color)

myText(img, (50, 380), "tones: " + ", ".join(sorted(input_tones)), color)
img.save()