#### Z = zadania tabloce
### D - deadliny
### P - zyski



class Task:
    def __init__(self):
        self.profit = 0
        self.deadline = 0


def choose(Z):
    Z.sort(key=lambda x: x.profit)
    Z.sort(key=lambda x: x.deadline,reverse=True)
    ret = []
    ret.append()
    while Z:
        f = Z[0]
        ret.append(f)
        Z.pop(0)
        for e in Z:
            if e.d != f.d:
                break
        e.d -=1
    return ret

