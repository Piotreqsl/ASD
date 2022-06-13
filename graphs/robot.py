# Robot porusza się po dwuwymiarowym labiryncie i ma dotrzeć z pocycji A = (x[a], y[a]) na pozycję
# B = (x[b], y[b]). Robot może wykonać następujące ruchy:
#   1) ruch do przodu na kolejne pole,
#   2) obrót o 90 stopni zgodnie z ruchem wskazówek zegara,
#   3) obrót o 90 stopni przeciwnie do ruchów wskazówek zegara.
# Obrót zajmuje robotowi 45 sekund. W trakcie ruchu do przodu robot się rozpędza i pokonanie pierwszego
# pola zajmuje 60 sekund, pokonanie drugiego 40 sekund, a kolejnych po 30 sekund na pole. Wykonanie
# obrotu zatrzymuje robota i następujące po nim ruchy do przodu ponownie go rozpędzają. Proszę
# zaimplementować funkcję:
# def robot(L, A, B):
#     ...
# która oblicza ile minimalnie sekund robot potrzebuje na dotarcie z punktu A do punktu B (lub zwraca
# None jeśli jest to niemożliwe).
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową użytego algorytmu.
# Labirynt. Labirynt reprezentowany jest przez tablicę w wierszy, z których każdy jest napisem
# składającym się z k kolumn. Pusty znak oznacza pole po którym robot może się poruszać, a znak ’X’
# oznacza ścianę labiryntu. Labirynt zawsze otoczony jest ścianami i nie da się opuścić planszy.
# Pozycja robota. Początkowo robot znajduje się na pozycji A = (x[a], y[a]) i jest obrócony w prawo
# (tj. znajduje się w wierszu y[a] i kolumnie x[a], skierowany w stronę rosnących numerów kolumn).
from robot_tests import runtests
from queue import PriorityQueue

## to działa
def robot(L, A, B):
    DP = [[[[-1] * 3 for _ in range(4)] for _ in range(len(L[0]))] for _ in range(len(L))]
    queue = PriorityQueue()
    queue.put((0, A[0], A[1], 0, 0))
    possible_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    seconds = [60, 40, 30]
    while not queue.empty():
        time, x, y, direction, idx = queue.get()
        if (x, y) == B:
            return time
        if DP[y][x][direction][idx] != -1 or L[y][x] == 'X':
            continue
        DP[y][x][direction][idx] = time
        queue.put((time + 45, x, y, (direction + 1) % 4, 0))
        queue.put((time + 45, x, y, (direction + 3) % 4, 0))
        x += possible_moves[direction][0]
        y += possible_moves[direction][1]
        queue.put((time + seconds[idx], x, y, direction, min(idx + 1, 2)))


runtests(robot)


from queue import PriorityQueue

################################################# Ale można też zrobić zajebisty graf
#### i opierdolić dijkstrą zwykłą (tyle że z warunkiem jak dojeżdżamy)

def dijkstra(G, s, t):
    def relax(u, v, weight):
        if d[v] > d[u] + weight:
            d[v] = d[u] + weight


    n = len(G)
    d = [float("inf")] * n
    enqueued = [True] * n
    Q = PriorityQueue()

    d[s] = 0
    cnt = 0
    Q.put((d[s], s))
    while not Q.empty() and cnt < n:
        u = Q.get()[1]
        if not enqueued[u]:
            continue
        enqueued[u] = False
        cnt += 1
        for v in G[u]:
            if enqueued[v[0]]:
                relax(u, v[0], v[1])
                Q.put((d[v[0]], v[0]))

    return d[t]


def robot( L, A, B ):
    w = len(L)
    k = len(L[0])
    n = w * k
    G = [[] for _ in range(12 * n)]

    for i in range(w):
        for j in range(k):
            if L[i][j] == "X":
                continue

            for s in [0, 1, 2, 6, 7, 8]: ## z orientacji poziomej mogę sie zrobić w pionową w 45 sek
                for t in [3, 9]:                                                 ## s i t trzeba mnożyć razy liczbę wierzchołków, gdyż dla każdego wierzchołka mamy 12 opcji co tam się dzieje
                    G[(s * n) + (i * k) + j].append([(t * n) + (i * k) + j, 45]) ## (i*k) +j to jest pozycja robota
            for s in [3, 4, 5, 9, 10, 11]: ## z orientacji pionowej mogę się zroibć na bazową prędkość poziomą w 45 sekund
                for t in [0, 6]:
                    G[(s * n) + (i * k) + j].append([(t * n) + (i * k) + j, 45])


            if j + 1 < k and L[i][j + 1] != "X": ## 0, 1, 2 to orientacja w prawo (0->1) czas 60 (1->2) czas 40, (2->2) czas 30
                G[(0 * n) + (i * k) + j].append([(1 * n) + (i * k) + (j + 1), 60])
                G[(1 * n) + (i * k) + j].append([(2 * n) + (i * k) + (j + 1), 40])
                G[(2 * n) + (i * k) + j].append([(2 * n) + (i * k) + (j + 1), 30])

            if i + 1 < w and L[i + 1][j] != "X": ## 3,4,5 orientacja w dół
                G[(3 * n) + (i * k) + j].append([(4 * n) + ((i + 1) * k) + j, 60])
                G[(4 * n) + (i * k) + j].append([(5 * n) + ((i + 1) * k) + j, 40])
                G[(5 * n) + (i * k) + j].append([(5 * n) + ((i + 1) * k) + j, 30])

            if j - 1 >= 0 and L[i][j - 1] != "X": ## orientacja poziomo w lewo
                G[(6 * n) + (i * k) + j].append([(7 * n) + (i * k) + (j - 1), 60])
                G[(7 * n) + (i * k) + j].append([(8 * n) + (i * k) + (j - 1), 40])
                G[(8 * n) + (i * k) + j].append([(8 * n) + (i * k) + (j - 1), 30])

            if i - 1 >= 0 and L[i - 1][j] != "X": ## orientacja pionowo w górę
                G[(9 * n) + (i * k) + j].append([(10 * n) + ((i - 1) * k) + j, 60])
                G[(10 * n) + (i * k) + j].append([(11 * n) + ((i - 1) * k) + j, 40])
                G[(11 * n) + (i * k) + j].append([(11 * n) + ((i - 1) * k) + j, 30])

    res = float("inf")
    for t in range(12): ## mnożę a1 razy k ponieważ a1 to numer wiersza, a przy b to se robię jeszcze t*n żeby sprawdzić każdą z 12 opcji dostania się tam
        res = min(res, dijkstra(G, (A[1] * k) + A[0], (t * n) + (B[1] * k) + B[0]))

    if res == float("inf"):
        return None
    return res