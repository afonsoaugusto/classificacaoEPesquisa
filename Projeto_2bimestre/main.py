# -*- coding: utf-8 -*-
import sys
import time
from define import Algoritimo, Execucao,Detalhes
from random import randint
from controller import Controller



def buscaLinearInit(controller):
	nome = 'Busca Linear'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = 'Busca Linear'
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		algoritimo.classe = 'Algoritmo de busca'
		algoritimo.estruturaDados = 'Array, Listas ligadas'
		algoritimo.complexidadePiorCaso = 'O(n)'
		algoritimo.complexidadeMedioCaso = 'O(n/2)'
		algoritimo.complexidadeMelhorCaso = '{O}(1)'
		algoritimo.complexidadeEspacos = ''
		algoritimo.pseudoAlgoritimo = ''
		controller.persistirObjeto(algoritimo)
	return algoritimo
	
def buscaLinearSentinelaInit(controller):
	nome = 'Busca Linear Sentinela'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		algoritimo.classe = 'Algoritmo de busca'
		algoritimo.estruturaDados = 'Array, Listas ligadas'
		algoritimo.complexidadePiorCaso = '{O}(n)'
		algoritimo.complexidadeMedioCaso = 'O(n/2)'
		algoritimo.complexidadeMelhorCaso = '{O}(1)'
		algoritimo.complexidadeEspacos = ''
		algoritimo.pseudoAlgoritimo = ''
		controller.persistirObjeto(algoritimo)
	return algoritimo
	
def buscaLinearBinaria(controller):
	nome = 'Busca Binaria'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		algoritimo.classe = 'Algoritmo de busca'
		algoritimo.estruturaDados = 'Array, Listas ligadas'
		algoritimo.complexidadePiorCaso = 'O(\log n)'
		algoritimo.complexidadeMedioCaso = 'O(n/2)'
		algoritimo.complexidadeMelhorCaso = '{O}(1)'
		algoritimo.complexidadeEspacos = '{O}(\log n)'
		algoritimo.pseudoAlgoritimo = ''
		controller.persistirObjeto(algoritimo)
	return algoritimo
	
def ordenacaoSelecao(controller):
	nome = 'Ordenação Seleção'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		algoritimo.classe = 'Algoritmo de odernação'
		algoritimo.estruturaDados = 'Array, Listas ligadas'
		algoritimo.complexidadePiorCaso = 'O(n^2)'
		algoritimo.complexidadeMedioCaso = 'O(n^2)'
		algoritimo.complexidadeMelhorCaso = 'O(n^2)'
		algoritimo.complexidadeEspacos = 'O(n) total, O(1) auxiliar'
		algoritimo.pseudoAlgoritimo = ''
		controller.persistirObjeto(algoritimo)
	return algoritimo



# ****** #
sys.setrecursionlimit(2 ** 30)
controller = Controller()

buscaLinear = buscaLinearInit(controller) 
print buscaLinear.id
buscaLinearSentinela = buscaLinearSentinelaInit(controller)
buscaBinaria = buscaLinearBinaria(controller)
selecao = ordenacaoSelecao(controller)
bubblesort = Algoritimo()
arvoreBinaria = Algoritimo()
arvoreAvl = Algoritimo()
arvoreBTree = Algoritimo()




