
#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <math.h>

///METAGRAMY
void wczytajSlowo(char str[100]){
    printf("Podaj słowo: ");
    scanf("%s",str);
}
   

int main(){
    char slowo1[100], slowo2[100];
    wczytajSlowo(slowo1);
    wczytajSlowo(slowo2);


    ///Sprawdzzam czy długość słów jest taka sama
    if(strlen(slowo1) != strlen(slowo2)){
        printf("Nie są metagramami!");
        return 0;
    }
    int i; //zmienna do pętli
    int roznice_licznik = 0;
    for (i=0; i < strlen(slowo1); i++){
        if(slowo1[i] != slowo2[i]){ // jeśli na itej pozycji się różnią
            roznice_licznik++;
        }
    }

    if(roznice_licznik == 1){ // tylko jedna litera sie rózni
        printf("Są metagramami");
        return 0;
    }
    else{
        printf("Nie są metagramami!");
        return 0;
    }



}


