# V - wartosci, W - wagi, H - wysokosci
def knapsack3d(V,W,H, max_h, max_w):
    n = len(V)
    F=[[[0 for i in range(max_h +1) ] for j in range(max_w +1) ] for k in range(n)]
    # F[i][w][h] - max profit rozwazajac do i-tego przedmiotu z wykorzystana waga w i wysokoscia h
    for w in range(W[0], max_w+1):
        for h in range(H[0], max_h+1):
            F[0][w][h] = V[0]
    for i in range(1,n):
        for w in range(1, max_w+1):
            for h in range(1, max_h+1):
                F[i][w][h] = F[i-1][w][h] ## nie bierzemy

                if(w >= W[i] and h >= H[i]):
                    F[i][w][h] = max(F[i][w][h], F[i-1][w-W[i]][h-H[i]] + V[i]) # bierzemy (jezeli sie oplaca)
    return F[n-1][max_w][max_h]

# 100
# [2]
V = [10, 10, 14, 6, 12, 20, 5]
W = [15, 7, 8, 4, 1, 2, 5]
H = [15, 3, 6, 5, 15, 19, 2]
max_w = 24; max_h = 30

print(knapsack3d(V,W,H,max_h,max_w))