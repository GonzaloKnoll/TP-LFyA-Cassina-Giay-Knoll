# ----------------------LEX----------------------------------------------------------------

import sys

import ply.lex as lex

keywords = {
    'SELECT':'SELECT', 'AS':'AS', 'MIN':'MIN', 'MAX':'MAX', 'COUNT':'COUNT', 'DISTINCT':'DISTINCT',
    'FROM':'FROM', 'INNER':'INNER', 'JOIN':'JOIN', 'ON':'ON', 'LEFT':'LEFT', 'WHERE':'WHERE',
    'AND':'AND', 'OR':'OR', 'IN':'IN', 'NOT':'NOT', 'IS':'IS', 'NULL':'NULL',
    'GROUP':'GROUP', 'BY':'BY', 'HAVING':'HAVING', 'ORDER':'ORDER', 'ASC':'ASC', 'DESC':'DESC',
}

tokens = list(keywords.values()) + [
    'numero', 'cadena',
]

literals = ['.', "'", '(', ')', '=', '>', '<', ',']

#t_cadena = r'[a-zA-Z_][a-zA-Z0-9_]*'

t_ignore = ' \t'

def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)

def t_numero(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_cadena(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'cadena')
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

diccionario = {}



# ----------------------YACC---------------------------------------------------------------

import ply.yacc as yacc



# ----------------------PRUEBA---------------------------------------------------------------

lexer = lex.lex()

data = '''
SELECT M.cod_multa FROM Multa M WHERE M.monto<>1000 GROUP BY M.cod_multa ORDER BY M.cod_multa ASC
'''
lexer.input(data)
 
while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)