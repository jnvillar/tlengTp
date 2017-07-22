"""Archivo principal de calculadora."""
from analizador import parse



exp_str1 = '(\\x:Nat->Nat.\\y:Nat.(\\z:Bool.if z then x y else 0)) (\\j:Nat.succ(j)) 8 true'
res1 = parse(exp_str1)
expected1 = 'nada'

assert (str(expected1) == str(res1))