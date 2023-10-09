import math
import sys
import heapq
MaxNumberV = 1000
class Map:
    def __init__(self, fname):
        Ni = 0
        Nj = 0
        MD = []
        fin = open(fname, "r")
        while (True):
            line = fin.readline().split()
            line = list(map(int, line))
            if not line:
                break
            MD.append(line)
            Nj = len(line)
            Ni += 1
        self.Ni = Ni
        self.Nj = Nj
        self.MD = MD
    def index(self, x, y):
        return self.MD[x][y]
    def neibhors(self, x, y):
        if x==0:
            if y==0:
                return [[x+1, y],[y+1, x]]
            if y==self.Nj:
                return [[x+1, y],[x, y-1]]
            else:
                return [[x, y-1],[x, y+1],[x+1, y]]
pass

class Cell:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def hManhetten(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)
def hChebiseva(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return max(abs(x1 - x2), abs(y1 - y2))
def hEvklida(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
def hDeikstra(a, b):
    return 0

def astar(map, start, end, h):
    start_node = Cell(None, start)
    start_node.g = 0 #Map1.MD[start[0]][start[1]]
    start_node.h = 0
    start_node.f = start_node.g + start_node.h
    end_node = Cell(None, end)
    open_list = []
    closed_list = []
    open_list.append(start_node)
    while open_list:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        open_list.pop(current_index)
        if current_node == end_node:
            path = []
            total = current_node.g
            current = current_node
            k = (len(closed_list)*100)/(Ni*Nj)
            while current:
                path.append(current.position)
                current = current.parent
                if current == start_node:
                    break
            path.append(start_node.position)
            return path[::-1], total, k
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if node_position[0] > (len(map) - 1) or node_position[0] < 0 or node_position[1] > (len(map[len(map)-1]) -1) or node_position[1] < 0:
                continue
            new_node = Cell(current_node, node_position)
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue
            k = child.position[0]
            l = child.position[1]
            i = current_node.position[0]
            j = current_node.position[1]
            tentative_g = current_node.g + abs(k - i) + abs(l - j) + abs(Map1.MD[k][l] - Map1.MD[i][j])
            if child not in open_list:
                open_list.append(child)
                tentative_is_better = True
            else:
                if tentative_g < child.g:
                    tentative_is_better = True
                else:
                    tentative_is_better = False
            if tentative_is_better == True:
                child.parent = current_node
                child.g = tentative_g
                if h == 1:
                    child.h = hManhetten(child.position, end_node .position)
                if h == 2:
                    child.h = hChebiseva(child.position, end_node.position)
                if h == 3:
                    child.h = hEvklida(child.position, end_node.position)
                if h == 4:
                    child.h = hDeikstra(child.position, end_node.position)
                child.f = child.g + child.h
        if current_node not in closed_list:
            closed_list.append(current_node)

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
    if len(sys.argv)<6:
        print("Ошибка! Нужно указать один из параметров -e, -m, -l, параметр -o, для вывода в файл или параметр -h, для вывода справки ")
        sys.exit(1)
    if "-h" in sys.argv:
        spravka()
        sys.exit(1)
    fname = sys.argv[2]
    parametr = sys.argv[1]
    Map1 = Map(fname)
    Ni = Map1.Ni
    Nj = Map1.Nj
    Vsx = int(sys.argv[sys.argv.index("-n") + 1])
    Vsy = int(sys.argv[sys.argv.index("-n") + 2])
    Vex = int(sys.argv[sys.argv.index("-d") + 1])
    Vey = int(sys.argv[sys.argv.index("-d") + 2])
    Vs = (Vsx, Vsy)
    Ve = (Vex, Vey)
    path, total, k = astar(Map1.MD, Vs, Ve, 1)
    print(path)
    print(f"Length = {total}, % = {k}")
    path, total, k = astar(Map1.MD, Vs, Ve, 2)
    print(path)
    print(f"Length = {total}, % = {k}")
    path, total, k = astar(Map1.MD, Vs, Ve, 3)
    print(path)
    print(f"Length = {total}, % = {k}")
    path, total, k = astar(Map1.MD, Vs, Ve, 4)
    print(path)
    print(f"Length = {total}, % = {k}")
