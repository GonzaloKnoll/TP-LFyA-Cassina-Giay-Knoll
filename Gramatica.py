# ----------------------LEX----------------------------------------------------------------

import sys
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input

keywords = (
    'SELECT', 'AS', 'MIN', 'MAX', 'COUNT', 'DISTINCT',
    'FROM', 'INNER JOIN', 'ON', 'LEFT JOIN', 'WHERE', 'AND', 'OR', 'IN', 'NOT IN',
    'IS NOT NULL', 'IS NULL', 'GROUP BY', 'HAVING', 'ORDER BY', 'ASC', 'DESC',
)

tokens = keywords + (
    'alias_tabla', 'nombre_campo', 'alias_columna', 'nombre_tabla', 'numero', 'cadena',
)

literals = ['.', "'", '(', ')', '=', '>', '<', ',']

t_alias_tabla = r'[a-zA-Z_][a-zA-Z0-9_]*'

t_alias_columna = r'[a-zA-Z_][a-zA-Z0-9_]*'

t_nombre_tabla = r'[a-zA-Z_][a-zA-Z0-9_]*'

t_nombre_campo = r'[a-zA-Z_][a-zA-Z0-9_]*'

t_cadena = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_numero(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# ----------------------YACC---------------------------------------------------------------




# ----------------------PRUEBA---------------------------------------------------------------

import ply.lex as lex

data = '''
SELECT M.cod_multa FROM Multa M WHERE M.monto>1000
'''
lex.lexer.input(data)
 
while True:
    tok = lex.lexer.token()
    if not tok: 
        break
    print(tok)