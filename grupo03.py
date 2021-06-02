# ----------------------LEX----------------------------------------------------------------

import sys

import ply.lex as lex

keywords = {
    'SELECT':'SELECT',
    'AS':'AS',
    'MIN':'MIN',
    'MAX':'MAX',
    'COUNT':'COUNT',
    'DISTINCT':'DISTINCT',
    'FROM':'FROM',
    'INNER':'INNER',
    'JOIN':'JOIN',
    'ON':'ON',
    'LEFT':'LEFT',
    'WHERE':'WHERE',
    'AND':'AND',
    'OR':'OR',
    'IN':'IN',
    'NOT':'NOT',
    'IS':'IS',
    'NULL':'NULL',
    'GROUP':'GROUP',
    'BY':'BY',
    'HAVING':'HAVING',
    'ORDER':'ORDER',
    'ASC':'ASC',
    'DESC':'DESC',
}

tokens = list(keywords.values()) + [
    'numero', 
    'cadena',
    'PUNTO',
    'COMILLA',
    'COMA',
    'PAR_IZQ',
    'PAR_DER',
    'IGUAL',
    'DESIGUAL',
    'MAYOR',
    'MENOR',
    'MAYOR_IGUAL',
    'MENOR_IGUAL',
]

t_ignore = ' \t'

t_PUNTO = r'\.'
t_COMILLA = r"'" # si da error probar a escapar
t_COMA = r','
t_PAR_IZQ = r'\('
t_PAR_DER = r'\)'
t_IGUAL = r'='
t_DESIGUAL = r'<>'
t_MAYOR= r'>'
t_MENOR = r'<'
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='

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

def p_S_consulta_completa(p):
    '''S : SELECT_ FROM_ JOIN_ WHERE_ GROUP_BY ORDER_BY'''

def p_SELECT_(p):
    '''SELECT_ : SELECT CAMPOS'''

def p_CAMPOS(p):
    '''CAMPO CAMPOS
        | : CAMPO'''

def p_CAMPO(p):
    '''CAMPO : cadena . cadena AS ' cadena '
        | : cadena . cadena
        | : FUNC_RESUMEN AS ' cadena ' ''' # si da error sacar comilla

def p_FUNC_RESUMEN(p):
    '''FUNC_RESUMEN : MIN ( cadena . cadena )
        | : MAX ( cadena . cadena )
        | : COUNT ( cadena . cadena )
        | : COUNT ( DISTINCT cadena . cadena )'''

def p_FROM_(p):
    '''FROM_ : FROM cadena ALIAS_T'''

def p_ALIAS_T(p):
    '''ALIAS_T : AS cadena
        | : cadena'''

def p_JOIN_(p):
    '''JOIN_ : JOIN JOIN_ 
        | '''

def p_JOIN(p):
    '''JOIN : INNER JOIN cadena ALIAS_T ON COND_W
        | : LEFT JOIN cadena ALIAS_T ON COND_W'''

def p_WHERE_(p):
    '''WHERE_ : WHERE COND_W
        | '''

def p_COND_W(p):
    '''COND_W : CONDICION
        | : cadena . cadena SUBCONSULTA
        | : COND_W AND COND_W
        | :  COND_W OR COND_W 
        | : ( COND_W OR COND_W )'''

def p_SUBCONSULTA(p):
    '''SUBCONSULTA : IN ( S )
        | : NOT IN ( S )'''

def p_VALOR(p):
    '''VALOR : numero
        | : ' cadena ' '''

def p_CONDICION(p):
    '''CONDICION : cadena . cadena SIGNO VALOR 
        | : cadena . cadena SIGNO cadena . cadena
        | :  cadena . cadena NULLEABLE'''

def p_NULLEABLE(p):
    '''NULLEABLE :  IS NOT NULL
        | :  IS NULL'''

def p_SIGNO(p):
    '''SIGNO : = 
        | : > 
        | : < 
        | : >= 
        | : <= 
        | : <>'''

def p_GROUP_BY(p):
    '''GROUP_BY : GROUP BY CAMPOS_G HAVING_
        | : '''

def p_CAMPOS_G(p):
    '''CAMPOS_G :  cadena . cadena , CAMPOS_G
        | : cadena . cadena'''

def p_HAVING_(p):
    '''HAVING_ : HAVING FUNC_RESUMEN SIGNO VALOR
        | '''

def p_ORDER_BY(p):
    '''ORDER_BY : ORDER BY CAMPOS_O
        | '''

def p_CAMPOS_O(p):
    '''CAMPOS_O : cadena . cadena ORDEN , CAMPOS_O
        | : cadena . cadena ORDEN'''

def p_ORDEN(p):
    '''ORDEN : ASC
        | : DESC
        | '''


# ----------------------YACC---------------------------------------------------------------

import ply.yacc as yacc

parser = yacc.yacc()

while True:
    try:
        s = input('consulta > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)


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
