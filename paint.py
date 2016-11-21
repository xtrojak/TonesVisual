"""
USAGE: python paint.py "<one1 tone2 ... toneN"
"""

import svgwrite
import sys
from subprocess import call

def createString(array):
    output = ""
    for item in sorted(array):
        output += item.__str__() + ", "
    return output[:-2]

img = svgwrite.Drawing(filename='hmatnik.svg', size=(1060, 400), debug=True)
img.add(img.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='rgb(255,255,255)'))


input_tones = sys.argv[-1]
input_tones = input_tones.split(" ")

default_tuning = ['e2', 'h1', 'g1', 'd1', 'a', 'e']

tones = [['e', 'f', 'f#', 'g', 'g#', 'a', 'b', 'h', 'c', 'c#', 'd', 'd#', 'e'],
         ['h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'b', 'h'],
         ['g', 'g#', 'a', 'b', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g'],
         ['d', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'b', 'h', 'c', 'c#', 'd'],
         ['a', 'b', 'h', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a'],
         ['e', 'f', 'f#', 'g', 'g#', 'a', 'b', 'h', 'c', 'c#', 'd', 'd#', 'e']]

for i in range(7):
    img.add(img.line((50, 50 + i*50), (1010, 50 + i*50), stroke='black'))
    if i != 6:
        img.add(img.text(default_tuning[i], insert=(30, 80 + i*50), fill='black'))

for i in range(13):
    img.add(img.line((50 + i*80, 50), (50 + i*80, 350), stroke='black'))
    if i != 12:
        img.add(img.text(i+1, insert=(80 + i*80, 30), fill='black'))

for string in range(6):
    for bar in range(13):
        if tones[string][bar] in input_tones:
            img.add(img.circle(center=(10 + bar*80, 25 + (string + 1)*50), r=3, stroke='red', stroke_width=3))

img.add(img.text("tones: " + createString(input_tones), insert=(50, 380), fill='black'))

img.save()

call(["inkscape", "-z", "-e", "hmatnik.png", "hmatnik.svg"])
call(["rm", "hmatnik.svg"])