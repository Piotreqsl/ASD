
#include <stdio.h>
#include <conio.h>
#include <math.h>
void WczytajCiag(int n, int A[100]){
    int i;
    printf("Podaj liczbę elememtów ciągu:");
    scanf("%d", &n);
    printf("Podaj elementy ciągu:\n");
    for (i=0; i<n; i++){
        printf("A[%d]=",i);
        scanf("%d", &A[i]);
    }
}


int main(){
    int n, A[100];
    WczytajCiag(n, A);

}