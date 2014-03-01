
class SelectionSort:

	def __init__(self, vetor):
		self.vetor = vetor

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

class BubbleSort:

	def __init__(self, vetor):
		self.vetor = vetor

	def sort(self):
		vetor = self.vetor
		for i in range((len(vetor)-1),1,-1):
			for j in range((i+1),len(vetor)):
				if(vetor[j-1] < vetor[j]):
					vetor[j-1],vetor[j] = vetor[j],vetor[j-1]


