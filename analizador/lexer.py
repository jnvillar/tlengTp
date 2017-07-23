#! coding: utf-8
"""Calculator lexer example."""
import ply.lex as lex

"""
Lista de tokens

El analizador léxico de PLY (al llamar al método lex.lex()) va a buscar
para cada uno de estos tokens una variable "t_TOKEN" en el módulo actual.

Sí, es súper nigromántico pero es lo que hay.

t_TOKEN puede ser:

- Una expresión regular
- Una función cuyo docstring sea una expresión regular (bizarro).

En el segundo caso, podemos hacer algunas cosas "extras", como se
muestra aquí abajo.

"""

tokens = (
    'TRUE',
    'FALSE',
    'IF',
    'THEN',
    'ELSE',
    'ZERO',
    'VARIABLE',
    'BACKSLASH',
    'NUMBER',
    'DOT',
    '2DOTS',
    'OPENPARENTHESIS',
    'CLOSEPARENTHESIS',
    'SUCC',
    'PRED',
    'ISZERO',
    'TYPE',
    'ARROW',
)

t_TRUE = r'true'
t_FALSE = r'false'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_ZERO = r'0'
t_DOT = r'\.'
t_BACKSLASH = r'\\'
t_2DOTS = r':'
t_OPENPARENTHESIS = r'\('
t_CLOSEPARENTHESIS = r'\)'
t_SUCC = r'succ'
t_PRED = r'pred'
t_ISZERO = r'iszero'
t_ARROW = r'->'


t_ignore = ' \t'

def t_VARIABLE(t):
    r'[a-z]\b'
    return t

def t_NUMBER(t):
	r'[1-9]([0-9]*)'
	t.value = int(t.value)
	return t

def t_TYPE(t):
	r'Nat|Bool'
	t.value = t.value
	return t

# Build the lexer
lexer = lex.lex()

def apply_lexer(string):
    """Aplica el lexer al string dado."""
    lexer.input(string)

    return list(lexer)
