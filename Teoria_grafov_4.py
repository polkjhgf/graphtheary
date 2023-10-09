MaxNumberV = 1000000
import sys
import timeit
class Graph:
    def __init__(self, fname, par):
        NumV = 0
        MD = []
        if par == "-e":
            fin = open(fname, "r")
            Elist = []
            while True:
                line = fin.readline()
                line = list(map(int, line.split()))
                if not line:
                    break
                if (len(line) == 2):
                    line.append(1)
                Elist.append(line)
                if line[0] > NumV or line[1] > NumV:
                    NumV = max(line[0], line[1])
            MD = [0] * NumV
            for i in range(NumV):
                MD[i] = [0] * NumV
            for k in range(len(Elist)):
                MD[(Elist[k][0]) - 1][(Elist[k][1]) - 1] = Elist[k][2];

        if par == "-m":
            fin = open(fname, "r")
            while (True):
                line = fin.readline().split()
                line = list(map(int, line))
                if not line:
                    break
                MD.append(line)
                NumV += 1

        if par == "-l":
            fin = open(fname, "r")
            Alist = []
            while (True):
                line = fin.readline().split()
                if not line:
                    break
                if line == ['-']:
                    line = []
                else:
                    line = list(map(int, line))
                Alist.append(line)
                NumV += 1
            MD = [0] * NumV
            for i in range(NumV):
                MD[i] = [0] * NumV
            for i in range(NumV):
                for j in range(len(Alist[i])):
                    MD[i][Alist[i][j] - 1] = 1

        self.NumV = NumV
        self.MD = MD

    def weight(self, v1, v2):
        return self.MD[v1 - 1][v2 - 1]

    def is_edge(self, v1, v2):
        if self.MD[v1 - 1][v2 - 1] != 0:
            return True
        else:
            return False

    def adjacency_matrix(self):
        return self.MD

    def adjacenty_list(self, v):
        return self.MD[v - 1]

    def is_directed(self):
        for i in range(self.NumV):
            for j in range(i + 1, self.NumV):
                if self.MD[i][j] != self.MD[j][i]:
                    return True
        return False
    def negative_edges(self):
        for i in range(self.NumV):
            for j in range(self.NumV):
                if self.MD[i][j] < 0:
                    return True
        return False

pass
def spravka():
    print("**********************************************************************")
    print("Автор работы: Тихомиров П.А.")
    print("Список ключей, доступных для ввода: ")
    print("    -e - ключ для ввода графа из файла, содержащего список ребер ")
    print("    -m - ключ для ввода графа из файла, содержащего матрицу смежности")
    print("    -l - ключ для ввода графа из файла, содержащего список смежности ")
    print("Важно! Можно указать не более одного ключа для ввода графа!")
    print("    -o - ключ для вывода результатов работы программы в файл")
    print("    -e - ключ для вывода справки")
    print("**********************************************************************")

def Kruskala(Vlist):
    visited = set()
    parent = [None] * N
    key = [MaxNumberV] * N
    key[0] = 0
    parent[0] = -1
    for _ in range(N):
        # Находим вершину с минимальным весом, которая еще не посещена
        min_key = MaxNumberV
        min_vertex = None
        for V in range(N):
            if V not in visited and key[V] < min_key:
                min_key = key[V]
                min_vertex = V
        visited.add(min_vertex)
        # Обновляем значения ключей и родительских вершин для смежных вершин
        for V in Vlist[min_vertex]:
            if V[0] not in visited and V[1]<key[V[0]]:
                key[V[0]] = V[1]
                parent[V[0]] = min_vertex

    # Собираем список ребер остовного дерева
    edges = []
    total_weight = 0
    for V in range(1, N):
        edges.append((parent[V]+1, V+1, sootMD[parent[V]][V]))
        total_weight += sootMD[parent[V]][V]
    return edges, total_weight

