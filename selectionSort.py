def selectionSort(tab):
    for i in range(len(tab) -1):
        minel = tab[i]
        minindex = i
        for j in range(i, len(tab)):
            if(tab[j] < minel):
                minel = tab[j]
                minindex = j

        tab[i], tab[minindex] = tab[minindex], tab[i]
            