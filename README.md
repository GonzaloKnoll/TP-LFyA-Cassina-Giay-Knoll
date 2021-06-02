# TP-LFyA-Cassina-Giay-Knoll
Trabajo Práctico Lenguajes Formales y Autómatas, Cassina-Giay-Knoll

Grámatica:

S : SELECT_ FROM_ JOIN_ WHERE_ GROUP_BY ORDER_BY

SELECT_ : SELECT CAMPOS

CAMPOS : CAMPO CAMPOS
| : CAMPO

CAMPO : cadena . cadena AS ' cadena '
| : cadena . cadena
| : FUNC_RESUMEN AS ' cadena '

FUNC_RESUMEN : MIN ( cadena . cadena )
| : MAX ( cadena . cadena )
| : COUNT ( cadena . cadena )
| : COUNT ( DISTINCT cadena . cadena )

FROM_ : FROM cadena ALIAS_T

ALIAS_T : AS cadena
| : cadena

JOIN_ : JOIN JOIN_ 
| : 𝛌

JOIN : INNER JOIN cadena ALIAS_T ON COND_W
| : LEFT JOIN cadena ALIAS_T ON COND_W

WHERE_ : WHERE COND_W
| : 𝛌

COND_W : CONDICION
| : cadena . cadena SUBCONSULTA
| : COND_W AND COND_W
| :  COND_W OR COND_W 
| : ( COND_W OR COND_W )

SUBCONSULTA : IN ( S )
| : NOT IN ( S )

VALOR : numero
| : ' cadena '

CONDICION : cadena . cadena SIGNO VALOR 
| : cadena . cadena SIGNO cadena . cadena
| :  cadena . cadena NULLEABLE

NULLEABLE :  IS NOT NULL
| :  IS NULL

SIGNO : = 
| : > 
| : < 
| : >= 
| : <= 
| : <>

GROUP_BY : GROUP BY CAMPOS_G HAVING_
| : 𝛌

CAMPOS_G :  cadena . cadena , CAMPOS_G
| : cadena . cadena

HAVING_ : HAVING FUNC_RESUMEN SIGNO VALOR
| : 𝛌

ORDER_BY : ORDER BY CAMPOS_O
| : 𝛌

CAMPOS_O : cadena . cadena ORDEN , CAMPOS_O
| : cadena . cadena ORDEN

ORDEN : ASC
| : DESC
| : 𝛌
