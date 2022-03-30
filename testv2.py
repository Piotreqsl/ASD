# 2 pkt

def times(T):
    details = [[0, 0, T[i]] for i in range(len(T))]
    values = [0]*10

    for i in range(len(T)):
        copy = T[i]
        while copy > 0:
            values[copy % 10] += 1
            copy //= 10
        for j in range(10):
            if values[j] == 1:
                details[i][0] += 1
            elif values[j] > 1:
                details[i][1] += 1
            values[j] = 0

    return details


def countsort(T, mode):
    occurences = [0] * 10
    result = [0] * len(T)

    if mode == 0:
        for i in range(len(T)):
            occurences[T[i][0]] += 1

        for i in range(8, -1, -1):
            occurences[i] += occurences[i + 1]

        for i in range(len(T) -1, -1, -1):
            occurences[T[i][0]] -= 1
            result[occurences[T[i][0]]] = T[i]

    elif mode == 1:
        for i in range(len(T)):
            occurences[T[i][1]] += 1

        for i in range(1, 10):
            occurences[i] += occurences[i - 1]

        for i in range(len(T) -1, -1, -1):
            occurences[T[i][1]] -= 1
            result[occurences[T[i][1]]] = T[i]

    for i in range(len(T)):
        T[i] = result[i]


def pretty_sort(T):
    extended = times(T)
    countsort(extended, 1)
    countsort(extended, 0)
    print(extended)
    for i in range(len(T)):
        T[i] = extended[i][2]



T=[11,567788,2344,557]

pretty_sort(T)
print(T)