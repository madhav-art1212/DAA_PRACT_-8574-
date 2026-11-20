INF = float("inf")


def floyd_warshall(graph):
    distance = [row[:] for row in graph]
    n = len(distance)

    # Allow one more intermediate vertex in each pass.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                through_k = distance[i][k] + distance[k][j]
                if through_k < distance[i][j]:
                    distance[i][j] = through_k

    if any(distance[i][i] < 0 for i in range(n)):
        raise ValueError("The graph contains a negative-weight cycle.")

    return distance


if __name__ == "__main__":
    # INF represents a missing edge.
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0],
    ]

    print("All-Pairs Shortest Distances:")
    for row in floyd_warshall(graph):
        print(" ".join("INF" if value == INF else str(value) for value in row))
