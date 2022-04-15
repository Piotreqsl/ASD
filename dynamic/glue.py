"""Dany jest ciag przedziałów postaci [ai, bi]. Dwa przedziały mozna
skleic jesli maja dokładnie jeden punkt wspólny. Prosze wskazac algorytmy dla nastepujacych problemów:
Problem stwierdzenia, czy da sie uzyskac przedział [a, b] przez sklejanie odcinków."""

# f(i, j) = True  ; da się uzyskać przedział od i do j
#         = False ; nie da się uzyskać przedziału od i do j

# f(i, j) = sum(f(i, k) && f(k, j)) ; i < k < j

