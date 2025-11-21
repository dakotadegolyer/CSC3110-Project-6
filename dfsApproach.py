from data_types import *

cycles: set[tuple[str]] = set()

def canonical_cycle(cycle):
    '''
    Determine the mininum lexicographic version of the cycle to ensure output uniqueness
    
    Parameters
    ----------
    cycle: list[str]
        the cycle to generate the minimum lexicographic version of
    '''
    
    t = tuple(cycle)
    rotations = [t[i:] + t[:i] for i in range(len(t))]
    return min(rotations)   


def checkCycles():
    '''
    removes duplicate cycles in the output array
    '''
    
    output:set[list[str]] = set()
    
    for cycle in cycles:
        cycle = canonical_cycle(cycle)
        if cycle not in output:
            output.add(cycle)
            
    return output
            

def dfsHelper(node: ListNode, adjList: AdjacencyList, visited:list[str], locations:dict[str, int]) -> None:
    '''
    A helper for the dfs function, this is responsible for recursively finding the cycles
    
    Parameters
    ----------
    node: ListNode
        the node to perform dfs on 
    adjList: AdjacencyList
        the entire adjacancy list object
    visited: list[str]
        the list of visited nodes in the dfs
    locations: dict[str, int]
        a dictionary where the keys are the visited nodes and the values are the nodes index in visited. 
        This is used for a constant look up time of where the cycle begins in the visited array

    '''
    
    while node is not None:
        
        value = node.val
        if value not in set(visited):
            visited.append(value)
            locations[value] = len(visited) - 1
            dfsHelper(adjList[value].head, adjList, visited, locations)
            visited.pop()
            locations.pop(value)
            
        else:
            valIdx = locations[value]
            cycle = visited[valIdx:]
            cycles.add(tuple(cycle))
        
        node = node.next

def dfsApproach(adjList: AdjacencyList):
    '''
    The main function for the dfs approach. 
    Performs dfs for each of the keys in the adjacency list
    
    Parameters
    ----------
    adjList: AdjacencyList
        The entire adjacency list object
    '''
    
    for key in adjList.lst.keys():
        list = adjList.lst[key]
        visited = [] # track visited nodes in current iteration
        locations = {}
        visited.append(key)
        locations[key] = 0
        dfsHelper(list.head, adjList, visited, locations)
    
    print(checkCycles())