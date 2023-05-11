def read_input_file(filename):
    with open(filename) as f:
        distances = [list(map(int, line.split())) for line in f]
    return distances

def compute_tsp(distances):
    n = len(distances)
    visited = [False] * n
    tour = [0] * n
    visited[0] = True
    tour[0] = 0
    for i in range(1, n):
        nearest = None
        for j in range(n):
            if not visited[j] and (nearest is None or distances[tour[i-1]][j] < distances[tour[i-1]][nearest]):
                nearest = j
        tour[i] = nearest
        visited[nearest] = True
    cost = 0
    for i in range(n):
        cost += distances[tour[i]][tour[(i+1)%n]]
    return tour, cost

def print_tsp_solution(tour, cost):
    for vertex in tour:
        print(vertex)
    print(cost)

if __name__ == "__main__":
    filename = input()
    distances = read_input_file(filename)
    tour, cost = compute_tsp(distances)
    print_tsp_solution(tour, cost)
