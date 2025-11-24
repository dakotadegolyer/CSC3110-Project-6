from data_types import *
#BFS Topological Sort - Cannot perform regular BFS on directed graph
class BFS_Topological:
    def __init__(self, adjList):
        self.adjList = adjList
        self.vertices = list(adjList.lst.keys())
        self.queue = []
        self.indegree = self.get_indegrees()
        self.indx = 0
        self.cycle = 0
        self.processed = []

    #Node indegrees are the number of edges pointing to that specific node
    def process_indegree(self):
        for key, val in self.indegree.items():
            if val == 0 and key not in self.processed:
                self.queue.append(key)
                self.solve()

    #Gets number of indegrees for each vertex
    def get_indegrees(self):
        indegree = {}
        for i in self.vertices:
            indegree[i] = 0
        for i in self.adjList.lst:
            temp = self.adjList.lst[i].head
            while temp:
                indegree[temp.val] += 1
                temp = temp.next
        return indegree
            


    #Nodes will only get processed if their indegree is 0 
    #Starts at A since there is nothing pointing to A
    def solve(self):
        curr = self.queue.pop(0)
        temp = self.adjList.lst[curr].head
        while temp:
            self.indegree[temp.val] -= 1
            temp = temp.next
        self.processed.append(curr)
        self.indx += 1

    #DFS for finding the vertices in which a cycle occurs
    def find_all_cycles(self):
        cycles = []

        def dfs(start, path, visited, indx):
            temp = self.adjList.lst[self.vertices[indx]].head

            while temp:
                val = temp.val
                #Adding start == first vertex to avoid repeated cycle sets
                if start == self.vertices[0] and val in path:
                    fullCycle = path.copy()
                    uniqueCycle = list(dict.fromkeys(fullCycle))
                    cycles.append(uniqueCycle)
                if val not in visited:
                    visited.add(val)
                    nextIndx = self.vertices.index(val)
                    dfs(start, path + [val], visited, nextIndx)
                temp = temp.next

        for i, vert in enumerate(self.vertices):
            dfs(vert, [vert], set([vert]), i)
        cycles2 = []
        for cycle in cycles:
            cycles2.append(set(cycle))

        #cycles returns a 2d list, cycles2 returns a list containing sets that are unordered
        return cycles2
        
