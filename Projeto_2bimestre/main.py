# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import sys
import time
from define import Algoritimo, Execucao,Detalhes
from random import randint
from controller import Controller
from utils import Util
from algoritimo_count import SelectionSort, BubbleSort, ShellSort
from algoritimo_count import InsertionSort, Quicksort, Heapsort
from algoritimo_count import SearchLinear, SearchLinearSentinel
from algoritimo_count import SearchBinary, SearchBinaryRecursion
from treeBinary import searchtree
from treeAvl import AVLTree
from bTree import BTree

util = Util()

def main():
	sys.setrecursionlimit(2 ** 30)
	controller = Controller()

	buscaLinear = algoritimoInit(controller,'Busca Linear','Algoritmo de busca','Array, Listas ligadas','O(n)','O(n/2)','{O}(1)','')
	buscaLinearSentinela = algoritimoInit(controller,'Busca Linear Sentinela','Algoritmo de busca','Array, Listas ligadas','O(n)','O(n/2)','{O}(1)','')
	buscaBinaria = algoritimoInit(controller,'Busca Binaria','Algoritmo de busca','Array, Listas ligadas','O(\log n)','O(n/2)','{O}(1)','{O}(\log n)')
	selecao = algoritimoInit(controller,'Ordenação Seleção','Algoritmo de ordenação','Array, Listas ligadas','O(n^2)','O(n^2)','O(n^2)','O(n) total, O(1) auxiliar')
	bubblesort = algoritimoInit(controller,'Ordenação BubbleSort','Algoritmo de ordenação','Array, Listas ligadas','O(n^2)','O(n^2)','O(n)','O(1) auxiliar')
	arvoreBinaria = algoritimoInit(controller,'Arvore Binaria','Arvore','Array, Listas ligadas',' ',' ',' ',' ')
	arvoreAvl = algoritimoInit(controller,'Arvore AVL','Arvore','Array, Listas ligadas',' ',' ',' ',' ')
	arvoreBTree = algoritimoInit(controller,'Arvore B-Tree','Arvore','Array, Listas ligadas',' ',' ',' ',' ')

	ex1 = [10000,30000,50000]
	ex2 = [10000,30000,50000]
	ex3 = [10000,30000,50000]
	#ex1 = [50,500,1000]
	#ex2 = [50,500,1000]
	#ex3 = [50,500,1000]
	for i in ([ex1,ex2,ex3]):
		for b in i:
			for a in (['-A','-C','-D']):
				execucao = Execucao()
				execucao.MODE = a
				execucao.N = b
				execucao = controller.persistirObjeto(execucao)
				vector = util.geraVetor(execucao)
				util.imprimir(util.DEBUG, ('-------- Execucao de numero:' + str(execucao.id) + ' --------'))
				util.imprimir(util.DEBUG, ('tamanho do vetor:' + str(len(vector)) + ' Modo: '+a ))
				
				#parte individual de cada teste
				'''
				util.imprimir(util.DEBUG,'selecao')
				detalhes = detalhesInit(execucao,selecao)
				select = SelectionSort(vector[:])
				detalhes = verificaTempo(select,detalhes)
				detalhes = controller.persistirObjeto(detalhes)

				util.imprimir(util.DEBUG,'bubblesort')
				detalhes = detalhesInit(execucao,bubblesort)
				select = BubbleSort(vector[:])
				detalhes = verificaTempo(select,detalhes)
				detalhes = controller.persistirObjeto(detalhes)
				
				#Seção de buscas
				util.imprimir(util.DEBUG,'buscaLinear')			
				detalhes = detalhesInit(execucao,buscaLinear)
				find = SearchLinear(vector[:])
				detalhes = verificaTempoBusca(find,execucao,detalhes)
				detalhes = controller.persistirObjeto(detalhes)

				util.imprimir(util.DEBUG,'buscaLinearSentinela')
				detalhes = detalhesInit(execucao,buscaLinearSentinela)
				find = SearchLinearSentinel(vector[:])
				detalhes = verificaTempoBusca(find,execucao,detalhes)
				detalhes = controller.persistirObjeto(detalhes)
				'''

				vetorOrdenado = vector[:]
				vetorOrdenado.sort()

				util.imprimir(util.DEBUG,'buscaBinaria')
				detalhes = detalhesInit(execucao,buscaBinaria)
				find = SearchBinary(vetorOrdenado[:])
				detalhes = verificaTempoBusca(find,execucao,detalhes)
				detalhes = controller.persistirObjeto(detalhes)
				'''
				util.imprimir(util.DEBUG,'arvoreBinaria')
				detalhes = detalhesInit(execucao,arvoreBinaria)
				tree = searchtree()		
				verificaTempoArvore(execucao,detalhes,vector[:],tree)
				detalhes = controller.persistirObjeto(detalhes)

				util.imprimir(util.DEBUG,'arvoreAvl')
				detalhes = detalhesInit(execucao,arvoreAvl)
				verificaTempoArvoreAVL(execucao,detalhes,vector[:])
				detalhes = controller.persistirObjeto(detalhes)
				

				util.imprimir(util.DEBUG,'arvoreBTree')
				detalhes = detalhesInit(execucao,arvoreBTree)
				util.imprimir(util.DEBUG,'ordem:' + str(b/2))
				tree = BTree(b/2)		
				verificaTempoArvore(execucao,detalhes,vector[:],tree)
				detalhes = controller.persistirObjeto(detalhes)
'''
				'''
				util.imprimir(util.DEBUG,'Breadth-First Traversal')
				tree.bft()
				util.imprimir(util.DEBUG,'Inorder Traversal')
				tree.inorder(tree.root) 
				util.imprimir(util.DEBUG,'Preorder Traversal')
				tree.preorder(tree.root) 
				util.imprimir(util.DEBUG,'Postorder Traversal')
				tree.postorder(tree.root) 
				'''
				
			
			
