
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS ASC BY CADENA COMA COMILLA COUNT DESC DESIGUAL DISTINCT FROM GROUP HAVING IGUAL IN INNER IS JOIN LEFT MAX MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MIN NOT NULL NUMERO ON OR ORDER PAR_DER PAR_IZQ PUNTO SELECT WHERES : SELECT_ FROM_ JOIN_ WHERE_ GROUP_BY ORDER_BYSELECT_ : SELECT CAMPOS\n        | SELECT DISTINCT CAMPOSCAMPOS : CAMPO COMA CAMPOS\n        | CAMPOCAMPO : CADENA PUNTO CADENA AS COMILLA CADENA COMILLA\n        | CADENA PUNTO CADENA\n        | FUNC_RESUMEN AS COMILLA CADENA COMILLAFUNC_RESUMEN : MIN PAR_IZQ CADENA PUNTO CADENA PAR_DER\n        | MAX PAR_IZQ CADENA PUNTO CADENA PAR_DER\n        | COUNT PAR_IZQ CADENA PUNTO CADENA PAR_DER\n        | COUNT PAR_IZQ DISTINCT CADENA PUNTO CADENA PAR_DERFROM_ : FROM CADENA CADENA\n        | FROM CADENA AS CADENA\n        | FROM CADENA\n    JOIN_ : JOIN_INNER_LEFT JOIN_ \n        | JOIN_INNER_LEFT : INNER JOIN CADENA CADENA ON COND_W\n        | INNER JOIN CADENA AS CADENA ON COND_W\n        | LEFT JOIN CADENA CADENA ON COND_W\n        | LEFT JOIN CADENA AS CADENA ON COND_WWHERE_ : WHERE COND_W\n        | COND_W : CONDICION\n        | CADENA PUNTO CADENA SUBCONSULTA\n        | COND_W AND COND_W\n        |  COND_W OR COND_W \n        | PAR_IZQ COND_W OR COND_W PAR_DERSUBCONSULTA : IN PAR_IZQ S PAR_DER\n        | NOT IN PAR_IZQ S PAR_DERVALOR : NUMERO\n        | COMILLA CADENA COMILLACONDICION : CADENA PUNTO CADENA SIGNO VALOR \n        | CADENA PUNTO CADENA SIGNO CADENA PUNTO CADENA\n        |  CADENA PUNTO CADENA NULLEABLENULLEABLE :  IS NOT NULL\n        |  IS NULLSIGNO : IGUAL \n        | MAYOR \n        | MENOR \n        | MAYOR_IGUAL \n        | MENOR_IGUAL\n        | DESIGUALGROUP_BY : GROUP BY CAMPOS_G HAVING_\n        | CAMPOS_G :  CADENA PUNTO CADENA COMA CAMPOS_G\n        | CADENA PUNTO CADENAHAVING_ : HAVING FUNC_RESUMEN SIGNO VALOR\n        | ORDER_BY : ORDER BY CAMPOS_O\n        | CAMPOS_O : CADENA PUNTO CADENA ORDEN COMA CAMPOS_O\n        | CADENA PUNTO CADENA ORDENORDEN : ASC\n        | DESC\n        | '
    
