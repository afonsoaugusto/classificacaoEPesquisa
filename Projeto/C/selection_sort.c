#include "selection_sort.h"
void selection_sort(int num[], int tam) 
{ 
  int i, j, min, swap;
  for (i = 0; i < (tam-1); i++) 
   {
    min = i;
    for (j = (i+1); j < tam; j++) {
      if(num[j] < num[min]) {
        min = j;
      }
    }
    if (i != min) {
      swap = num[i];
      num[i] = num[min];
      num[min] = swap;
    }
  }
}
/*
void selection_sort_name() {
    int i,j,n;
    for(i=0; i<n-1; i++) {
        for(j=i+1; j<n; j++) {
            if(strcmp(vetor[i], vetor[j])>0) {
            strcpy(aux_char, vetor[i]);
            strcpy(vetor[i], vetor[j]);
            strcpy(vetor[j], aux_char);
        }
    }
}*/
