from Search_Algorithms import BFS, DFS, Greedy, AStar_search, DFS_unlimited, DFS_iterative
from time import time

def readInput():
    file = open("puzzle.txt", "r")
    n = int(file.readline())
    root = []
    for i in range(0,n*n):
        line = list(map(int, file.readline().split()))
        for number in line:
            root.append(number)
    return root, n

class solvers:
    def __init__(self, root = None, n = None):
        self.root = root
        self.n = n

    #count the number of inversions       
    def inv_num(self, puzzle):
        inv = 0
        for i in range(len(puzzle)-1):
            for j in range(i+1 , len(puzzle)):
                if (( puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                    inv += 1
        return inv

    def solvable(self, puzzle): #check if initial state puzzle is solvable: number of inversions should be even.
        inv_counter = self.inv_num(puzzle)
        if (inv_counter %2 ==0):
            return True
        return False

    def BFS_solution(self):
        time_ = time()
        BFS_solution = BFS(self.root, self.n)
        BFS_time = time() - time_
        return {'BFS Solution': BFS_solution[0], 'Number of explored nodes': BFS_solution[1], 'BFS time': BFS_time}


    def DFS_solution(self):
        time_ = time()
        DFS_solution = DFS(self.root, self.n)
        DFS_time = time() - time_
        return {'DFS Solution': DFS_solution[0], 'Number of explored nodes': DFS_solution[1], 'DFS time': DFS_time}

    def Greedy_solution(self, heuristic = 1):
        time_ = time()
        Greedy_solution = Greedy(self.root, self.n, heuristic)
        Greedy_time = time() - time_
        return {'Greedy Solution': Greedy_solution[0], 'Number of explored nodes': Greedy_solution[1], 'Greedy time': Greedy_time}
        
    def AStar_solution(self, heuristic = 1):
        time_ = time()
        AStar_solution = AStar_search(self.root, self.n, heuristic)
        AStar_time = time() - time_
        return {'A* Solution': AStar_solution[0], 'Number of explored nodes': AStar_solution[1], 'A* time': AStar_time}
        
    def DFS_unlimited_solution(self):
        time_ = time()
        DFS_unlimited_solution = DFS_unlimited(self.root, self.n)
        DFS_unlimited_time = time() - time_
        return {'DFS Unlimited Solution': DFS_unlimited_solution[0], 'Number of explored nodes': DFS_unlimited_solution[1], 'DFS Unlimited time': DFS_unlimited_time}

    def DFS_iterative_solution(self):
        time_ = time()
        DFS_iterative_solution = DFS_iterative(self.root, self.n)
        DFS_iterative_time = time() - time_
        return {'DFS Iterative Solution': DFS_iterative_solution[0], 'Number of explored nodes': DFS_iterative_solution[1], 'DFS Iterative time': DFS_iterative_time}

    def execute(self, algorithm = 1, heuristic = 1):
        if not self.solvable(self.root):
            raise Exception("The given state is not solvable.")

        print("Solvable, please wait. \n")

        if algorithm == 1:
            return self.BFS_solution()
        elif algorithm == 2:
            return self.DFS_solution()
        elif algorithm == 3:
            return self.Greedy_solution(heuristic)
        elif algorithm == 4:
            return self.AStar_solution(heuristic)
        elif algorithm == 5:
            return self.DFS_unlimited_solution()
        elif algorithm == 6:
            return self.DFS_iterative_solution()
    


if __name__ == "__main__":
    print("Menu:")
    print("1. Breadth-first Search")
    print("2. Depth-first Search")
    print("3. Greedy Search")
    print("4. A* Search")
    print("5. Depth-first Search with unlimited depth")
    print("6. Depth-first Search with Iterative Deepening and adjustable starting depth")
    print("7. Exit")
    algoritm = int(input("Choose an algorithm: "))

    print("\n")
    heuristic = 1

    if algoritm == 7:
        print("Exiting...")

    root, n = readInput()
    print("The given state is:", root, "\n")

    solvers = solvers(root, n)
    
    try:

        if algoritm == 3 or algoritm == 4:
            heuristic = int(input("Choose heuristic function: \n1. Manhattan Distance\n2. Misplaced Tiles: "))
        solution = solvers.execute(algorithm = algoritm, heuristic = heuristic)
        for key, value in solution.items():
            print(key, ":", value)

    except Exception as e:
        print("\n")
        print(e)
        print("Please check the input file and try again.")
        print("Exiting...")