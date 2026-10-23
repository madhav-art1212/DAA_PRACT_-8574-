n = 5
edges = [
    (2, 0, 1),
    (3, 1, 2),
    (6, 0, 3),
    (8, 1, 3),
    (5, 1, 4),
    (7, 2, 4),
    (9, 3, 4)
]

edges.sort()
parent = list(range(n))
cost = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

print("Edges in Minimum Spanning Tree:")

for w, u, v in edges:
    a = find(u)
    b = find(v)

    if a != b:
        print(u, "-", v, ":", w)
        parent[a] = b
        cost += w

print("Minimum Cost:", cost)