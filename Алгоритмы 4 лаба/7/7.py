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
        while True:
            s = fin.readline()
            if not s:
                exit()
            w1, w2 = map(str, s.split())
            len_w1, len_w2 = len(w1), len(w2)
            k = min(len_w1, len_w2)
            p = 10 ** 9 + 7
            x = random.randint(1, p - 1)
            ok = False
            for i in reversed(range(1, k + 1)):
                hash_w1 = PrecomputeHashes(w1, len_w1, i, p, x)
                hash_w2 = PrecomputeHashes(w2, len_w2, i, p, x)
                for j in range(len(hash_w1)):
                    for h in range(len(hash_w2)):
                        if hash_w1[j] == hash_w2[h]:
                            fout.write((str(j) + ' ' + str(h) + ' ' + str(i) + '\n'))
                            ok = True
                            break
                    if ok:
                        break
                if ok:
                    break
            if not ok:
                fout.write((str(0) + ' ' + str(1) + ' ' + str(0) + '\n'))