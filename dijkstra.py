from graph import graph


def dijkstra(start, finish):
    distances = {}
    previous = {}
    unvisited = []

    for point in graph:
        distances[point] = float("inf")
        previous[point] = None
        unvisited.append(point)

    distances[start] = 0

    while unvisited:
        current = min(unvisited, key=lambda point: distances[point])

        if current == finish:
            break

        unvisited.remove(current)

        for neighbor, data in graph[current].items():
            distance = data["distance"]

            new_distance = distances[current] + distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current

    route = []
    current = finish

    while current is not None:
        route.append(current)
        current = previous[current]

    route.reverse()

    total_time = 0

    for i in range(len(route) - 1):
        start_point = route[i]
        end_point = route[i + 1]

        total_time += graph[start_point][end_point]["time"]

    return route, distances[finish], total_time