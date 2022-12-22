import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:]:  # Pega um "slice", um intervalo de 1 até end
    print("Hello, my name is", arg)
