from data_types import AdjacencyList
from dfsApproach import canonical_cycle

def FindCycles(AdjList: AdjacencyList):
	cycles = set()
	for v in AdjList.lst.keys():		# Try each vertex as a root
		root = v
		path = [v]
		visited_set = {v}
		DFS(root, path, visited_set, cycles, AdjList)	
	return Deduplicate(cycles)
	
def DFS(root, path, visited_set, cycles, AdjList: AdjacencyList):
	currVertex = path[-1]                                       
	currNeighborNode = AdjList[currVertex].head             # Explore neighbors of most recent vertex in path
	while currNeighborNode != None:
		currNeighborVertex = currNeighborNode.val
		if currNeighborVertex == root and len(path) > 1:    # If cycle is found
			cycles.add(tuple(path))
		
		elif currNeighborVertex not in visited_set:         # If unexplored neighbor vertex is found
			path.append(currNeighborVertex)
			visited_set.add(currNeighborVertex)
			DFS(root, path, visited_set, cycles, AdjList)   # Explore neighbor vertex
			path.pop()
			visited_set.remove(currNeighborVertex)		    # Backtrack when done exploring neighbor vertex
		currNeighborNode = currNeighborNode.next
		
def Deduplicate(cycles):
	uniqueCycles = set()
	for cycle in cycles:
		uniqueCycles.add(canonical_cycle(cycle))
	return uniqueCycles