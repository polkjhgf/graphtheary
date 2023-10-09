MaxNumberV = 1000
import heapq as queueW
import sys
class Graph:
    def __init__(self, fname, par):
        NumV=0
        MD=[]
        if par == "-e":
            fin = open(fname, "r")
            Elist = []
            while True:
                line = fin.readline()
                line = list(map(int, line.split( )))
                if not line:
                    break
                if (len (line) == 2):
                    line.append(1)
                Elist.append(line)
                if line[0] > NumV or line[1] > NumV:
                    NumV=max(line[0], line[1])
            MD = [0]*NumV
            for i in range(NumV):
                MD[i] = [0]*NumV
            for k in range(len(Elist)):
                MD[(Elist[k][0])-1][(Elist[k][1])-1] = Elist[k][2];
            
        if par == "-m":
            fin = open(fname, "r")
            while(True):
                line = fin.readline().split( )
                line=list(map(int, line))
                if not line:
                    break
                MD.append(line)
                NumV += 1

        if par == "-l":
            fin = open(fname, "r")
            Alist=[]
            while(True):
                line = fin.readline().split()
                if not line:
                    break
                if line == ['-']:
                    line = []
                else:
                    line = list(map(int, line))
                Alist.append(line)
                NumV+=1
            MD=[0]*NumV 
            for i in range(NumV):
                MD[i]=[0]*NumV
            for i in range(NumV):
                for j in range(len(Alist[i])):
                    MD[i][Alist[i][j]-1]=1
                
        self.NumV = NumV
        self.MD = MD
    def weight(self, v1, v2):
        return self.MD[v1-1][v2-1]
    def is_edge(self, v1, v2):
        if self.MD[v1-1][v2-1]!=0:
            return True
        else: return False
    def adjacency_matrix(self):
        return self.MD
    def adjacenty_list(self, v):
        return self.MD[v-1]
    def is_directed(self):
        for i in range(self.NumV):
            for j in range(i+1, self.NumV):
                if self.MD[i][j]!=self.MD[j][i]:
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

if __name__ == "__main__":
    if len(sys.argv) == 1 or ("-e" in sys.argv and "-l" in sys.argv) or ("-e" in sys.argv and "-m" in sys.argv) or ("-l" in sys.argv and "-m" in sys.argv):
        print("Ошибка! Нужно указать один из параметров -e, -m, -l, параметр -o, для вывода в файл или параметр -h, для вывода справки ")
        sys.exit(1)
    if "-h" in sys.argv:
        spravka()
        sys.exit(1)
    if "-n" not in sys.argv or "-d" not in sys.argv:
        print("Ошибка! Нужно указать ключи -d и -n для указания начальной и конечной вершины")
        sys.exit(1)
    fname = sys.argv[2]
    parametr = sys.argv[1]
    Graph1 = Graph(fname, parametr)
    N = Graph1.NumV
    Vlist = []
    for i in range(N):
        m=[]
        for j in range(N):
            if Graph1.MD[i][j] != 0:
                l = []
                l.append(j)
                l.append(Graph1.MD[i][j])
                m.append(l)
        Vlist.append(m)

    V0 = int(sys.argv[sys.argv.index("-n")+1]) - 1
    Vend = int(sys.argv[sys.argv.index("-d")+1]) - 1

    '''Алгоритм Дейкстры'''
    def Deikstra(V0, Vend):
        visited = set()
        weights = [MaxNumberV] * N
        weights[V0] = 0
        p = [None] * N
        queue = []
        queueW.heappush(queue, (0, V0))
        while queue:
            Vweigth, V = queueW.heappop(queue)
            visited.add(V)
            for U, Uweigth in Vlist[V]:
                if U not in visited:
                    f = Vweigth + Uweigth
                    if f < weights[U]:
                        weights[U] = f
                        p[U] = V
                        queueW.heappush(queue, (f, U))
        distanse = weights[Vend]
        adjlist = []
        i = Vend
        if distanse == MaxNumberV:
            return 0, 0
        while i != V0:
            l=[]
            l.append(p[i] + 1)
            l.append(i + 1)
            if Graph1.MD[i][p[i]] != 0 and Graph1.MD[i][p[i]] != 1:
                l.append(Graph1.MD[i][p[i]])
            i=p[i]
            adjlist.append(l)
        adjlist.reverse()
        return distanse, adjlist
    distance, adjlist = Deikstra(V0, Vend)
    if "-o" not in sys.argv:
        if distance == 0 and adjlist == 0:
            print(f"There is no path between the vertices {V0+1} and {Vend+1}.")
        else:
            print(f"Shortest path length between {V0+1} and {Vend+1} vertices: {distance}")
            print("Path:")
            print(adjlist)
    else:
        fout = open('res.txt', 'w')
        if distance == 0 and adjlist == 0:
            fout.write(f"There is no path between the vertices {V0+1} and {Vend+1}.")
        else:
            fout.write(f"Shortest path length between {V0+1} and {Vend+1} vertices: {distance}\n")
            fout.write("Path:\n")
            for i in adjlist:
                fout.write(str(i))
                fout.write(" ")