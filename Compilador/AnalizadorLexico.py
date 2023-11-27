import ply.lex as lex
import re
import codecs
import os
import sys
from tkinter import *

tokens =[
      'ID',
      'NUMERO',
      'SUMA',
      'ASIGNACION',
      'RESTA',
      'DIVISION',
      'MULTIPLICACION',

      'IGUAL',
      'DIFERENTE',
      'MAYORQUE',
      'MENORQUE',
      'MAYORIGUAL',
      'MENORIGUAL',

      'PUNTO',
      'COMA',
      'DOSPUNTOS',
      'PUNTOCOMA',
      'COMILLASSIMPLES',
      'COMILLASDOBLES',
      'PARENTESIS_A',
      'PARENTESIS_C',
      'LLAVE_A',
      'LLAVE_C',
      'CORCHETE_A',
      'CORCHETE_C',

      'MASMAS',
      'MENOSMENOS',
      ]

reservadas = {
  'import':'IMPORT',
  'def':'DEF',
  'class':'CLASS',
  'if':'IF',
  'else':'ELSE',
  'for':'FOR',
  'in':'IN',
  'range':'RANGE',
  'self':'SELF',
  'while':'WHILE',
  'try':'TRY',
  'except':'EXCEPT',
  'return':'RETURN',
  'break':'BREAK',
  'next':'NEXT',
  
  'input':'LEER',
  'print':'IMPRIMIR',
  'int':'ENTER',
  'float':'DECIMAL',
  'boolean':'BOOLEANO',
  'str':'CADENA',
  
  'pow':'POTENCIA',
  'math.sqrt':'RAIZ',
  'and':'AND',
  'or':'OR',
  'not':'NOT',
  }
 
tokens = tokens+list(reservadas.values())

t_ignore = '\t'

#Operadores matematicos
t_SUMA = r'\+'
t_ASIGNACION = r'='
t_RESTA = r'-'
t_DIVISION = r'/'
t_MULTIPLICACION = r'\*'

#Operadores racionales
t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='

#Variables
t_PUNTO = r'\.'
t_COMA = r'\,'
t_DOSPUNTOS = r'\:'
t_PUNTOCOMA = r'\;'
t_COMILLASSIMPLES = r'\''
t_COMILLASDOBLES = r'\""'
t_PARENTESIS_A = r'\('
t_PARENTESIS_C = r'\)'
t_LLAVE_A = r'\{'
t_LLAVE_C = r'\}'
t_CORCHETE_A = r'\['
t_CORCHETE_C = r'\]'

#Operadores de incremento y decremento
t_MASMAS = r'\+\+'
t_MENOSMENOS = r'\-\-'

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z0-9_]'
  if t.value.upper() in reservadas:
    t.value = t.value.upper()
    t.type = t.value
  return t

def t_SALTOLINEA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_COMENTARIO(t):
    r'\#.*'
    pass

def t_NUMERO(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_error(t):
  t.lexer.skip(1)
  return "Caracter Ilegal"

a = []

def analisis(cadena):
  analizador = lex.lex()
  analizador.input(cadena)
  a.clear()

  while True:
    tok = analizador.token()
    if not tok : break
    a.append(str(tok))
  return a

"""
cadena1= "Hola \n hola"
analisis(cadena1)
print(a)
"""
