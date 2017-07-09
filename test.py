"""Archivo principal de calculadora."""
from analizador import parse

exp_str1 = '(\\x:Nat.succ(succ(x))) 3'
res1 = parse(exp_str1)
expected1 = 'succ(succ(succ(succ(succ(0)))))'

assert (str(expected1) == str(res1))



exp_str3 = '\\x:Bool.if x then false else true'
res3 = parse(exp_str3)
expected3 = '\\x:Bool.if x then false else true'

assert (str(expected3) == str(res3))



exp_str4 = '(\\x:Bool.if x then false else true)'
res4 = parse(exp_str4)
expected4 = '(\\x:Bool.if x then false else true) '

assert (str(expected4) == str(res4))




exp_str5 = '\\x:Nat.succ(0)'
res5 = parse(exp_str5)
expected5 = '\\x:Nat.succ(0)'

assert (str(expected5) == str(res5))




exp_str6 = '\\x:Nat.succ(x)'
res6 = parse(exp_str6)
expected6 = '\\x:Nat.succ(x)'

assert (str(expected6) == str(res6))


exp_str7 = 'if true then 1 else 0'
res7 = parse(exp_str7)
expected7 = 'succ(0)'

assert (str(expected7) == str(res7))



exp_str8 = '\\x:Nat->Nat.x'
res8 = parse(exp_str8)
expected8 = '\\x:Nat->Nat.x'

assert (str(expected8) == str(res8))



exp_str9 = '\\x:Nat->Nat.\\y:Nat.(\\z:Bool.if z then x else 0)'
res9 = parse(exp_str9)
expected9 = '\\x:Nat->Nat.\\y:Nat.(\\z:Bool.if z then x else 0) '

assert (str(expected9) == str(res9))




exp_str10 = '(\\x:Nat.\\y:Nat.y) 3'
res10 = parse(exp_str10)
expected10 = '\\y:Nat.y'

assert (str(expected10) == str(res10))




exp_str11 = '(\\x:Nat.\\y:Nat.succ(x)) 3'
res11 = parse(exp_str11)
expected11 = '\y:Nat.succ(succ(succ(succ(0))))'

assert (str(expected11) == str(res11))




















