# quick sort tak aby zawsze uzywał co najwyzej logn pamieci na
# stosie systemowym

# scalanie k posortowanych list na kopcu
# wiec wyciagamy min i dopinamy
# lub scalanie każdych dwóch ze sobą, ale parami
# złożoność jesrt nlog k w każdym przypadku
#scalanie parami żeby budować takie równe drzewo scalań


#Prosze przedstawić w jaki sposob zrealizowaćstrukture danych
#insert removeMin removeMax
# dwa kopce, kazdy trzyma infomracje o indexie elementu w drugim kopcu
# usuwanie z kopca ze srodka - zamienić indexy usuwanego z ostatnim i naprawić