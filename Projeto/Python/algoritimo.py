class Algorithm(object):

	def __init__(self, vetor):
		self.vetor = vetor

	def sort(self):
		pass

class SelectionSort(Algorithm):

	def sort(self):
		vetor = self.vetor
		for i in range(len(vetor)-1):
			min = i
			for j in range((i+1),len(vetor)):
				if(vetor[j] < vetor[min]):
					min = j
			if(i != min):
				swap = vetor[i]
				vetor[i] = vetor[min]
				vetor[min] = swap

class BubbleSort(Algorithm):

	def sort(self):
		vetor = self.vetor
		for i in range((len(vetor)-1),0,-1):
			for j in range(1,i):
				if(vetor[j-1] > vetor[j]):
					vetor[j-1],vetor[j] = vetor[j],vetor[j-1]

class ShellSort(Algorithm):

	def sort(self):
 		array = self.vetor
#		 "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
		gap = len(array) // 2
		 # loop over the gaps
		while gap > 0:
		     # do the insertion sort
			for i in range(gap, len(array)):
				val = array[i]
				j = i
				while j >= gap and array[j - gap] > val:
					array[j] = array[j - gap]
					j -= gap
				array[j] = val
			gap //= 2

