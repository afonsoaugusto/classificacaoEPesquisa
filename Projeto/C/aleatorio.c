#include "aleatorio.h"
/********************************************************** 
Algoritmo 1 – Gerador de números reais aleatórios 
Gerador de distribuicao uniforme retorna um numero 
double (real com longa precisão) na faixa low – high, 
ou seja, [low,high]. 
**********************************************************/ 
double unif(long int *seed, double low, double high) { 
 double unif_ret; 
 long int m,a,b,c, k; 
 double value_0_1; 

 m = 2147483647; 
 a = 16807; 
 b = 127773; 
 c = 2836; 
 k = *seed/b; 
 *seed = a * (*seed % b) - k*c; 

 if (*seed <0) 
	 *seed = *seed + m; 

 value_0_1 = (double) *seed/m; 
 unif_ret = low+value_0_1*(high - low); 
 return (unif_ret); 
} 

/********************************************************** 
Algoritmo 2 – Gerador de números inteiros aleatórios 
Gerador de distribuicao uniforme retorna um numero inteiro 
na faixa low – high, ou seja, [low,high]. 
**********************************************************/ 

/*int inteiros_unif(seed, low, high) 

long int *seed; int low; int high; */

int inteiros_unif(long int *seed, int low, int high){ 

 int unif_ret; 
 long int m,a,b,c, k; 
 double value_0_1; 
 

 m = 2147483647; 
 a = 16807; 
 b = 127773; 
 c = 2836; 

 k = *seed/b; 
 *seed = a * (*seed % b) - k * c; 

 if (*seed <0) 
	 *seed = *seed + m; 

 value_0_1 = (double) *seed/m; 
 unif_ret = low+value_0_1*(high-low+1); 

 return (unif_ret); 
}
