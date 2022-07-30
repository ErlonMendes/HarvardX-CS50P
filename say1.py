import sys
from sayings1 import hello  # Vai usar o sayings1.py como uma biblioteca pessoal

if len(sys.argv) == 2:
    hello(sys.argv[1])
# Infelizmente, python say1.py Erlon resulta em três respostas: Hello, world, Goodbye, world e Hello, Erlon.
