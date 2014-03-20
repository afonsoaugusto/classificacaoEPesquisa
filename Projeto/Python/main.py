import sys
import time
from define import Entradas
from random import randint
from algoritimo import SelectionSort
from algoritimo import BubbleSort
from algoritimo import ShellSort

def processaEntradas(argv):
	argc = len(argv)
	if(argc == 2):
		return Entradas(int(argv[1]))

	if(argc == 3):
		return Entradas(int(argv[1]),argv[2])
	return Entradas()

def geraVetor(entradas):
	lista = []
	for i in range (entradas.N):
		lista.append(randint(entradas.LOW, entradas.HIGH))
	return lista

def geraAlgoritimo(vetor,algo):
	if algo == "ShellSort":
		return ShellSort(vetor)
	if algo == "SelectionSort":
		return SelectionSort(vetor)	
	if algo == "BubbleSort":
		return BubbleSort(vetor)

def verificaTempo(select):
	time_start = time.time()
	select.sort()
	time_stop = time.time()
	time_execution = time_stop - time_start
	print ("Tempo de execucao: %f segundos" % time_execution)

def main():
	entradas = processaEntradas(sys.argv)
	vetor = geraVetor(entradas)

	select = geraAlgoritimo(vetor[:], "ShellSort")
	print "ShellSort"
	verificaTempo(select)

	select = geraAlgoritimo(vetor[:], "SelectionSort")
	print "SelectionSort"
	verificaTempo(select)

	select = geraAlgoritimo(vetor[:], "BubbleSort")
	print "BubbleSort"
	verificaTempo(select)



main()