def Prima(Vlist):
    visited = set()
    i = 0
    visited.add(0)
    total_weight = 0
    edges = []
    while (i < N - 1):
        minimum = MaxNumberV
        a = 0
        b = 0
        for V in range(N):
            if V in visited:
                for U, W in Vlist[V]:
                    if U not in visited:
                        if minimum > W:
                            minimum = W
                            a = V
                            b = U
        edges.append((a+1, b+1, sootMD[a][b]))
        total_weight += sootMD[a][b]
        visited.add(b)
        i += 1
    return edges, total_weight

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
        # If ranks are same, then make one as root and increment
        # its rank by one
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

    # The main function to construct MST using Kruskal's algorithm
def Boruvka(Vlist):
    parent = []
    rank = []
    edges = []
    cheapest = []
    numC = N
    total_weight = 0
    for node in range(N):
        parent.append(node)
        rank.append(0)
        cheapest = [-1] * N
    while numC > 1:
        for u in range(len(Vlist)):
            for v, w in Vlist[u]:
                set1 = find(parent, u)
                set2 = find(parent, v)
                if set1 != set2:
                    if cheapest[set1] == -1 or cheapest[set1][2] > w:
                        cheapest[set1] = [u, v, w]
                    if cheapest[set2] == -1 or cheapest[set2][2] > w:
                        cheapest[set2] = [u, v, w]
        for node in range(N):
            if cheapest[node] != -1:
                u, v, w = cheapest[node]
                set1 = find(parent, u)
                set2 = find(parent, v)
                if set1 != set2:
                    total_weight += w
                    union(parent, rank, set1, set2)
                    print((u+1, v+1, w))
                    edges.append((u+1, v+1, w))
        numC = numC - 1
        cheapest = [-1] * N
    return edges, total_weight

if __name__ == "__main__":
    if len(sys.argv) == 1 or ("-e" in sys.argv and "-l" in sys.argv) or ("-e" in sys.argv and "-m" in sys.argv) or \
            ("-l" in sys.argv and "-m" in sys.argv):
        print("Ошибка! Нужно указать один из параметров -e, -m, -l, параметр -o, для вывода в файл или параметр -h, для вывода справки. ")
        sys.exit(1)
    if ("-d" in sys.argv and "-b" in sys.argv) or ("-d" in sys.argv and "-t" in sys.argv) or \
            ("-b" in sys.argv and "-t" in sys.argv):
        print("Ошибка! Нужно указать один из параметров -d, -b, -t для рассчета. ")
    if "-h" in sys.argv:
        spravka()
        sys.exit(1)
    fname = sys.argv[2]
    parametr = sys.argv[1]
    Graph1 = Graph(fname, parametr)
    N = Graph1.NumV
    sootMD = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if Graph1.MD[i][j]!=0:
                sootMD[i][j] = Graph1.MD[i][j]
                sootMD[j][i] = Graph1.MD[i][j]

    Vlist = []
    for i in range(N):
        m=[]
        for j in range(N):
            if sootMD[i][j] != 0:
                l = []
                l.append(j)
                l.append(sootMD[i][j])
                m.append(l)
        Vlist.append(m)
    if "-k" in sys.argv:
        print(Kruskala(Vlist))
        sys.exit(1)
    if "-p" in sys.argv:
        print(Prima(Vlist))
        sys.exit(1)
    if "-b" in sys.argv:
        print(Boruvka(Vlist))
        sys.exit(1)
    if "-s" in sys.argv:
        st = timeit.default_timer()
        ed, tw = Kruskala(Vlist)
        time = timeit.default_timer() - st
        print(ed, tw)
        print(f"{time:.04f}")
        st = timeit.default_timer()
        ed, tw = Prima(Vlist)
        time = timeit.default_timer() - st
        print(ed, tw)
        print(f"{time:.04f}")
        st = timeit.default_timer()
        ed, tw = Boruvka(Vlist)
        time = timeit.default_timer() - st
        print(ed, tw)
        print(f"{time:.04f}")
