from collections import defaultdict

def topsortutil(g, v, vis, st):
    vis[v] = True
    for i in g[v]:
        if vis[i] == False:
            topsortutil(g, i, vis, st)
    st.insert(0, v)

def topsort(g, v):
    vis = [False] * (v + 1)
    st = []
    for i in range(v + 1):
        if vis[i] == False:
            topsortutil(g, i, vis, st)
    o.write(str(st[:len(st) - 1]))

f = open("input.txt", "r")
o = open("output.txt", "w")
n, m = map(int, f.readline().split())
g = defaultdict(list)
for i in range(m):
    q = list(map(int, f.readline().split()))
    g[q[0]].append(q[1])
topsort(g, n)