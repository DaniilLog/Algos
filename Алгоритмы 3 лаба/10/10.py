class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist, root):
        with open('output.txt', 'w') as f:
            for i in range(self.V):
                if dist[i] != float("inf"):
                    if i == root:
                        f.write('0\n')
                    elif dist[i] == 0:
                        f.write('-\n')
                    else:
                        f.write(f'{dist[i]}\n')
                else:
                    f.write('*\n')

    def BellmanFord(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0

        for i in range(self.V - 1):

            for u, v, w in self.graph:
                if dist[u - 1] != float("inf") and dist[u - 1] + w < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + w

        for u, v, w in self.graph:
            if dist[u - 1] != float("inf") and dist[u - 1] + w < dist[v - 1]:
                dist[u - 1] = 0
                dist[v - 1] = 0

        self.printArr(dist, src)


def main():
    with open("input.txt") as f:
        s = f.readlines()
        n, m = map(int, s[0].split())
        g = Graph(n)
        root = int(s[-1]) - 1
        for i in range(1, m + 1):
            u, v, w = map(int, s[i].split())
            g.addEdge(u, v, w)

        g.BellmanFord(root)


if __name__ == "__main__":
    main()
