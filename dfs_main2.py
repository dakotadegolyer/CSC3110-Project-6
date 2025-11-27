from data_types import AdjacencyList
from dfs_algorithm2 import FindCycles

# Graph represented by adjacency list
adj = AdjacencyList()
adj["A"].insert("B")
adj["A"].insert("C")
adj["A"].insert("E")

adj["B"].insert("C")
adj["B"].insert("D")

adj["C"].insert("E")

adj["D"].insert("A")
adj["D"].insert("C")
adj["D"].insert("E")

adj["E"].insert("C")


print("Cycles:", FindCycles(adj))