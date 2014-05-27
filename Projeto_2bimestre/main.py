# -*- coding: utf-8 -*-
import sys
import time
from define import Algoritimo, Execucao,Detalhes
from random import randint
from controller import Controller
from utils

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
		controller.persistirObjeto(algoritimo)
	return algoritimo
	
def ordenacaoSelecaoInit(controller):
	nome = 'Ordenacao Selecao'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		algoritimo.classe = 'Algoritmo de odernacao'
		algoritimo.estruturaDados = 'Array, Listas ligadas'
		algoritimo.complexidadePiorCaso = u'O(n^2)'
		algoritimo.complexidadeMedioCaso = u'O(n^2)'
		algoritimo.complexidadeMelhorCaso = u'O(n^2)'
		algoritimo.complexidadeEspacos = u'O(n) total, O(1) auxiliar'
		algoritimo.pseudoAlgoritimo = ''
		controller.persistirObjeto(algoritimo)
	return algoritimo

def ordenacaoBolhaInit(controller):
	nome = 'Ordenacao BubbleSort'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		algoritimo.classe = 'Algoritmo de odernacao'
		algoritimo.estruturaDados = 'Array, Listas ligadas'
		algoritimo.complexidadePiorCaso = u'O(n^2)'
		algoritimo.complexidadeMedioCaso = u'O(n^2)'
		algoritimo.complexidadeMelhorCaso = u'O(n)'
		algoritimo.complexidadeEspacos = u'O(1) auxiliar'
		algoritimo.pseudoAlgoritimo = ''
		controller.persistirObjeto(algoritimo)
	return algoritimo
	
def arvoreBinariaInit(controller):
	nome = 'Arvore Binaria'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		controller.persistirObjeto(algoritimo)
	return algoritimo

	
def arvoreAVLInit(controller):
	nome = 'Arvore AVL'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		controller.persistirObjeto(algoritimo)
	return algoritimo
	
def arvoreBTreeInit(controller):
	nome = 'Arvore B-Tree'
	algoritimo = Algoritimo()
	algoritimo.nomeAlgoritimo = nome
	algoritimo = controller.findAlgoritimo(algoritimo)
	if algoritimo == None:
		algoritimo = Algoritimo()
		algoritimo.nomeAlgoritimo = nome
		controller.persistirObjeto(algoritimo)
	return algoritimo

	
# ****** #
main()




