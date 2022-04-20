from cmath import inf

def bin_search(A, x):
  n = len(A)
  l = 0
  r = n - 1
  while l <= r:
    c = (l+r)//2
    if A[c] < x:
      l = c + 1
    elif A[c] > x:
      r = c - 1
    else:
      while c > 0 and A[c-1] == x:
        c -= 1
      break

  if A[c] != x:
    return None
  return c

def get_path(parents, min_dist, t, min_f_i):
  if min_dist == inf:
    return None

  if parents[t][min_f_i] is None:
    return []

  path = []
  _v = (t, min_f_i)
  while _v is not None:
    v, f = _v
    path.append(v)
    _v = parents[v][f]

  return path[::-1]


def czolg(A,P,bak,target):
    n = len(A)
  
    F=[[inf]* (bak+1) for i in range(target+1)]
    parents = [[None]* (bak+1) for i in range(target+1)]

    F[0][bak] = 0 ##startujemy z pola 0 z pełnym bakiem

    for i in range(1, target+1):
        stacja = bin_search(A,i)
        for prev_i in range(i):
            distance = i - prev_i
            for f in range(bak-distance+1):
                if F[prev_i][f+distance] < F[i][f]:
                    F[i][f] = F[prev_i][f+distance]
                    parents[i][f] = (prev_i,f+distance)
                if stacja is not None:
                    tankowanie = F[prev_i][f+distance] + P[stacja]*(bak-f)
                    if(tankowanie < F[i][bak]):
                        F[i][bak] = tankowanie
                        parents[i][bak] = (prev_i, f+distance)
    min_f_i = 0
    for f in range(bak+1):
        if F[target][f] < F[target][min_f_i]:
            min_f_i = f


    return (F[target][min_f_i], get_path(parents, F[target][min_f_i], target, min_f_i))


    # zakladam, ze stacje sa w posortowanej kolejnosci

S = [1, 2, 3, 4]
P = [0.9, 1, 0.9, 0.5]
L = 2
t = 6
print(czolg(S, P, L,t))