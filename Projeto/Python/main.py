import sys
import time
from define import Entradas
from random import randint

print "Informe ''1'' para algoritimo sera executado com os contadores ou ''0'' para nao"

a = input()

if a == 1:
	from algoritimo_count import SelectionSort
	from algoritimo_count import BubbleSort
	from algoritimo_count import ShellSort
	from algoritimo_count import InsertionSort
	from algoritimo_count import Quicksort
	from algoritimo_count import Heapsort
else:
	from algoritimo import SelectionSort
	from algoritimo import BubbleSort
	from algoritimo import ShellSort
	from algoritimo import InsertionSort
	from algoritimo import Quicksort
	from algoritimo import Heapsort
	



def processaEntradas(argv):
	argc = len(argv)
	if(argc == 2):
		return Entradas(int(argv[1]))

	if(argc == 3):
		return Entradas(int(argv[1]),argv[2])
	return Entradas()

def geraVetor(entradas):
	lista = []
	
	if entradas.MODO == "-A":
		for i in range (entradas.N):
			lista.append(randint(entradas.LOW, entradas.HIGH))
		return lista
		
	if entradas.MODO == "-C":
		for i in range (entradas.N):
			lista.append(i)
		return lista
		
	if entradas.MODO == "-D":
		for i in range (entradas.N-1,-1,-1):
			lista.append(i)
		return lista
	return lista
	
def geraAlgoritimo(vetor,algo):
	if algo == "ShellSort":
		return ShellSort(vetor)
	if algo == "SelectionSort":
		return SelectionSort(vetor)	
	if algo == "BubbleSort":
		return BubbleSort(vetor)
	if algo == "InsertionSort":
		return InsertionSort(vetor)
	if algo == "Quicksort":
		return Quicksort(vetor)
	if algo == "Heapsort":
		return Heapsort(vetor)


def verificaTempo(select):
	time_start = time.time()
	select.sort()
	time_stop = time.time()
	time_execution = time_stop - time_start
	print ("Tempo de execucao: %f segundos" % time_execution)

def main():
	entradas = processaEntradas(sys.argv)
	vetor = geraVetor(entradas)

	select = geraAlgoritimo(vetor[:], "SelectionSort")
	print "SelectionSort"
	verificaTempo(select)

	select = geraAlgoritimo(vetor[:], "InsertionSort")
	print "InsertionSort"
	verificaTempo(select)

	select = geraAlgoritimo(vetor[:], "ShellSort")
	print "ShellSort"
	verificaTempo(select)

	select = geraAlgoritimo(vetor[:], "Quicksort")
	print "Quicksort"
	verificaTempo(select)

	select = geraAlgoritimo(vetor[:], "Heapsort")
	print "Heapsort"
	verificaTempo(select)

	select = geraAlgoritimo(vetor[:], "BubbleSort")
	print "BubbleSort"
	verificaTempo(select)

for i in range (3):
	sys.setrecursionlimit(2 ** 30)
	main()
