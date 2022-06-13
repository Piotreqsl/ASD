## zadanie dwoch kierowców
## wierzchołki to miasta, drogi to krawędzie skierowane
## mamy dwoch kierowc Alicja i Bob
## mają dojechać z A do B


## najkrótsza monotoniczna ścieżka - rozwiązanie od prowadzącego!!!!!
## taki bellman-ford na krawedziach posortowanych malejąco
## distances są na float('inf') zeby relaksacja zaczęła się od



### domknięcie przechodnie


## kantor to pamiętać o logarytmach (przy mnożeniu w ogóle logarytmy są przyjemne)




## stacje benzynowe na grafie
## rozdzielam każdy wierzchołek na d wierzchołków (i,0), (i,1), .... (i,d)

## jak zrobić tankowanie - wszystkie krawędzie (i,0) (i,1) .... (i,d) mają krawędź wagi 1 między sobą
# 
# potem łącze wszystkie i oraz j które miały krawędź z jakąś wagą w oryginalnym grafie np łącze (i,7) z (j,2) jeśli krawędź była z i do j z wagą 5 (w nowym grafie mają wagi 0) 
# wagi 0 ponieważ spalanie się dokonuje poprzez dobre krawędzie

## i najkrótsze ścieżki normalnie dijsktrą np