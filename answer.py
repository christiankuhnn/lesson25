import itertools

def read_input_file(filename):
    with open(filename) as f:
        distances = [list(map(int, line.split())) for line in f]
    return distances

def compute_tsp(distances):
    n = len(distances)
    best_tour = None
    best_cost = float("inf")
    for tour in itertools.permutations(range(n)):
        cost = 0
        for i in range(n-1):
            cost += distances[tour[i]][tour[i+1]]
        cost += distances[tour[-1]][tour[0]]
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
    return best_tour, best_cost

def print_tsp_solution(tour, cost):
    for vertex in tour:
        print(vertex)
    print(cost)

if __name__ == "__main__":
    filename = input()
    distances = read_input_file(filename)
    tour, cost = compute_tsp(distances)
    print_tsp_solution(tour, cost)
