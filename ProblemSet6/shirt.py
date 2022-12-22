import sys
from os.path import splitext
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
file1 = splitext(sys.argv[1])
file2 = splitext(sys.argv[2])
if file1[1] and file2[1] not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
if file1[1].lower() != file2[1].lower():
    sys.exit("Input and output have different extensions")

try:
    photo = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")
size = shirt.size
photo2 = ImageOps.fit(photo, size)
photo2.paste(shirt, shirt)
photo2.save(sys.argv[2])
