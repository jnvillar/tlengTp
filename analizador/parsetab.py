
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'TRUE FALSE IF THEN ELSE ZERO VARIABLE BACKSLASH NUMBER DOT 2DOTS OPENPARENTHESIS CLOSEPARENTHESIS SUCC PRED ISZERO TYPE ARROWexpression : ZEROexpression : TRUEexpression : FALSEexpression : IF expression THEN expression ELSE expressionexpression : NUMBERfuncionType : TYPE funcImgfuncImg : ARROW funcionTypefuncImg : expression : PRED OPENPARENTHESIS expression CLOSEPARENTHESISexpression : SUCC OPENPARENTHESIS expression CLOSEPARENTHESISexpression : ISZERO OPENPARENTHESIS expression CLOSEPARENTHESISexpression : VARIABLEexpression : BACKSLASH expression 2DOTS funcionType DOT expressionexpression :  OPENPARENTHESIS expression CLOSEPARENTHESIS expression_valuesexpression_values : expressionexpression_values : expression :  expression expression'
    
_lr_action_items = {'CLOSEPARENTHESIS':([1,5,6,7,11,15,18,21,22,23,24,28,29,30,31,32,38,40,],[-3,-5,-12,-1,-2,-17,24,28,29,30,-16,-10,-9,-11,-15,-14,-13,-4,]),'THEN':([1,5,6,7,11,15,19,24,28,29,30,31,32,38,40,],[-3,-5,-12,-1,-2,-17,25,-16,-10,-9,-11,-15,-14,-13,-4,]),'FALSE':([0,1,2,4,5,6,7,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,28,29,30,31,32,33,34,37,38,40,],[1,-3,1,1,-5,-12,-1,1,-2,1,1,1,1,1,1,1,1,1,1,1,1,1,-10,-9,-11,1,-14,1,1,1,1,1,]),'PRED':([0,1,2,4,5,6,7,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,28,29,30,31,32,33,34,37,38,40,],[8,-3,8,8,-5,-12,-1,8,-2,8,8,8,8,8,8,8,8,8,8,8,8,8,-10,-9,-11,8,-14,8,8,8,8,8,]),'2DOTS':([1,5,6,7,11,13,15,24,28,29,30,31,32,38,40,],[-3,-5,-12,-1,-2,20,-17,-16,-10,-9,-11,-15,-14,-13,-4,]),'ZERO':([0,1,2,4,5,6,7,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,28,29,30,31,32,33,34,37,38,40,],[7,-3,7,7,-5,-12,-1,7,-2,7,7,7,7,7,7,7,7,7,7,7,7,7,-10,-9,-11,7,-14,7,7,7,7,7,]),'NUMBER':([0,1,2,4,5,6,7,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,28,29,30,31,32,33,34,37,38,40,],[5,-3,5,5,-5,-12,-1,5,-2,5,5,5,5,5,5,5,5,5,5,5,5,5,-10,-9,-11,5,-14,5,5,5,5,5,]),'ELSE':([1,5,6,7,11,15,24,28,29,30,31,32,33,38,40,],[-3,-5,-12,-1,-2,-17,-16,-10,-9,-11,-15,-14,37,-13,-4,]),'BACKSLASH':([0,1,2,4,5,6,7,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,28,29,30,31,32,33,34,37,38,40,],[2,-3,2,2,-5,-12,-1,2,-2,2,2,2,2,2,2,2,2,2,2,2,2,2,-10,-9,-11,2,-14,2,2,2,2,2,]),'ISZERO':([0,1,2,4,5,6,7,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,28,29,30,31,32,33,34,37,38,40,],[9,-3,9,9,-5,-12,-1,9,-2,9,9,9,9,9,9,9,9,9,9,9,9,9,-10,-9,-11,9,-14,9,9,9,9,9,]),'SUCC':([0,1,2,4,5,6,7,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,28,29,30,31,32,33,34,37,38,40,],[3,-3,3,3,-5,-12,-1,3,-2,3,3,3,3,3,3,3,3,3,3,3,3,3,-10,-9,-11,3,-14,3,3,3,3,3,]),'ARROW':([27,],[36,]),'VARIABLE':([0,1,2,4,5,6,7,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,28,29,30,31,32,33,34,37,38,40,],[6,-3,6,6,-5,-12,-1,6,-2,6,6,6,6,6,6,6,6,6,6,6,6,6,-10,-9,-11,6,-14,6,6,6,6,6,]),'TYPE':([20,36,],[27,27,]),'OPENPARENTHESIS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,28,29,30,31,32,33,34,37,38,40,],[10,-3,10,14,10,-5,-12,-1,16,17,10,-2,10,10,10,10,10,10,10,10,10,10,10,10,10,-10,-9,-11,10,-14,10,10,10,10,10,]),'TRUE':([0,1,2,4,5,6,7,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,28,29,30,31,32,33,34,37,38,40,],[11,-3,11,11,-5,-12,-1,11,-2,11,11,11,11,11,11,11,11,11,11,11,11,11,-10,-9,-11,11,-14,11,11,11,11,11,]),'$end':([1,4,5,6,7,11,15,24,28,29,30,31,32,38,40,],[-3,0,-5,-12,-1,-2,-17,-16,-10,-9,-11,-15,-14,-13,-4,]),'DOT':([26,27,35,39,],[34,-8,-6,-7,]),'IF':([0,1,2,4,5,6,7,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,28,29,30,31,32,33,34,37,38,40,],[12,-3,12,12,-5,-12,-1,12,-2,12,12,12,12,12,12,12,12,12,12,12,12,12,-10,-9,-11,12,-14,12,12,12,12,12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'funcImg':([27,],[35,]),'funcionType':([20,36,],[26,39,]),'expression':([0,2,4,10,12,13,14,15,16,17,18,19,21,22,23,24,25,31,33,34,37,38,40,],[4,13,15,18,19,15,21,15,22,23,15,15,15,15,15,31,33,15,15,38,40,15,15,]),'expression_values':([24,],[32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> ZERO','expression',1,'p_expression_zero','parser.py',13),
  ('expression -> TRUE','expression',1,'p_expression_true','parser.py',18),
  ('expression -> FALSE','expression',1,'p_expression_false','parser.py',23),
  ('expression -> IF expression THEN expression ELSE expression','expression',6,'p_expression_if_then_else','parser.py',28),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',57),
  ('funcionType -> TYPE funcImg','funcionType',2,'p_expression_type','parser.py',62),
  ('funcImg -> ARROW funcionType','funcImg',2,'p_expression_type_img','parser.py',71),
  ('funcImg -> <empty>','funcImg',0,'p_expression_type_img_empty','parser.py',78),
  ('expression -> PRED OPENPARENTHESIS expression CLOSEPARENTHESIS','expression',4,'p_expression_pred','parser.py',83),
  ('expression -> SUCC OPENPARENTHESIS expression CLOSEPARENTHESIS','expression',4,'p_expression_succ','parser.py',102),
  ('expression -> ISZERO OPENPARENTHESIS expression CLOSEPARENTHESIS','expression',4,'p_expression_is_zero','parser.py',122),
  ('expression -> VARIABLE','expression',1,'p_expression_variable','parser.py',140),
  ('expression -> BACKSLASH expression 2DOTS funcionType DOT expression','expression',6,'p_expression_lambda','parser.py',150),
  ('expression -> OPENPARENTHESIS expression CLOSEPARENTHESIS expression_values','expression',4,'p_expression_application','parser.py',167),
  ('expression_values -> expression','expression_values',1,'p_expression_values','parser.py',195),
  ('expression_values -> <empty>','expression_values',0,'p_expression_values_empty','parser.py',200),
  ('expression -> expression expression','expression',2,'p_expression_application_function','parser.py',208),
]
