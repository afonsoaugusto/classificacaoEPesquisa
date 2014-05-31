# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import sys
import time
from random import randint
from define import Execucao
import datetime


class Util():
	DEBUG = 'DEBUG'
	ERROR = 'ERROR'
	INFO  = 'INFO'
	NIVEL_ASSUMIDO = [ERROR,DEBUG]
	def geraVetor(self, execucao):
		lista = []
		
		if execucao.MODE == "-A":
			for i in range (execucao.N):
				lista.append(randint(execucao.LOW, execucao.HIGH))
			return lista
			
		if execucao.MODE == "-C":
			for i in range (execucao.N):
				lista.append(i)
			return lista
			
		if execucao.MODE == "-D":
			for i in range (execucao.N-1,-1,-1):
				lista.append(i)
			return lista
		return lista

	def imprimir(self,nivel,objeto):
		if nivel in self.NIVEL_ASSUMIDO:
			name = 'classPesq'
			f = open(name+ str(datetime.date.today())+'.log','a')
			f.write(nivel +' '+str(datetime.datetime.utcnow()) + ' - '+  str(objeto) + '\n') 
			f.close() 
			print str(objeto)
		