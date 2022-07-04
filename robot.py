

def robot(L, A, B):
    rows = len(L)
    cols = len(L[0])
    n = rows * cols

    G = [[] for i in range(12*n)]

    #[0,1,2,3,4,5,6,7,8,9,10,11,12]
    # 0,1,2 - prawo
    # 3,4,5 - góra
    # 6,7,8 - lewo
    # 9,10,11 - dół

    for i in range(rows):
        for j in range(cols):
            if L[i][j] == "X":
                continue

            for s in [0,1,2,6,7,8]:
                for t in [3,9]:
                    G[(s*n) + (i*cols) + j].append([(t*n) + (i*cols) + j, 45])
            
            for s in [3,4,5,9,10,11]:
                for t in [0,6]:
                    G[(s*n) + (i*cols) + j].append([(t*n) + (i*cols) + j, 45])