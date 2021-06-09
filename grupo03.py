# ----------------------LEX----------------------------------------------------------------

import sys

import ply.lex as lex

# Definición de tokens y palabras reservadas.
reservadas = {
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

tokens = list(reservadas.values()) + [
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

# Ignorar un espacio en blanco.
t_ignore = ' \t'

# Definición de expresiones regulares para los tokens.
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

def t_NUMERO(t):
    r'\d+'
    t.type = reservadas.get(t.value, 'NUMERO')
    t.value = int(t.value)
    return t

def t_CADENA(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'CADENA')
    return t

# Función para informar de caracteres ilegales (no definidos previamente).
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Función para ignorar saltos de línea.
def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

# Inicialización diccionarios globales de tablas y columnas utilizadas.
diccionarioTablas = {}
diccionarioColumnas = {}

# Definición de la gramática.
def p_S_consulta_completa(p):
    '''S : SELECT_ FROM_ JOIN_ WHERE_ GROUP_BY ORDER_BY'''

def p_SELECT_(p):
    '''SELECT_ : SELECT CAMPOS
        | SELECT DISTINCT CAMPOS'''

def p_CAMPOS(p):
    '''CAMPOS : CAMPO COMA CAMPOS
        | CAMPO'''
    
def p_CAMPO(p):
    '''CAMPO : CADENA PUNTO CADENA AS COMILLA CADENA COMILLA
        | CADENA PUNTO CADENA
        | FUNC_RESUMEN AS COMILLA CADENA COMILLA'''
    llave = p[1]
    if llave in diccionarioColumnas:
        if len(p)!=6:
            campo = p[3] 
            if campo not in diccionarioColumnas[llave]:
                diccionarioColumnas[llave].append(campo)
    else:
        if len(p)!=6:
            diccionarioColumnas[llave]=[p[3]]
    # Guardado de campos en el diccionario de columnas, usando como llave el nombre de la tabla o el alias.

def p_FUNC_RESUMEN(p):
    '''FUNC_RESUMEN : MIN PAR_IZQ CADENA PUNTO CADENA PAR_DER
        | MAX PAR_IZQ CADENA PUNTO CADENA PAR_DER
        | COUNT PAR_IZQ CADENA PUNTO CADENA PAR_DER
        | COUNT PAR_IZQ DISTINCT CADENA PUNTO CADENA PAR_DER'''
    llave = ''
    if len(p)<8:
        llave = p[3]
    else:
        llave = p[4]
    if llave in diccionarioColumnas:
        if len(p)==7: 
            campo = p[5] 
            if campo not in diccionarioColumnas[llave]:
                diccionarioColumnas[llave].append(campo)
        elif len(p)==8:
            campo = p[6] 
            if campo not in diccionarioColumnas[llave]:
                diccionarioColumnas[llave].append(campo)
    else:
        if len(p)==7:
            diccionarioColumnas[llave]=[p[5]]
        elif len(p)==8:
            diccionarioColumnas[llave]=[p[6]]
    # Guardado de campos en el diccionario de columnas, usando como llave el nombre de la tabla o el alias.

def p_FROM_(p):
    '''FROM_ : FROM CADENA CADENA
        | FROM CADENA AS CADENA
        | FROM CADENA
    '''
    if len(p)==4:
        diccionarioTablas[p[2]]=p[3]
    elif len(p)==5:
        diccionarioTablas[p[2]]=p[4]
    elif len(p)==3: 
        diccionarioTablas.setdefault(p[2])
    # Guardado de nombres de tablas en el diccionario de tablas, junto con sus alias si tuvieran definido alguno.

def p_JOIN_(p):
    '''JOIN_ : JOIN_INNER_LEFT JOIN_ 
        | '''

def p_JOIN_INNER_LEFT(p):
    '''JOIN_INNER_LEFT : INNER JOIN CADENA CADENA ON COND_W
        | INNER JOIN CADENA AS CADENA ON COND_W
        | LEFT JOIN CADENA CADENA ON COND_W
        | LEFT JOIN CADENA AS CADENA ON COND_W
        | INNER JOIN CADENA ON COND_W
        | LEFT JOIN CADENA ON COND_W'''
    llave = p[3]
    if len(p)==7:
        diccionarioTablas[llave]=p[4]
    elif len(p)==8:
        diccionarioTablas[llave]=p[5]
    elif len(p)==6:
        diccionarioTablas.setdefault(llave)
    # Guardado de nombres de tablas en el diccionario de tablas, junto con sus alias si tuvieran definido alguno.

def p_WHERE_(p):
    '''WHERE_ : WHERE COND_W
        | '''

def p_COND_W(p):
    '''COND_W : CONDICION
        | CADENA PUNTO CADENA SUBCONSULTA
        | COND_W AND COND_W
        |  COND_W OR COND_W 
        | PAR_IZQ COND_W OR COND_W PAR_DER'''
    llave = ''
    if len(p)==5:
        llave = p[1]
    if llave in diccionarioColumnas:
        if len(p)==5: 
            campo = p[3] 
            if campo not in diccionarioColumnas[llave]:
                diccionarioColumnas[llave].append(campo)
    else:
        if len(p)==5:
            diccionarioColumnas[llave]=[p[3]]
    # Guardado de campos en el diccionario de columnas, usando como llave el nombre de la tabla o el alias.

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
    if len(p)<8:
        llave = p[1]
        if llave in diccionarioColumnas:
            campo = p[3] 
            if campo not in diccionarioColumnas[llave]:
                diccionarioColumnas[llave].append(campo)
        else:
            diccionarioColumnas[llave]=[p[3]]
    else:
        llave1 = p[1]
        llave2 = p[5] 
        if llave1 in diccionarioColumnas:
            campo = p[3] 
            if campo not in diccionarioColumnas[llave1]:
                diccionarioColumnas[llave1].append(campo)
        else:
            diccionarioColumnas[llave1]=[p[3]]
        if llave2 in diccionarioColumnas:
            campo = p[7] 
            if campo not in diccionarioColumnas[llave2]:
                diccionarioColumnas[llave2].append(campo)
        else:
            diccionarioColumnas[llave2]=[p[7]]
    # Guardado de campos en el diccionario de columnas, usando como llave el nombre de la tabla o el alias.

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
    if p[1] in diccionarioColumnas:
        if p[3] not in diccionarioColumnas[p[1]]:
            diccionarioColumnas[p[1]].append(p[3])
    else:
        diccionarioColumnas[p[1]]=[p[3]]
    # Guardado de campos en el diccionario de columnas, usando como llave el nombre de la tabla o el alias.

def p_HAVING_(p):
    '''HAVING_ : HAVING FUNC_RESUMEN SIGNO VALOR
        | '''

def p_ORDER_BY(p):
    '''ORDER_BY : ORDER BY CAMPOS_O
        | '''

def p_CAMPOS_O(p):
    '''CAMPOS_O : CADENA PUNTO CADENA ORDEN COMA CAMPOS_O
        | CADENA PUNTO CADENA ORDEN'''
    if p[1] in diccionarioColumnas:
        if p[3] not in diccionarioColumnas[p[1]]:
            diccionarioColumnas[p[1]].append(p[3])
    else:
        diccionarioColumnas[p[1]]=[p[3]]
    # Guardado de campos en el diccionario de columnas, usando como llave el nombre de la tabla o el alias.

def p_ORDEN(p):
    '''ORDEN : ASC
        | DESC
        | '''

# Función para informar de errores sintácticos.
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# ----------------------YACC---------------------------------------------------------------

import ply.yacc as yacc

# Definición de función principal (retorna un diccionario de tablas y campos utilizados en la consulta).
def parse_select_statement(s):
    # Vaciado de los diccionarios globales.
    diccionarioColumnas.clear()
    diccionarioTablas.clear()
    contador=0
    yacc.yacc()
    yacc.parse(s)
    # Inicialización de diccionario que se retorna como resultado (para las tablas y campos usados).
    diccionarioResultado = {}
    # Bucle para recorrer y guardar las tablas y sus campos.
    for llaveT in diccionarioTablas:
        control=''
        if diccionarioTablas.get(llaveT)!=None:
            control=diccionarioTablas.get(llaveT)
        else:
            control=llaveT
            # Si la tabla tiene definido un alias, se usa ese alias para matchear; sino se usa el nombre de la tabla.
        for llaveC in diccionarioColumnas:
            if control==llaveC:
                diccionarioResultado[llaveT]=sorted(diccionarioColumnas.get(llaveC))
                contador+=1
    if len(diccionarioColumnas.keys())>contador:
        raise Exception('Error de cadena inválida: mal uso del alias para una tabla.')
        # Control para que no se permitan consultas en las que se define un alias que no se use, o que se use un alias no definido.
    return diccionarioResultado
