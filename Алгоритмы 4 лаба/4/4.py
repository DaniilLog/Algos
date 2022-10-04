import random


def PolyHash(P, l, p, x):
    res = 0
    for i in reversed(range(l)):
        res = (res * x + ord(P[i])) % p
    return res % p


def PrecomputeHashes(T, l, k, p, x):
    H = [0] * (l - k + 1)
    S = T[l - k: l]
    H[l - k] = PolyHash(S, k, p, x)
    y = 1
    for i in range(1, k + 1):
        y = (y * x) % p
    for i in range(l - k - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + k]) + p) % p
    return H


with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        s = fin.readline().strip()
        len_s = len(s)
        q = int(fin.readline())
        p = 10 ** 9 + 7
        x = random.randint(1, p - 1)
        for i in range(q):
            a, b, l = map(int, fin.readline().split())
            H = PrecomputeHashes(s, len_s, l, p, x)
            if H[a] == H[b]:
                fout.write('Yes\n')
            else:
                fout.write('No\n')
