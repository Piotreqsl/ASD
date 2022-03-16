#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>

using namespace std;


struct przedzial {
    int a;
    int b;
    bool worth;
};


void quickSort(przedzial *tab, int left, int right) {
    if (right <= left) return;

    int i = left - 1, j = right + 1,
            pivot = tab[(left + right) / 2].a; //wybieramy punkt odniesienia

    while (true) {
        //szukam elementu wiekszego lub rownego piwot stojacego
        //po prawej stronie wartosci pivot
        while (pivot > tab[++i].a);

        //szukam elementu mniejszego lub rownego pivot stojacego
        //po lewej stronie wartosci pivot
        while (pivot < tab[--j].a);

        //jesli liczniki sie nie minely to zamień elementy ze soba
        //stojace po niewlasciwej stronie elementu pivot
        if (i <= j)
            //funkcja swap zamienia wartosciami tab[i] z tab[j]
            swap(tab[i], tab[j]);
        else
            break;
    }

    if (j > left)
        quickSort(tab, left, j);
    if (i < right)
        quickSort(tab, i, right);
}

int find_interval(przedzial *tab, const int N) {
    quickSort(tab, 0, N - 1);
    int max = 0;
    int max_index = -1;
    for (int i = 0; i < N; i++) {
        if (tab[i].worth) {
            int count = 0;
            for (int j = i + 1; j < N; j++) {
                if (tab[i].b >= tab[j].a) {
                    if (tab[i].b >= tab[j].b) {
                        tab[j].worth = false;
                        count++;
                    }
                } else
                    break;
            }
            if (count > max) {
                max = count;
                max_index = i;
            }
        }
    }
    cout << max << " \n ";
    for (unsigned int i=0;i<5;++i){
        cout << tab[i].a << "-" << tab[i].b <<' ';
    }
     
    return max_index;

}

void zadanie4() {
    //wartości początkowe do testów
    przedzial tab[5];
    tab[0].a = 1;
    tab[1].a = 5;
    tab[2].a = 2;
    tab[3].a = 8;
    tab[4].a = 1;
    tab[0].b = 6;
    tab[1].b = 6;
    tab[2].b = 5;
    tab[3].b = 9;
    tab[4].b = 6;
    tab[0].worth = true;
    tab[1].worth = true;
    tab[2].worth = true;
    tab[3].worth = true;
    tab[4].worth = true;
    int interval = find_interval(tab, 5);
    cout << tab[interval].a << " " << tab[interval].b;
}

int main() {
//    zadanie2();
    zadanie4();
//    zadanie4();
}