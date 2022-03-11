def insertionSort(tab):

    for i in range(1, len(tab)):
        selected = tab[i]

        y = i -1
        while(y >= 0 and selected < tab[y]):
            tab[y + 1] = tab[y]
            y -= 1
        tab[y+1] = selected
        