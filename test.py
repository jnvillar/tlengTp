"""Archivo principal de calculadora."""
from analizador import parse

print "Test 1:"
exp_str1 = '(\\x:Nat.succ(succ(x))) 3'
res1 = parse(exp_str1)
expected1 = 'succ(succ(succ(succ(succ(0))))):Nat'

assert (str(expected1) == str(res1))


print "Test 3:"
exp_str3 = '\\x:Bool.if x then false else true'
res3 = parse(exp_str3)
expected3 = '\\x:Bool.if x then false else true:Bool->Bool'

assert (str(expected3) == str(res3))


print "Test 4:"
exp_str4 = '(\\x:Bool.if x then false else true)'
res4 = parse(exp_str4)
expected4 = '(\\x:Bool.if x then false else true):Bool->Bool'


assert (str(expected4) == str(res4))



print "Test 5:"
exp_str5 = '\\x:Nat.succ(0)'
res5 = parse(exp_str5)
expected5 = '\\x:Nat.succ(0):Nat->Nat'

assert (str(expected5) == str(res5))



print "Test 6:"
exp_str6 = '\\x:Nat.succ(x)'
res6 = parse(exp_str6)
expected6 = '\\x:Nat.succ(x):Nat->Nat'

assert (str(expected6) == str(res6))


print "Test 7:"
exp_str7 = 'if true then 1 else 0'
res7 = parse(exp_str7)
expected7 = 'succ(0):Nat'

assert (str(expected7) == str(res7))


print "Test 8:"
exp_str8 = '\\x:Nat->Nat.x'
res8 = parse(exp_str8)
expected8 = '\\x:Nat->Nat.x:(Nat->Nat)->(Nat->Nat)'

assert (str(expected8) == str(res8))



exp_str9 = '\\x:Nat.\\y:Nat.(\\z:Bool.if z then x else 0)'
res9 = parse(exp_str9)
expected9 = '\\x:Nat.\\y:Nat.(\\z:Bool.if z then x else 0):Nat->(Nat->(Bool->Nat))'

assert (str(expected9) == str(res9))




exp_str10 = '(\\x:Nat.\\y:Nat.y) 3'
res10 = parse(exp_str10)
expected10 = '\\y:Nat.y:Nat->Nat'
assert (str(expected10) == str(res10))



exp_str11 = '(\\x:Nat.\\y:Nat.succ(x)) 3'
res11 = parse(exp_str11)
expected11 = '\y:Nat.succ(succ(succ(succ(0)))):Nat->Nat'
assert (str(expected11) == str(res11))


exp_str12 = '\\x:Nat.if true then 1 else 0'
res12 = parse(exp_str12)
expected12 = '\\x:Nat.succ(0):Nat->Nat'
assert (str(expected12) == str(res12))



exp_str13 = '(\\y:Nat.(\\z:Bool.if z then (\\j:Nat.succ(j)) y else 0)) 8'
res13 = parse(exp_str13)
expected13 = '(\\z:Bool.if z then succ(succ(succ(succ(succ(succ(succ(succ(succ(0))))))))) else 0):Bool->Nat'
assert (str(expected13) == str(res13))


exp_str14 = '(\\x:Nat->Nat.\\y:Nat.(\\z:Bool.if z then x y else 0)) (\\j:Nat.succ(j))'
res14 = parse(exp_str14)
expected14 = '\\y:Nat.(\\z:Bool.if z then (\\j:Nat.succ(j)) y else 0):Nat->(Bool->Nat)'
assert (str(expected14) == str(res14))

exp_str15 = '(\\x:Nat->Nat.\\y:Nat.(\\z:Bool.if z then x y else 0)) (\\j:Nat.succ(j)) 8'
res15 = parse(exp_str15)
expected15 = '(\\z:Bool.if z then succ(succ(succ(succ(succ(succ(succ(succ(succ(0))))))))) else 0):Bool->Nat'
assert (str(expected15) == str(res15))


print "Test 16:"
exp_str16 = '(\\x:Nat->Nat.\\y:Nat.(\\z:Bool.if z then x y else 0)) (\\j:Nat.succ(j)) 8 true'
res16 = parse(exp_str16)
expected16 = 'succ(succ(succ(succ(succ(succ(succ(succ(succ(0))))))))):Nat'
assert (str(expected16) == str(res16))























