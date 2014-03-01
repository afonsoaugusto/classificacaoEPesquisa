import sys
import time
from define import Entradas
from random import randint
from algoritimo import SelectionSort
from algoritimo import BubbleSort


def processaEntradas(argc,argv):
	if(argc == 2):
		return Entradas(int(argv[1]))
	return Entradas()

def geraVetor(entradas):
	lista = []
	for i in range (entradas.N):
		lista.append(randint(entradas.LOW, entradas.HIGH))
	return lista

def main():
	entradas = processaEntradas(len(sys.argv),sys.argv)
	vetor = geraVetor(entradas)
	print (vetor)
	select = BubbleSort(vetor)
	time_start = time.time()
	select.sort()
	time_stop = time.time()
	time_execution = time_stop - time_start
	print (vetor)	
	print ("Tempo de execucao: %f segundos" % time_execution)



main()
