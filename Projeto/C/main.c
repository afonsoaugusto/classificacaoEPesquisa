#include "define.h"
#include "selection_sort.h"
#include "bubble_sort.h"

void processaEntrada(int argc, char*argv[], Entrada *entradas);
void geraVetor (int vetor[],Entrada *entradas);
void imprimiVetor (Vetor vetor[],Entrada *entradas);
/*
1. Busca linear. 
2. Busca linear com sentinela. 
3. Busca Binária. 
4. Ordenação usando seleção. 
5. Ordenação usando bubblesort.
*/

int main(int argc,char *argv[]){
	Entrada entradas;
	processaEntrada(argc,argv, &entradas);
	int vetor[entradas.N];

	geraVetor(vetor,&entradas);
	printf("\n");
	
    double tstart, tstop, ttime;
    tstart = (double)clock()/CLOCKS_PER_SEC;
//	selection_sort(vetor, entradas.N);
	bubbleSort(vetor, entradas.N);
    tstop = (double)clock()/CLOCKS_PER_SEC;
    ttime= tstop-tstart; /*ttime is how long your code run */
	imprimiVetor(vetor,&entradas);
    printf("\nTempo de execucao: %f segundos\n",ttime);
	return 0;
}

void processaEntrada(int argc, char*argv[], Entrada *entradas){
	if (argc == 2){
		entradas->N = atoi(argv[1]);
		entradas->LOW = 0;
		entradas->HIGH = 100000;
		entradas->SEED = 1234554321;
		entradas->NUM_FIND = 87;
		entradas->NUM_SECOND_FIND = 100001;
	}else 
	if (argc == 7){
		entradas->N = atoi(argv[1]);
		entradas->LOW = atoi(argv[2]);
		entradas->HIGH = atoi(argv[3]);
		entradas->SEED = atoi(argv[4]);
		entradas->NUM_FIND = atoi(argv[5]);
		entradas->NUM_SECOND_FIND = atoi(argv[6]);
	}else{
		entradas->N = 100;
		entradas->LOW = 0;
		entradas->HIGH = 100000;
		entradas->SEED = 1234554321;
		entradas->NUM_FIND = 87;
		entradas->NUM_SECOND_FIND = 100001;
	}
}

void geraVetor (Vetor vetor[],Entrada *entradas){
	int i;
	for (i=0;i<entradas->N;i++){
		vetor[i] = inteiros_unif(&(entradas->SEED), entradas->LOW, entradas->HIGH);
	}	
}

void imprimiVetor (Vetor vetor[],Entrada *entradas){
	int i;
	for (i=0;i<entradas->N;i++){
		printf("%d ",vetor[i]);
	}	

}
