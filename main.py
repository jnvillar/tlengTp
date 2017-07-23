"""Archivo principal de calculadora."""
from analizador import parse
import sys

exp_str = ""
if len(sys.argv) == 2:
    exp_str = sys.argv[1]

while True:
    if len(exp_str) == 0:
        exp_str = raw_input('calculoLambda> ')
    print(parse(exp_str))
    exp_str = ""
