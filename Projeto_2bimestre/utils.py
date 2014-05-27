# -*- coding: utf-8 -*-
import sys
import time
from random import randint
from define import Execucao


class Util(Object):
	def geraVetor(execucao):
		lista = []
		
		if execucao.MODO == "-A":
			for i in range (execucao.N):
				lista.append(randint(execucao.LOW, execucao.HIGH))
			return lista
			
		if execucao.MODO == "-C":
			for i in range (execucao.N):
				lista.append(i)
			return lista
			
		if execucao.MODO == "-D":
			for i in range (execucao.N-1,-1,-1):
				lista.append(i)
			return lista
		return lista
		