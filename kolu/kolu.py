from kolutesty import runtests
from collections import deque
def disk_processing(disk_num, G, Prevs, dnm):
    n = len(disk_num)
    Stacks = [deque() for i in range(2)]
    for i in range(n):
        if Prevs[i] == 0:
            Stacks[disk_num[i]].append(i)
    d = dnm
    r = 0
    while Stacks[d]:
        while Stacks[d]:
            p = Stacks[d].pop()
            for x in G[p]:
                Prevs[x] -= 1
                if Prevs[x] == 0:
                    Stacks[disk_num[x]].append(x)
        d = (d + 1) % 2
        r += 1
    for x in Prevs:
        if x != 0:
            r = 0
    return r - 1


def swaps( disk, depends ):
    n = len(disk)
    G = [[] for i in range(n)]
    Prevs = [0 for i in range(n)]
    disk_num = [0 for i in range(n)]
    for i in range(n):
        Prevs[i] = len(depends[i])
        if disk[i] == 'A':
            disk_num[i] = 0
        else:
            disk_num[i] = 1
        for p in depends[i]:
            G[p].append(i)
    r1 = disk_processing(disk_num, G, Prevs[:], 0)
    r2 = disk_processing(disk_num, G, Prevs[:], 1)
    if r1 == -1:
        return r2
    if r2 == -1:
        return r1
    return min(r1, r2)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( swaps, all_tests = True )



