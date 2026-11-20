from itertools import permutations


def travelling_salesman(graph):
    if not graph:
        return None, float("inf")

    best_route = None
    best_cost = float("inf")

    # Fix city 0 as the start and try every order of the other cities.
    for order in permutations(range(1, len(graph))):
        route = (0, *order, 0)
        cost = sum(graph[start][end] for start, end in zip(route, route[1:]))
        if cost < best_cost:
            best_route = route
            best_cost = cost

    return best_route, best_cost


if __name__ == "__main__":
    # Use float("inf") for a missing connection.
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    route, cost = travelling_salesman(graph)
    if route is None:
        print("No tour exists.")
    else:
        print("Minimum Cost Tour:", " -> ".join(map(str, route)))
        print("Minimum Cost:", cost)
