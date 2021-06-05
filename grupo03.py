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
    'NUMERO', 
    'CADENA',
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
t_COMILLA = r"'"
t_COMA = r','
t_PAR_IZQ = r'\('
t_PAR_DER = r'\)'
t_IGUAL = r'='
t_DESIGUAL = r'<>'
t_MAYOR= r'>'
t_MENOR = r'<'
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)

def t_numero(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_cadena(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'CADENA')
    return t

lexer = lex.lex()

diccionarioTablas = {}
diccionarioColumnas = {}

def p_S_consulta_completa(p):
    '''S : SELECT_ FROM_ JOIN_ WHERE_ GROUP_BY ORDER_BY''' # DISTINCT???
    

def p_SELECT_(p):
    '''SELECT_ : SELECT CAMPOS'''


def p_CAMPOS(p):
    '''CAMPOS : CAMPO COMA CAMPOS
        | CAMPO'''
    

def p_CAMPO(p):
    '''CAMPO : CADENA PUNTO CADENA AS COMILLA CADENA COMILLA
        | CADENA PUNTO CADENA
        | FUNC_RESUMEN AS COMILLA CADENA COMILLA'''
    llave = p[1]
    if llave in diccionarioColumnas:
        if len(p)==8: 
            campo = p[6] 
            if campo not in diccionarioColumnas[llave]:
                diccionarioColumnas[llave].append(campo)
        elif len(p)==4:
            campo = p[3] 
            if campo not in diccionarioColumnas[llave]:
                diccionarioColumnas[llave].append(campo)
        elif len(p)==6: # funcion de resumen REVISAR!!!!!!
            campo = p[4] 
            if campo not in diccionarioColumnas[llave]:
                diccionarioColumnas[llave].append(campo)
    else:
        if len(p)==8:
            diccionarioColumnas.setdefault(p[1], [p[6]])
        elif len(p)==4:
            diccionarioColumnas.setdefault(p[1], [p[3]])
        elif len(p)==6:
            diccionarioColumnas.setdefault('nombre tabla', [p[4]])
    print('p_CAMPO', diccionarioColumnas)
    
def p_FUNC_RESUMEN(p):
    '''FUNC_RESUMEN : MIN PAR_IZQ CADENA PUNTO CADENA PAR_DER
        | MAX PAR_IZQ CADENA PUNTO CADENA PAR_DER
        | COUNT PAR_IZQ CADENA PUNTO CADENA PAR_DER
        | COUNT PAR_IZQ DISTINCT CADENA PUNTO CADENA PAR_DER'''

def p_FROM_(p):
    '''FROM_ : FROM CADENA CADENA
        | FROM CADENA AS CADENA
        | FROM CADENA
    '''
    if len(p)==4:
        diccionarioTablas.setdefault(p[2],p[3])
    elif len(p)==5:
        diccionarioTablas.setdefault(p[2],p[4])
    elif len(p)==3: 
        diccionarioTablas.setdefault(p[2])
    print('p_FROM_', diccionarioTablas)

def p_ALIAS_T(p):
    '''ALIAS_T : AS CADENA
        | CADENA'''

def p_JOIN_(p):
    '''JOIN_ : JOIN_INNER_LEFT JOIN_ 
        | '''

def p_JOIN_INNER_LEFT(p):
    '''JOIN_INNER_LEFT : INNER JOIN CADENA ALIAS_T ON COND_W
        | LEFT JOIN CADENA ALIAS_T ON COND_W'''

def p_WHERE_(p):
    '''WHERE_ : WHERE COND_W
        | '''

def p_COND_W(p):
    '''COND_W : CONDICION
        | CADENA PUNTO CADENA SUBCONSULTA
        | COND_W AND COND_W
        |  COND_W OR COND_W 
        | PAR_IZQ COND_W OR COND_W PAR_DER'''

def p_SUBCONSULTA(p):
    '''SUBCONSULTA : IN PAR_IZQ S PAR_DER
        | NOT IN PAR_IZQ S PAR_DER'''

def p_VALOR(p):
    '''VALOR : NUMERO
        | COMILLA CADENA COMILLA'''

def p_CONDICION(p):
    '''CONDICION : CADENA PUNTO CADENA SIGNO VALOR 
        | CADENA PUNTO CADENA SIGNO CADENA PUNTO CADENA
        |  CADENA PUNTO CADENA NULLEABLE'''

def p_NULLEABLE(p):
    '''NULLEABLE :  IS NOT NULL
        |  IS NULL'''

def p_SIGNO(p):
    '''SIGNO : IGUAL 
        | MAYOR 
        | MENOR 
        | MAYOR_IGUAL 
        | MENOR_IGUAL
        | DESIGUAL'''

def p_GROUP_BY(p):
    '''GROUP_BY : GROUP BY CAMPOS_G HAVING_
        | '''

def p_CAMPOS_G(p):
    '''CAMPOS_G :  CADENA PUNTO CADENA COMA CAMPOS_G
        | CADENA PUNTO CADENA'''

def p_HAVING_(p):
    '''HAVING_ : HAVING FUNC_RESUMEN SIGNO VALOR
        | '''

def p_ORDER_BY(p):
    '''ORDER_BY : ORDER BY CAMPOS_O
        | '''

def p_CAMPOS_O(p):
    '''CAMPOS_O : CADENA PUNTO CADENA ORDEN COMA CAMPOS_O
        | CADENA PUNTO CADENA ORDEN'''

def p_ORDEN(p):
    '''ORDEN : ASC
        | DESC
        | '''

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# ----------------------YACC---------------------------------------------------------------

import ply.yacc as yacc

def parse_select_statement(s):
    
    yacc.yacc()
    yacc.parse(s)

    return diccionarioTablas

if __name__ == '__main__':
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


data = '''
SELECT M.cod_multa, M.nombre FROM Multa M WHERE M.monto<>1000 AND M.nombre='Juan'
GROUP BY M.cod_multa ORDER BY M.cod_multa ASC
'''
lexer.input(data)
 
while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)
