import sys
import time
from define import Algoritimo, Execucao,Detalhes
from random import randint
from controller import Controller

# ****** #
sys.setrecursionlimit(2 ** 30)
c2 = Controller()

execucao  = Execucao()
c2.persistirObjeto(execucao)

import sqlite3
conn = sqlite3.connect('classificacao_pesquisa.db')

c = conn.cursor()
c.execute('SELECT * FROM execucao')
print c.fetchall()
conn.close()

execucao = 
execucao.MODE = 'TA'
c2.persistirObjeto(execucao)

import sqlite3
conn = sqlite3.connect('classificacao_pesquisa.db')

c = conn.cursor()
c.execute('SELECT * FROM execucao')
print c.fetchall()
conn.close()