from data_types import *
from dfsApproach import canonical_cycle

cycles: set[tuple[str]] = set()

def bruteForceAlgo(adj: AdjacencyList):
    permutationHelper(adj, [], [i for i in list(adj.lst.keys())])
    return cycles

# returns true if val is in linked
def searchLinkedList(linked: LinkedList, val: str):
    cur = linked.head
    while cur != None:
        if cur.val == val:
            return True
        cur = cur.next
    return False

# checks if the vertices in the path all connect, and if the last vertex connects to the start
def checkCycle(adj, path):
    if len(path) == 0:
        return False
    
    elif len(path) == 1:
        if searchLinkedList(adj[path[0]], path[0]):
            return True
        else:
            # print(f"{path[0]} does not point to itself ({path[0]} -> {adj[path[0]]})")
            return False

        # checking vertices in path
    for i in range(len(path) - 1):
        curItem = path[i]
        curItemReachable = adj[curItem]
        nextItem = path[i + 1]
        if not searchLinkedList(curItemReachable, nextItem):
            # print(f"{nextItem} is not reachable from {curItem} ({curItemReachable})")
            return False
        
    # checking that last item connects to first item
    lastItem = path[-1]
    lastItemReachable = adj[lastItem]
    firstItem = path[0]
    if (searchLinkedList(lastItemReachable, firstItem)):
        return True
    else:
        # print(f"{firstItem} is not reachable from {lastItem} ({lastItem} -> {lastItemReachable})")
        return False

# calls test() on every path starting with curPath, using some permutation of the vertices in remainingVertices
def permutationHelper(adj: AdjacencyList, curPath: list(str), remainingVertices: set(str)):
    test(adj, curPath)

    for v in remainingVertices:
        newRemaining = set(remainingVertices)
        newRemaining.remove(v)
        newCurPath = [i for i in curPath]
        newCurPath.append(v)
        permutationHelper(adj, newCurPath, newRemaining)

            
# checks if the path is a cycle, adds it to cycles if so
def test(adj, path):
    if checkCycle(adj, path):
        # print(f"Cycle Found: {path}")
        cycles.add(tuple(canonical_cycle(path)))

    else:
        # print(f"Not a cycle: {path}")
        return


def main():
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
    bruteForceAlgo(adjList)
    for i in cycles:
        print(i)
    

if __name__ == "__main__":
    main()