def verificaTempoArvoreAVL(execucao,detalhes,vector):
	time_start = time.time()
	arvore = AVLTree(vector)	
	time_stop = time.time()
	time_execution = time_stop - time_start
	arvore.sanity_check()
	detalhes.tempoExecucao = time_execution
	detalhes.quantidadeComparacoes = arvore.comparacao
	detalhes.quantidadeTrocas = arvore.troca
	util.imprimir(util.DEBUG, 'time_execution: '+ str(time_execution))
	return detalhes


def verificaTempoArvore(execucao,detalhes,vector,arvore):
	time_start = time.time()
	for i in (vector):
		arvore.insert(i)
	time_stop = time.time()
	time_execution = time_stop - time_start
	detalhes.tempoExecucao = time_execution
	detalhes.quantidadeComparacoes = arvore.comparacao
	detalhes.quantidadeTrocas = arvore.troca
	util.imprimir(util.DEBUG, 'time_execution: '+ str(time_execution))
	return detalhes


def verificaTempoBusca(find,execucao,detalhes):
	time_start = time.time()
	indice = find.find(execucao.NUM_FIND)
	time_stop = time.time()
	time_execution = time_stop - time_start
	detalhes.tempoExecucao = time_execution
	detalhes.quantidadeComparacoes = find.comparacao
	detalhes.quantidadeTrocas = find.troca
	util.imprimir(util.DEBUG, 'INDICE: '+ str(indice))
	util.imprimir(util.DEBUG, 'time_execution: '+ str(time_execution))
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

def algoritimoInit(controller,nome,classe,estruturaDados,complexidadePiorCaso,complexidadeMedioCaso,complexidadeMelhorCaso,complexidadeEspacos):
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		algoritimo.classe = classe
		algoritimo.estruturaDados = estruturaDados
		algoritimo.complexidadePiorCaso = complexidadePiorCaso
		algoritimo.complexidadeMedioCaso = complexidadeMedioCaso
		algoritimo.complexidadeMelhorCaso = complexidadeMelhorCaso
		algoritimo.complexidadeEspacos = complexidadeEspacos
		algoritimo.pseudoAlgoritimo = ''
		algoritimo = controller.persistirObjeto(algoritimo)
	return algoritimo
	


# ****** #
main()




