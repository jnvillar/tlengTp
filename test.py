"""Archivo principal de calculadora."""
from analizador import parse


exp_str1 = '(\\x:Nat.succ(succ(x))) 3'
print ("Test 1: " + exp_str1)
res1 = parse(exp_str1)
print ("Res: " + str(res1))
expected1 = 'succ(succ(succ(succ(succ(0))))):Nat'

assert (str(expected1) == str(res1))


exp_str3 = '\\x:Bool.if x then false else true'
print ("Test 2: " + exp_str3)
res3 = parse(exp_str3)
print ("Res: " + str(res3))
expected3 = '\\x:Bool.if x then false else true:Bool->Bool'

assert (str(expected3) == str(res3))


exp_str4 = '(\\x:Bool.if x then false else true)'
print ("Test 1: " + exp_str4)
res4 = parse(exp_str4)
print ("Res: " + str(res4))
expected4 = '(\\x:Bool.if x then false else true):Bool->Bool'

assert (str(expected4) == str(res4))


exp_str5 = '\\x:Nat.succ(0)'
print ("Test 5: " + exp_str5)
res5 = parse(exp_str5)
print ("Res: " + str(res5))
expected5 = '\\x:Nat.succ(0):Nat->Nat'

assert (str(expected5) == str(res5))

exp_str6 = '\\x:Nat.succ(x)'
print ("Test 6: " + exp_str6)
res6 = parse(exp_str6)
print ("Res: " + str(res6))
expected6 = '\\x:Nat.succ(x):Nat->Nat'

assert (str(expected6) == str(res6))

exp_str7 = 'if true then 1 else 0'
print ("Test 7: " + exp_str7)
res7 = parse(exp_str7)
print ("Res: " + str(res7))
expected7 = 'succ(0):Nat'

assert (str(expected7) == str(res7))

exp_str8 = '\\x:Nat->Nat.x'
print ("Test 8: " + exp_str8)
res8 = parse(exp_str8)
print ("Res: " + str(res8))
expected8 = '\\x:Nat->Nat.x:(Nat->Nat)->(Nat->Nat)'

assert (str(expected8) == str(res8))


exp_str9 = '\\x:Nat.\\y:Nat.(\\z:Bool.if z then x else 0)'
print ("Test 9: " + exp_str9)
res9 = parse(exp_str9)
print ("Res: " + str(res9))
expected9 = '\\x:Nat.\\y:Nat.(\\z:Bool.if z then x else 0):Nat->(Nat->(Bool->Nat))'

assert (str(expected9) == str(res9))


exp_str10 = '(\\x:Nat.\\y:Nat.y) 3'
print ("Test 10: " + exp_str10)
res10 = parse(exp_str10)
print ("Res: " + str(res10))
expected10 = '\\y:Nat.y:Nat->Nat'
assert (str(expected10) == str(res10))

exp_str11 = '(\\x:Nat.\\y:Nat.succ(x)) 3'
print ("Test 11: " + exp_str11)
res11 = parse(exp_str11)
print ("Res: " + str(res11))
expected11 = '\y:Nat.succ(succ(succ(succ(0)))):Nat->Nat'
assert (str(expected11) == str(res11))

exp_str12 = '\\x:Nat.if true then 1 else 0'
print ("Test 12: " + exp_str12)
res12 = parse(exp_str12)
print ("Res: " + str(res12))
expected12 = '\\x:Nat.succ(0):Nat->Nat'
assert (str(expected12) == str(res12))

exp_str13 = '(\\y:Nat.(\\z:Bool.if z then (\\j:Nat.succ(j)) y else 0)) 8'
print ("Test 13: " + exp_str13)
res13 = parse(exp_str13)
print ("Res: " + str(res13))
expected13 = '(\\z:Bool.if z then succ(succ(succ(succ(succ(succ(succ(succ(succ(0))))))))) else 0):Bool->Nat'
assert (str(expected13) == str(res13))


exp_str14 = '(\\x:Nat->Nat.\\y:Nat.(\\z:Bool.if z then x y else 0)) (\\j:Nat.succ(j))'
print ("Test 14: " + exp_str14)
res14 = parse(exp_str14)
print ("Res: " + str(res14))
expected14 = '\\y:Nat.(\\z:Bool.if z then (\\j:Nat.succ(j)) y else 0):Nat->(Bool->Nat)'
assert (str(expected14) == str(res14))

exp_str15 = '(\\x:Nat->Nat.\\y:Nat.(\\z:Bool.if z then x y else 0)) (\\j:Nat.succ(j)) 8'
print ("Test 15: " + exp_str15)
res15 = parse(exp_str15)
print ("Res: " + str(res15))
expected15 = '(\\z:Bool.if z then succ(succ(succ(succ(succ(succ(succ(succ(succ(0))))))))) else 0):Bool->Nat'
assert (str(expected15) == str(res15))


exp_str16 = '(\\x:Nat->Nat.\\y:Nat.(\\z:Bool.if z then x y else 0)) (\\j:Nat.succ(j)) 8 true'
print ("Test 16: " + exp_str16)
res16 = parse(exp_str16)
print ("Res: " + str(res16))
expected16 = 'succ(succ(succ(succ(succ(succ(succ(succ(succ(0))))))))):Nat'
assert (str(expected16) == str(res16))


exp_str17 = '(\\x:Nat->Bool.\\y:Nat.x y)'
print ("Test 17: " + exp_str17)
res17 = parse(exp_str17)
print ("Res: " + str(res17))
expected17 = '(\\x:Nat->Bool.\\y:Nat.x y):(Nat->Bool)->(Nat->Bool)'
assert (str(expected17) == str(res17))


exp_str18 = '(\\x:Nat.true) (if true then (\\y:Nat.succ(0)) 0 else (\\z:Nat.succ(0)) 0)'
print ("Test 18: " + exp_str18)
res18 = parse(exp_str18)
print ("Res: " + str(res18))
expected18 = 'true:Bool'
assert (str(expected18) == str(res18))



