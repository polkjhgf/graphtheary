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
                line=list(map(int, line))
                if not line:
                    break
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
#9 4
import sys
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

    SMD=[0]*N
    for i in range(N):
        SMD[i]=[0]*N
    for i in range(N):
        for j in range(N):
            if Graph1.MD[i][j]==1:
                SMD[i][j]=1
                SMD[j][i]=1
    Vlist=[]
    for i in range(N):
        l=[]
        for j in range(N):
            if SMD[i][j]!=0:
                l.append(j)
        Vlist.append(l)

    visited=[]
    time=0
    V0list=list(range(0,N))
    V0=V0list[0]
    tin=[0]*N
    tup=[0]*N
    Vobr=[-1]*N
    cutpoints=set()
    bridges=[]

    def DFS(V0, p):
        global time
        visited.append(V0)
        n=0
        time+=1
        tin[V0]=time
        tup[V0]=time
        for Vertex in Vlist[V0]:
            if Vertex==p:
                continue
            if Vertex not in visited:

                DFS(Vertex, V0)
                n+=1
                tup[V0]=min(tup[V0], tup[Vertex])
                if p!=-1:
                    if tup[Vertex]>=tin[V0]:
                        cutpoints.add(V0+1)
                if tup[Vertex]>tin[V0]:
                    l=[]
                    l.append(V0+1)
                    l.append(Vertex+1)
                    l.sort()
                    bridges.append(l)
            else:
                tup[V0]=min(tup[V0], tin[Vertex])
        if p==-1 and n>=2: #корень и шарнир
            cutpoints.add(V0+1)

    """DFS"""
    for V in V0list:
        if V not in visited:
            DFS(V0, -1)
    print("Bridges: ")
    print(bridges)
    print("Cutpoints: ")
    for V in cutpoints:
        print(V, end=' ')