_lr_action_items = {'SELECT':([0,119,132,],[3,3,3,]),'$end':([1,4,14,15,18,26,28,31,40,42,43,48,55,73,75,76,88,90,93,95,106,108,114,116,117,122,123,124,125,126,133,134,135,136,137,138,139,140,141,144,145,],[0,-17,-23,-17,-15,-45,-16,-13,-51,-22,-24,-14,-1,-49,-26,-27,-50,-44,-25,-35,-18,-20,-47,-33,-31,-37,-28,-19,-21,-56,-36,-53,-54,-55,-48,-46,-34,-32,-29,-30,-52,]),'FROM':([2,6,8,19,33,34,67,110,],[5,-2,-5,-3,-4,-7,-8,-6,]),'DISTINCT':([3,25,],[7,39,]),'CADENA':([3,5,7,18,20,21,23,24,25,27,29,30,32,35,39,45,46,47,51,52,53,57,58,59,60,63,65,66,71,72,78,79,81,92,94,98,99,100,101,102,103,107,109,112,118,128,129,143,],[9,18,9,31,9,34,36,37,38,44,46,47,48,50,54,44,62,64,68,69,70,74,44,44,77,80,82,83,87,89,44,44,44,114,115,-38,-39,-40,-41,-42,-43,44,44,126,130,74,139,89,]),'MIN':([3,7,20,91,],[11,11,11,11,]),'MAX':([3,7,20,91,],[12,12,12,12,]),'COUNT':([3,7,20,91,],[13,13,13,13,]),'WHERE':([4,14,15,18,28,31,43,48,75,76,93,95,106,108,116,117,122,123,124,125,133,139,140,141,144,],[-17,27,-17,-15,-16,-13,-24,-14,-26,-27,-25,-35,-18,-20,-33,-31,-37,-28,-19,-21,-36,-34,-32,-29,-30,]),'GROUP':([4,14,15,18,26,28,31,42,43,48,75,76,93,95,106,108,116,117,122,123,124,125,133,139,140,141,144,],[-17,-23,-17,-15,41,-16,-13,-22,-24,-14,-26,-27,-25,-35,-18,-20,-33,-31,-37,-28,-19,-21,-36,-34,-32,-29,-30,]),'ORDER':([4,14,15,18,26,28,31,40,42,43,48,73,75,76,90,93,95,106,108,114,116,117,122,123,124,125,133,137,138,139,140,141,144,],[-17,-23,-17,-15,-45,-16,-13,56,-22,-24,-14,-49,-26,-27,-44,-25,-35,-18,-20,-47,-33,-31,-37,-28,-19,-21,-36,-48,-46,-34,-32,-29,-30,]),'PAR_DER':([4,14,15,18,26,28,31,40,42,43,48,55,68,69,70,73,75,76,87,88,90,93,95,105,106,108,114,116,117,122,123,124,125,126,131,133,134,135,136,137,138,139,140,141,142,144,145,],[-17,-23,-17,-15,-45,-16,-13,-51,-22,-24,-14,-1,84,85,86,-49,-26,-27,111,-50,-44,-25,-35,123,-18,-20,-47,-33,-31,-37,-28,-19,-21,-56,141,-36,-53,-54,-55,-48,-46,-34,-32,-29,144,-30,-52,]),'INNER':([4,15,18,31,43,48,75,76,93,95,106,108,116,117,122,123,124,125,133,139,140,141,144,],[16,16,-15,-13,-24,-14,-26,-27,-25,-35,-18,-20,-33,-31,-37,-28,-19,-21,-36,-34,-32,-29,-30,]),'LEFT':([4,15,18,31,43,48,75,76,93,95,106,108,116,117,122,123,124,125,133,139,140,141,144,],[17,17,-15,-13,-24,-14,-26,-27,-25,-35,-18,-20,-33,-31,-37,-28,-19,-21,-36,-34,-32,-29,-30,]),'COMA':([8,34,67,110,114,126,134,135,136,],[20,-7,-8,-6,128,-56,143,-54,-55,]),'PUNTO':([9,36,37,38,44,54,74,89,115,],[21,51,52,53,60,71,92,112,129,]),'AS':([10,18,34,46,47,84,85,86,111,],[22,32,49,63,65,-9,-10,-11,-12,]),'PAR_IZQ':([11,12,13,27,45,58,59,78,79,81,96,107,109,120,],[23,24,25,45,45,45,45,45,45,45,119,45,45,132,]),'JOIN':([16,17,],[29,30,]),'COMILLA':([22,49,50,83,94,98,99,100,101,102,103,127,130,],[35,66,67,110,118,-38,-39,-40,-41,-42,-43,118,140,]),'BY':([41,56,],[57,72,]),'AND':([42,43,61,75,76,93,95,105,106,108,116,117,122,123,124,125,133,139,140,141,144,],[58,-24,58,58,58,-25,-35,58,58,58,-33,-31,-37,-28,58,58,-36,-34,-32,-29,-30,]),'OR':([42,43,61,75,76,93,95,105,106,108,116,117,122,123,124,125,133,139,140,141,144,],[59,-24,78,59,59,-25,-35,59,59,59,-33,-31,-37,-28,59,59,-36,-34,-32,-29,-30,]),'ON':([62,64,80,82,],[79,81,107,109,]),'HAVING':([73,114,138,],[91,-47,-46,]),'IN':([77,97,],[96,120,]),'NOT':([77,104,],[97,121,]),'IGUAL':([77,84,85,86,111,113,],[98,-9,-10,-11,-12,98,]),'MAYOR':([77,84,85,86,111,113,],[99,-9,-10,-11,-12,99,]),'MENOR':([77,84,85,86,111,113,],[100,-9,-10,-11,-12,100,]),'MAYOR_IGUAL':([77,84,85,86,111,113,],[101,-9,-10,-11,-12,101,]),'MENOR_IGUAL':([77,84,85,86,111,113,],[102,-9,-10,-11,-12,102,]),'DESIGUAL':([77,84,85,86,111,113,],[103,-9,-10,-11,-12,103,]),'IS':([77,],[104,]),'NUMERO':([94,98,99,100,101,102,103,127,],[117,-38,-39,-40,-41,-42,-43,117,]),'NULL':([104,121,],[122,133,]),'ASC':([126,],[135,]),'DESC':([126,],[136,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,119,132,],[1,131,142,]),'SELECT_':([0,119,132,],[2,2,2,]),'FROM_':([2,],[4,]),'CAMPOS':([3,7,20,],[6,19,33,]),'CAMPO':([3,7,20,],[8,8,8,]),'FUNC_RESUMEN':([3,7,20,91,],[10,10,10,113,]),'JOIN_':([4,15,],[14,28,]),'JOIN_INNER_LEFT':([4,15,],[15,15,]),'WHERE_':([14,],[26,]),'GROUP_BY':([26,],[40,]),'COND_W':([27,45,58,59,78,79,81,107,109,],[42,61,75,76,105,106,108,124,125,]),'CONDICION':([27,45,58,59,78,79,81,107,109,],[43,43,43,43,43,43,43,43,43,]),'ORDER_BY':([40,],[55,]),'CAMPOS_G':([57,128,],[73,138,]),'CAMPOS_O':([72,143,],[88,145,]),'HAVING_':([73,],[90,]),'SUBCONSULTA':([77,],[93,]),'SIGNO':([77,113,],[94,127,]),'NULLEABLE':([77,],[95,]),'VALOR':([94,127,],[116,137,]),'ORDEN':([126,],[134,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> SELECT_ FROM_ JOIN_ WHERE_ GROUP_BY ORDER_BY','S',6,'p_S_consulta_completa','grupo03.py',89),
  ('SELECT_ -> SELECT CAMPOS','SELECT_',2,'p_SELECT_','grupo03.py',93),
  ('SELECT_ -> SELECT DISTINCT CAMPOS','SELECT_',3,'p_SELECT_','grupo03.py',94),
  ('CAMPOS -> CAMPO COMA CAMPOS','CAMPOS',3,'p_CAMPOS','grupo03.py',98),
  ('CAMPOS -> CAMPO','CAMPOS',1,'p_CAMPOS','grupo03.py',99),
  ('CAMPO -> CADENA PUNTO CADENA AS COMILLA CADENA COMILLA','CAMPO',7,'p_CAMPO','grupo03.py',103),
  ('CAMPO -> CADENA PUNTO CADENA','CAMPO',3,'p_CAMPO','grupo03.py',104),
  ('CAMPO -> FUNC_RESUMEN AS COMILLA CADENA COMILLA','CAMPO',5,'p_CAMPO','grupo03.py',105),
  ('FUNC_RESUMEN -> MIN PAR_IZQ CADENA PUNTO CADENA PAR_DER','FUNC_RESUMEN',6,'p_FUNC_RESUMEN','grupo03.py',118),
  ('FUNC_RESUMEN -> MAX PAR_IZQ CADENA PUNTO CADENA PAR_DER','FUNC_RESUMEN',6,'p_FUNC_RESUMEN','grupo03.py',119),
  ('FUNC_RESUMEN -> COUNT PAR_IZQ CADENA PUNTO CADENA PAR_DER','FUNC_RESUMEN',6,'p_FUNC_RESUMEN','grupo03.py',120),
  ('FUNC_RESUMEN -> COUNT PAR_IZQ DISTINCT CADENA PUNTO CADENA PAR_DER','FUNC_RESUMEN',7,'p_FUNC_RESUMEN','grupo03.py',121),
  ('FROM_ -> FROM CADENA CADENA','FROM_',3,'p_FROM_','grupo03.py',143),
  ('FROM_ -> FROM CADENA AS CADENA','FROM_',4,'p_FROM_','grupo03.py',144),
  ('FROM_ -> FROM CADENA','FROM_',2,'p_FROM_','grupo03.py',145),
  ('JOIN_ -> JOIN_INNER_LEFT JOIN_','JOIN_',2,'p_JOIN_','grupo03.py',160),
  ('JOIN_ -> <empty>','JOIN_',0,'p_JOIN_','grupo03.py',161),
  ('JOIN_INNER_LEFT -> INNER JOIN CADENA CADENA ON COND_W','JOIN_INNER_LEFT',6,'p_JOIN_INNER_LEFT','grupo03.py',164),
  ('JOIN_INNER_LEFT -> INNER JOIN CADENA AS CADENA ON COND_W','JOIN_INNER_LEFT',7,'p_JOIN_INNER_LEFT','grupo03.py',165),
  ('JOIN_INNER_LEFT -> LEFT JOIN CADENA CADENA ON COND_W','JOIN_INNER_LEFT',6,'p_JOIN_INNER_LEFT','grupo03.py',166),
  ('JOIN_INNER_LEFT -> LEFT JOIN CADENA AS CADENA ON COND_W','JOIN_INNER_LEFT',7,'p_JOIN_INNER_LEFT','grupo03.py',167),
  ('WHERE_ -> WHERE COND_W','WHERE_',2,'p_WHERE_','grupo03.py',176),
  ('WHERE_ -> <empty>','WHERE_',0,'p_WHERE_','grupo03.py',177),
  ('COND_W -> CONDICION','COND_W',1,'p_COND_W','grupo03.py',180),
  ('COND_W -> CADENA PUNTO CADENA SUBCONSULTA','COND_W',4,'p_COND_W','grupo03.py',181),
  ('COND_W -> COND_W AND COND_W','COND_W',3,'p_COND_W','grupo03.py',182),
  ('COND_W -> COND_W OR COND_W','COND_W',3,'p_COND_W','grupo03.py',183),
  ('COND_W -> PAR_IZQ COND_W OR COND_W PAR_DER','COND_W',5,'p_COND_W','grupo03.py',184),
  ('SUBCONSULTA -> IN PAR_IZQ S PAR_DER','SUBCONSULTA',4,'p_SUBCONSULTA','grupo03.py',198),
  ('SUBCONSULTA -> NOT IN PAR_IZQ S PAR_DER','SUBCONSULTA',5,'p_SUBCONSULTA','grupo03.py',199),
  ('VALOR -> NUMERO','VALOR',1,'p_VALOR','grupo03.py',202),
  ('VALOR -> COMILLA CADENA COMILLA','VALOR',3,'p_VALOR','grupo03.py',203),
  ('CONDICION -> CADENA PUNTO CADENA SIGNO VALOR','CONDICION',5,'p_CONDICION','grupo03.py',206),
  ('CONDICION -> CADENA PUNTO CADENA SIGNO CADENA PUNTO CADENA','CONDICION',7,'p_CONDICION','grupo03.py',207),
  ('CONDICION -> CADENA PUNTO CADENA NULLEABLE','CONDICION',4,'p_CONDICION','grupo03.py',208),
  ('NULLEABLE -> IS NOT NULL','NULLEABLE',3,'p_NULLEABLE','grupo03.py',235),
  ('NULLEABLE -> IS NULL','NULLEABLE',2,'p_NULLEABLE','grupo03.py',236),
  ('SIGNO -> IGUAL','SIGNO',1,'p_SIGNO','grupo03.py',239),
  ('SIGNO -> MAYOR','SIGNO',1,'p_SIGNO','grupo03.py',240),
  ('SIGNO -> MENOR','SIGNO',1,'p_SIGNO','grupo03.py',241),
  ('SIGNO -> MAYOR_IGUAL','SIGNO',1,'p_SIGNO','grupo03.py',242),
  ('SIGNO -> MENOR_IGUAL','SIGNO',1,'p_SIGNO','grupo03.py',243),
  ('SIGNO -> DESIGUAL','SIGNO',1,'p_SIGNO','grupo03.py',244),
  ('GROUP_BY -> GROUP BY CAMPOS_G HAVING_','GROUP_BY',4,'p_GROUP_BY','grupo03.py',247),
  ('GROUP_BY -> <empty>','GROUP_BY',0,'p_GROUP_BY','grupo03.py',248),
  ('CAMPOS_G -> CADENA PUNTO CADENA COMA CAMPOS_G','CAMPOS_G',5,'p_CAMPOS_G','grupo03.py',251),
  ('CAMPOS_G -> CADENA PUNTO CADENA','CAMPOS_G',3,'p_CAMPOS_G','grupo03.py',252),
  ('HAVING_ -> HAVING FUNC_RESUMEN SIGNO VALOR','HAVING_',4,'p_HAVING_','grupo03.py',261),
  ('HAVING_ -> <empty>','HAVING_',0,'p_HAVING_','grupo03.py',262),
  ('ORDER_BY -> ORDER BY CAMPOS_O','ORDER_BY',3,'p_ORDER_BY','grupo03.py',265),
  ('ORDER_BY -> <empty>','ORDER_BY',0,'p_ORDER_BY','grupo03.py',266),
  ('CAMPOS_O -> CADENA PUNTO CADENA ORDEN COMA CAMPOS_O','CAMPOS_O',6,'p_CAMPOS_O','grupo03.py',269),
  ('CAMPOS_O -> CADENA PUNTO CADENA ORDEN','CAMPOS_O',4,'p_CAMPOS_O','grupo03.py',270),
  ('ORDEN -> ASC','ORDEN',1,'p_ORDEN','grupo03.py',273),
  ('ORDEN -> DESC','ORDEN',1,'p_ORDEN','grupo03.py',274),
  ('ORDEN -> <empty>','ORDEN',0,'p_ORDEN','grupo03.py',275),
]
