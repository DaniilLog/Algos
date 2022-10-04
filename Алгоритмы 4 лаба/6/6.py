def zFunction(word):
    z = []
    n = len(word)
    for i in range(n):
        z.append([])
    l, r = 0, 0
    for i in range(1,n):
        if i >= r:
            j = 0
            while i + j < n and word[i + j] == word[j]:
                j += 1
            l = i
            r = i + j
            z[i] = j
        else:
            if z[i - l] < r - i:
                z[i] = z[i - l]
            else:
                j = r - i
                while i + j < n and word[i + j] == word[j]:
                    j += 1
                l = i
                r = i + j
                z[i] = j
    return z

with open("input.txt") as f:
    word = f.readline()
z = zFunction(word)
with open("output.txt","w") as f:
    f.write(" ".join(list(map(str,z[1:]))))