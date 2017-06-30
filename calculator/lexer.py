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
    'NUMBER',
    'PLUS',
    'TIMES',
    'MINUS',
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_ignore = ' \t'
#t_NUMBER = r'\d+'


def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

# Build the lexer
lexer = lex.lex()

def apply_lexer(string):
    """Aplica el lexer al string dado."""
    lexer.input(string)

    return list(lexer)
