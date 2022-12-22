import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")

num_lines = 0
try:
    for arg in sys.argv[1:]:
        with open(arg) as file:
            lines = file.readlines()
            for line in lines:
                if line.isspace() is False and line.lstrip().startswith("#") is False:
                    num_lines += 1
    print(num_lines)
except FileNotFoundError:
    sys.exit("File does not exist")
