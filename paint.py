import svgwrite
import sys

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

# paint strings
for i in range(7):
    color = "black"
    img.add(img.line((50, 50 + i*50), (1010, 50 + i*50), stroke=color))
    if i != 6:
        if tuning[i] in input_tones:
            color = "red"
        img.add(img.text(tuning[i], insert=(30, 80 + i*50), fill=color))

# paint bars
for i in range(13):
    img.add(img.line((50 + i*80, 50), (50 + i*80, 350), stroke='black'))
    if i != 12:
        img.add(img.text(i+1, insert=(80 + i*80, 30), fill='black'))

# paint tones
for string in range(6):
    for bar in range(12):
        if tones[string][bar] in input_tones:
            img.add(img.text(tones[string][bar], insert=(85 + bar*80, 30 + (string + 1)*50), fill='red'))

img.add(img.text("tones: " + ", ".join(sorted(input_tones)), insert=(50, 380), fill='black'))
img.save()