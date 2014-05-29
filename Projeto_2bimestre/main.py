# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import sys
import time
from define import Algoritimo, Execucao,Detalhes
from random import randint
from controller import Controller
from utils import Util
from algoritimo_count import SelectionSort
from algoritimo_count import BubbleSort
from algoritimo_count import ShellSort
from algoritimo_count import InsertionSort
from algoritimo_count import Quicksort
from algoritimo_count import Heapsort
from algoritimo_count import SearchLinear
from algoritimo_count import SearchLinearSentinel

util = Util()

def main():
	sys.setrecursionlimit(2 ** 30)
	controller = Controller()

	buscaLinear = buscaLinearInit(controller) 
	buscaLinearSentinela = buscaLinearSentinelaInit(controller)
	buscaBinaria = buscaLinearBinariaInit(controller)
	selecao = ordenacaoSelecaoInit(controller)
	bubblesort = ordenacaoBolhaInit(controller)
	arvoreBinaria = arvoreBinariaInit(controller)
	arvoreAvl = arvoreAVLInit(controller)
	arvoreBTree = arvoreBTreeInit(controller)
	n = 25
	for i in range(3):
		for a in (['-A','-D','-C']):
			execucao = Execucao()
			execucao.MODE = a
			execucao.N = n * n
			execucao = controller.persistirObjeto(execucao)
			vector = util.geraVetor(execucao)
			#util.imprimir(vector)



			#parte individual de cada teste
			detalhes = detalhesInit(execucao,selecao)
			select = SelectionSort(vector[:])
			detalhes = verificaTempo(select,detalhes)
			detalhes = controller.persistirObjeto(detalhes)

			detalhes = detalhesInit(execucao,bubblesort)
			select = BubbleSort(vector[:])
			detalhes = verificaTempo(select,detalhes)
			detalhes = controller.persistirObjeto(detalhes)

			detalhes = detalhesInit(execucao,buscaLinear)
			find = SearchLinear(vector[:])
			detalhes = verificaTempoBusca(find,execucao,detalhes)
			detalhes = controller.persistirObjeto(detalhes)

			detalhes = detalhesInit(execucao,buscaLinearSentinela)
			find = SearchLinearSentinel(vector[:])
			detalhes = verificaTempoBusca(find,execucao,detalhes)
			detalhes = controller.persistirObjeto(detalhes)



def verificaTempoBusca(find,execucao,detalhes):
	time_start = time.time()
	indice = find.find(execucao.NUM_FIND)
	time_stop = time.time()
	time_execution = time_stop - time_start
	detalhes.tempoExecucao = time_execution
	detalhes.quantidadeComparacoes = find.comparacao
	detalhes.quantidadeTrocas = find.troca
	util.imprimir(indice)
	return detalhes

def verificaTempo(select,detalhes):
	time_start = time.time()
	select.sort()
	time_stop = time.time()
	time_execution = time_stop - time_start
	detalhes.tempoExecucao = time_execution
	detalhes.quantidadeComparacoes = select.comparacao
	detalhes.quantidadeTrocas = select.troca
	return detalhes





#Inicialização de objetos
def detalhesInit(execucao,algoritimo):
	detalhes = Detalhes()
	detalhes.execucao_id = execucao.id
	detalhes.algoritimo_id = algoritimo.id
	return detalhes

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
		algoritimo = controller.persistirObjeto(algoritimo)
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
		algoritimo = controller.persistirObjeto(algoritimo)
	return algoritimo
	
def buscaLinearBinariaInit(controller):
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
		algoritimo = controller.persistirObjeto(algoritimo)
	return algoritimo
	
def ordenacaoSelecaoInit(controller):
	nome = 'Ordenação Seleção'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		algoritimo.classe = 'Algoritmo de ordenação'
		algoritimo.estruturaDados = 'Array, Listas ligadas'
		algoritimo.complexidadePiorCaso = u'O(n^2)'
		algoritimo.complexidadeMedioCaso = u'O(n^2)'
		algoritimo.complexidadeMelhorCaso = u'O(n^2)'
		algoritimo.complexidadeEspacos = u'O(n) total, O(1) auxiliar'
		algoritimo.pseudoAlgoritimo = ''
		algoritimo = controller.persistirObjeto(algoritimo)
	return algoritimo

def ordenacaoBolhaInit(controller):
	nome = 'Ordenação BubbleSort'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		algoritimo.classe = 'Algoritmo de ordenação'
		algoritimo.estruturaDados = 'Array, Listas ligadas'
		algoritimo.complexidadePiorCaso = u'O(n^2)'
		algoritimo.complexidadeMedioCaso = u'O(n^2)'
		algoritimo.complexidadeMelhorCaso = u'O(n)'
		algoritimo.complexidadeEspacos = u'O(1) auxiliar'
		algoritimo.pseudoAlgoritimo = ''
		algoritimo = controller.persistirObjeto(algoritimo)
	return algoritimo
	
def arvoreBinariaInit(controller):
	nome = 'Arvore Binaria'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		algoritimo = controller.persistirObjeto(algoritimo)
	return algoritimo

	
def arvoreAVLInit(controller):
	nome = 'Arvore AVL'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		algoritimo = controller.persistirObjeto(algoritimo)
	return algoritimo
	
def arvoreBTreeInit(controller):
	nome = 'Arvore B-Tree'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		algoritimo = controller.persistirObjeto(algoritimo)
	return algoritimo

	
# ****** #
main()




