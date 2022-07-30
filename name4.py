import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")  # Com o sys.exit eu garanto que, em qualquer das duas condições, o programa será
    # concluído sem executar a linha 7.
print("Hello, my name is", sys.argv[1])
