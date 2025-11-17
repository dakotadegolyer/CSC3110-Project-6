# from DFS_Algo import DFS_Algo
# from BFS_Algo import BFS_Algo
import time as t
from data_types import AdjacencyList

def DFS_Algo(adjList: AdjacencyList): 
    
    t.sleep(2)
    return

def BFS_Algo(adjList: AdjacencyList):
    t.sleep(1)
    return

def time(algo, lst: AdjacencyList) -> float:
    start = t.time()
    algo(lst)
    end = t.time()

    res = end - start
    return res

def testAlgos(adjList: AdjacencyList):
    print("running DFS algorithm...")
    resDFS = time(DFS_Algo, adjList)
    print("DFS algorithm complete, time taken: " + str(resDFS) + "s")
    print("running BFS algorithm...")
    resBFS = time(BFS_Algo, adjList)
    print("BFS algorithm complete, time taken: " + str(resBFS) + "s")

def createTestList():
    
    adjList: AdjacencyList = AdjacencyList()
    adjList["A"].insert("B")
    adjList["A"].insert("C")
    adjList["A"].insert("E")

    adjList["B"].insert("C")
    adjList["B"].insert("D")

    adjList["C"].insert("E")

    adjList["D"].insert("A")
    adjList["D"].insert("C")
    adjList["D"].insert("E")

    adjList["E"].insert("C")

    print(adjList)
    return adjList

if __name__ == "__main__":
    testAlgos(createTestList())