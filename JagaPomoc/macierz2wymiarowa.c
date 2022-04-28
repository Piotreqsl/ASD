
#include <stdio.h>

#include <conio.h>
#include <math.h>

void wczytajMacierz(int x, int y, int A[100][100]){
    

    for(int i =0; i < x; i++){
        for(int j =0; j < y; j++){
            printf("Podaj[%d][%d]: ",i,j);                
            scanf("%d",&A[i][j]);  
        }
    }
}



void main (){
    int x, y, macierz[100][100];  
    printf("Podaj liczbę wierszy:");
    scanf("%d", &x);

    printf("Podaj liczbę kolumn:");
    scanf("%d", &y);

    wczytajMacierz(x,y,macierz);

    //teraz już masz macierz gotową do działania

}    