

from queue import PriorityQueue


def tanagram(x,y,t):
    indexes = [PriorityQueue() for i in range(26)]

    for i in range(len(x)):
        indexes[ord(x[i]) - 97].put(i)
    for i in range(len(y)):
        idx = ord(y[i]) - 97
        if(indexes[idx].empty()):
            return False
        received = indexes[idx].get()
        if(abs(i-received) > t):
            return False
    return True


print(tanagram("kotomysz", "tokmysoz", 3))