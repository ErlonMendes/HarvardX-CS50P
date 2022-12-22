import sys
from pyfiglet import Figlet
figlet = Figlet()

if len(sys.argv) < 3 or sys.argv[1] != "-f" or sys.argv[2:] in figlet.getFonts():
    sys.exit("Invalid usage")

for f in sys.argv[2:]:
    figlet.setFont(font=f)
    s = input("Input: ")
    print("Output: ")
    print(figlet.renderText(s))
