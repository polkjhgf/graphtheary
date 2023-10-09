import sys
MaxNumberV = 1000
class Graph:
    def __init__(self, fname, par):
        NumV=0
        MD=[]
        if par=="-e":
            fin = open(fname, "r")
            Elist=[]
            while True:
                line = fin.readline()
                line=list(map(int, line.split( )))
                if not line:
                    break
                if (len(line)==2):
                    line.append(1)
                Elist.append(line)
                if line[0]>NumV or line[1]>NumV:
                    NumV=max(line[0], line[1])
            MD=[0]*NumV
            for i in range(NumV):
                MD[i]=[0]*NumV
            for k in range(len(Elist)):
                MD[(Elist[k][0])-1][(Elist[k][1])-1]=Elist[k][2];
            
        if par=="-m":
            fin = open(fname, "r")
            while(True):
                line = fin.readline().split( )
                line=list(map(int, line))
                if not line:
                    break
                MD.append(line)
                NumV+=1
                
        if par=="-l":
            fin = open(fname, "r")
            Alist=[]
            while(True):
                line = fin.readline().split( )
                if not line:
                    break
                
                if line==['-']:
                    line=[]
                else:
                    line=list(map(int, line))

                Alist.append(line)
                NumV+=1
            
            MD=[0]*NumV 
            for i in range(NumV):
                MD[i]=[0]*NumV
            for i in range(NumV):
                for j in range(len(Alist[i])):
                    MD[i][Alist[i][j]-1]=1
                
        self.NumV=NumV
        self.MD=MD
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
"""BFS O(|v|+|e|)"""
def BFS(Vlist, V0list):
    KS=[]
    visited = set()
    for V0 in V0list:
        if V0 in visited:
            continue
        queue = []
        currKS=[]
        visited.add(V0)
        queue.append(V0)
        while queue: 
            V = queue.pop(0)
            currKS.append(V+1)
            for Vertex in Vlist[V]: 
                if Vertex not in visited:  
                    visited.add(Vertex)
                    queue.append(Vertex)
        currKS.sort()
        KS.append(currKS)
    return KS

"""DFS O(|v|+|e|)"""
def DFS(Vlist, V0list):
    visited=set()
    KS=[]
    K=0
    M=[0]*len(V0list)
    for V0 in V0list:
        if V0 not in visited:
            currKS=[]
            stack=[]
            stack.append(V0)
            visited.add(V0)
            currKS.append(V0+1)
            K+=1
            M[V0]=K
            while stack:
                V=stack.pop()
                K+=1
                M[V]=K
                for Vertex in Vlist[V]:
                    if Vertex not in visited:
                        stack.append(V)
                        visited.add(Vertex)
                        currKS.append(Vertex+1)
                        stack.append(Vertex)
                        break
            currKS.sort()
            KS.append(currKS)
    return KS, M
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

if __name__ == "__main__":
    if len(sys.argv)>5 or len(sys.argv)==1:
        print("Ошибка! Нужно указать один из параметров -e, -m, -l, параметр -o, для вывода в файл или параметр -h, для вывода справки ")
        sys.exit(1)
    if "-h" in sys.argv:
        spravka()
        sys.exit(1)
    fname=sys.argv[2]
    parametr=sys.argv[1]

    Graph1=Graph(fname, parametr)
    N=Graph1.NumV
    Vlist=[]
    for i in range(N):
        l=[]
        for j in range(N):
            if Graph1.MD[i][j]!=0:
                l.append(j)
        Vlist.append(l)
    V0 = list(range(0, N))
    V0.reverse()
    if Graph1.is_directed()==False:
        KompSV=BFS(Vlist, V0)
        if "-o" in sys.argv:
            fout = open('res.txt', 'w')
            if len(KompSV) == 1:
                fout.write("Graph is connected\n")
            else:
                fout.write("Graph is not connected\n")
            fout.write("The number of components: ", len(KompSV))
            fout.write(f"{KompSV}")
        else:
            if len(KompSV)==1:
                print("Graph is connected")
            else:
                print("Graph is not connected")
            print("The number of components: ", len(KompSV))
            print(KompSV)
    else:
        MDTR=[0]*N
        MDST=[0]*N
        for i in range(N):
            MDTR[i]=[0]*N
            MDST[i]=[0]*N
        for i in range(N):
            for j in range(N):
                MDTR[i][j]=Graph1.MD[j][i]
                if Graph1.MD[i][j]!=0:
                    MDST[i][j]=1
                    MDST[j][i]=1
        Vlistreverse=[]
        Vlistsoot=[]
        for i in range(N):
            r=[]
            l=[]
            for j in range(N):
                if MDTR[i][j]!=0:
                    r.append(j)
                if MDST[i][j]!=0:
                    l.append(j)
            Vlistreverse.append(r)
            Vlistsoot.append(l)

        """Поиск компонент слабой связности"""
        KompSV=BFS(Vlistsoot, V0)
        if "-o" in sys.argv:
            fout = open('res.txt', 'w')
            if len(KompSV)==1:
                fout.write("Graph is weakly connected\n")
            else:
                fout.write("The number of weakly connected components: ")
                fout.write(f"{len(KompSV)}")
            fout.write("\nConnected components: ")
            fout.write(f"{KompSV}")
        else:
            if len(KompSV)==1:
                print("Graph is weakly connected")
            else:
                print("The number of weakly connected components: ")
                print(f"{len(KompSV)}")
            print("Connected components: ")
            print(f"{KompSV}")

        """Алгоритм Касараджу"""
        KompSV, Metki=DFS(Vlist, V0)
        i=0
        while True:
            W=Metki.index(max(Metki))
            Metki[W]=-1
            V0[i]=W
            i+=1
            if i==N:
                break
        KompSV, Metki=DFS(Vlistreverse, V0)
        if "-o" in sys.argv:
            if len(KompSV)==1:
                fout.write("Graph is strongly connected\n")
            else:
                fout.write("\nThe number of strongly connected components: ")
                fout.write(f"{len(KompSV)}")
            fout.write("\nStrongly connected components: \n")
            fout.write(f"{KompSV}")
        else:
            if len(KompSV)==1:
                print("Graph is strongly connected")
            else:
                print("The number of strongly connected components: ", len(KompSV))
            print("Strongly connected components: ", KompSV)