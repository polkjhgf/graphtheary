MaxNumberV = 1000
import sys
import heapq as queueW
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
    print("Автор работы: Тихомиров П.А. ")
    print("Список ключей, доступных для ввода: ")
    print("    -e - ключ для ввода графа из файла, содержащего список ребер ")
    print("    -m - ключ для ввода графа из файла, содержащего матрицу смежности")
    print("    -l - ключ для ввода графа из файла, содержащего список смежности ")
    print("Важно! Можно указать не более одного ключа для ввода графа!")
    print("    -o - ключ для вывода результатов работы программы в файл")
    print("    -e - ключ для вывода справки")
    print("**********************************************************************")

'''Алгоритм Дейкстры'''
def Deikstra(V0, Vlist):
    visited = set()
    weights = [MaxNumberV] * N
    weights[V0] = 0
    p = [None] * N
    queue = []
    queueW.heappush(queue, (0, V0))
    while queue:
        Vweigth, V = queueW.heappop(queue)
        visited.add(V)
        for U, Uw in Vlist[V]:
            if U not in visited:
                f = Vweigth + Uw
                if f < weights[U]:
                    weights[U] = f
                    p[U] = V
                    queueW.heappush(queue, (f, U))
    return weights

'''Алгоритм Белмана-Форда'''
def BelmanFordMura(V0, Vlist):
    weights = [MaxNumberV] * len(Vlist)
    weights[V0] = 0
    for _ in range(len(Vlist) - 1):
        for j in range(len(Vlist)):
            for U, Uw in Vlist[j]:
                if weights[j] + Uw < weights[U]:
                    weights[U] = weights[j] + Uw
    for j in range(len(Vlist)):
        for U, Uw in Vlist[j]:
            if weights[j] != MaxNumberV and weights[j] + Uw < weights[U]:
                return None
    return weights
"""Алгорим Джонсона"""
def Djonson(Vlist):
    m=[]
    for i in range(N):
        l = []
        l.append(i)
        l.append(0)
        m.append(l)
    Vlist.append(m)
    q = len(Vlist)-1
    h = BelmanFordMura(q, Vlist)
    if h == None:
        return None
    Vlist2=[]
    for U in range(len(Vlist)-1):
        m=[]
        for V, W in Vlist[U]:
            W2 = W + h[U] - h[V]
            l=[]
            l.append(V)
            l.append(W2)
            m.append(l)
        Vlist2.append(m)
    distance = []
    for i in range(N):
        d = Deikstra(i, Vlist2)
        distance.append(d)
    for U in range(len(distance)):
        for V, W in Vlist2[U]:
            distance[U][V] = distance[U][V] + h[V] - h[U]
    return distance

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
    Vlist = []
    for i in range(N):
        m = []
        for j in range(N):
            if Graph1.MD[i][j] != 0:
                l = []
                l.append(j)
                l.append(Graph1.MD[i][j])
                m.append(l)
        Vlist.append(m)

    D = Djonson(Vlist)
    if D == None:
        if "-o" in sys.argv:
            fout = open('res.txt', 'w')
            fout.write("Graph contains negative weight cycle")
        else:
            print("Graph contains negative weight cycle")
    else:
        if "-o" in sys.argv:
            fout = open('res.txt', 'w')
            if Graph1.negative_edges()==True:
                fout.write("Graph contains edges with negative weight.\n")
            else:
                fout.write("Graph doesn't contain edges with negative weight.\n")
            fout.write("Shortest paths lengths:\n")
            for i in range(len(D)):
                for j in range(len(D[i])):
                    if i != j and D[i][j] != MaxNumberV:
                        fout.write(f"{i+1} - {j+1}: {D[i][j]}\n")
        else:
            if Graph1.negative_edges()==True:
                print("Graph contains edges with negative weight.")
            else:
                print("Graph doesn't contain edges with negative weight.")
            print("Shortest paths lengths:")
            for i in range(len(D)):
                for j in range(len(D[i])):
                    if i != j and D[i][j] != MaxNumberV:
                        print(f"{i+1} - {j+1}: {D[i][j]}")
