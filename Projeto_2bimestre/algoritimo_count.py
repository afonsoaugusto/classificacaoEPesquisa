# -*- coding: utf-8 -*-
class AlgorithmInterface(object):
        
	def __init__(self, vetor):
		pass

	def sort(self):
		pass

class Algorithm(AlgorithmInterface):

	def __init__(self, vetor):
		self.vetor = vetor
		self.comparacao = 0
		self.troca = 0

	def sort(self):
		pass

class SelectionSort(Algorithm):

	def sort(self):
		vetor = self.vetor
		for i in range(len(vetor)-1):
			min = i
			for j in range((i+1),len(vetor)):
                                self.comparacao += 1
				if(vetor[j] < vetor[min]):
					min = j
					
			self.comparacao += 1
			if(i != min):
				vetor[i],vetor[min] = vetor[min],vetor[i]
				self.troca += 1



class BubbleSort(Algorithm):

	def sort(self):
		self.comparacao = 0
		self.troca = 0
		vetor = self.vetor
		for i in range((len(vetor)-1),0,-1):
			for j in range(1,i):
                                self.comparacao += 1
				if(vetor[j-1] > vetor[j]):
					vetor[j-1],vetor[j] = vetor[j],vetor[j-1]
					self.troca += 1



class ShellSort(Algorithm):

	def sort(self):
		self.comparacao = 0
		self.troca = 0
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
					self.comparacao += 2
					self.troca += 1
				array[j] = val
			gap //= 2



class InsertionSort(Algorithm):

	def sort(self):
 		v = self.vetor
		self.comparacao = 0
		self.troca = 0
		for j in range(1, len(v)):
			chave = v[j]
			i = j - 1
			while i >= 0 and v[i] > chave:
				v[i + 1] = v[i]
				i -= 1
				self.comparacao += 2
				self.troca += 1
			v[i + 1] = chave



class Quicksort(Algorithm):

	"Everybody's favourite sorting algorithm... :)"
	def partition(self,list, start, end):
		pivot = list[end]                          # Partition around the last value
		bottom = start-1                           # Start outside the area to be partitioned
		top = end                                  # Ditto


		done = 0
		while not done:                            # Until all elements are partitioned...


			while not done:                        # Until we find an out of place element...
				bottom = bottom+1                  # ... move the bottom up.


                                self.comparacao += 1
				if bottom == top:					# If we hit the top...
					done = 1                       # ... we are done.
					break

                                self.comparacao += 1
				if list[bottom] > pivot:           # Is the bottom out of place?
					list[top] = list[bottom]       # Then put it at the top...
					self.troca += 1
					break                          # ... and start searching from the top.


				while not done:                        # Until we find an out of place element...
					top = top-1                        # ... move the top down.


                                        self.comparacao += 1
                                        if top == bottom:                  # If we hit the bottom...
                                                done = 1                       # ... we are done.
                                                break


                                        self.comparacao += 1
                                        if list[top] < pivot:              # Is the top out of place?
                                                list[bottom] = list[top]       # Then put it at the bottom...
                                                self.troca += 1
                                                break                          # ...and start searching from the bottom.


		list[top] = pivot                          # Put the pivot in its place.
		self.troca += 1
		return top                                 # Return the split point




	def quicksort(self,list, start, end):
                self.comparacao += 1
		if start < end:                            # If there are two or more elements...
			split = self.partition(list, start, end)    # ... partition the sublist...
			self.quicksort(list, start, split-1)        # ... and sort both halves.
			self.quicksort(list, split+1, end)
		else:
		    return


	def sort(self):
		self.comparacao = 0
		self.troca = 0
		list = self.vetor 				              # Get all the arguments
		start = 0
		end = len(list)-1
		self.quicksort(list,start,end)                  # Sort the entire list of arguments


class Heapsort(Algorithm):

	def sift_down(self,arr, root, bottom):
		while root*2 <= bottom:
                        self.comparacao += 1
			if root*2 == bottom:
				newr = root*2
			elif arr[root*2-1]>arr[root*2]:
				newr = root*2
				self.comparacao += 1
			else:
				newr = root*2 + 1
				self.comparacao += 1

                        self.comparacao += 1
			if arr[root-1] < arr[newr-1]:
				arr[root-1], arr[newr-1] = arr[newr-1], arr[root-1]
				root=newr
				self.troca += 1
			else:
				break

	def heapsort(self,arr):
		for i in range( len(arr)/2,  0, -1 ):
			self.sift_down(arr, i, len(arr))
		for i in range( len(arr), 0, -1 ):
			arr[i-1], arr[0] = arr[0], arr[i-1]
			self.sift_down(arr, 1, i-1)
			self.troca += 1

	def sort(self):
		self.comparacao = 0
		self.troca = 0
		list = self.vetor 
		self.heapsort(list) 

