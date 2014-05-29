# -*- coding: utf-8 -*-
import sys
import time
from random import randint
from define import Execucao


class Util():
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

	def imprimir(self,objeto):
		print objeto
		