from itertools import permutations

def read_input_file(filename):
    with open(filename) as f:
        distances = [list(map(int, line.split())) for line in f]
    return distances

def compute_tsp(distances):
    n = len(distances)
    vertices = set(range(n))
    min_cost = float('inf')
    min_tour = None
    
    # Generate all possible tours
    for tour in permutations(vertices):
        cost = 0
        # Compute the total cost of the current tour
        for i in range(n-1):
            cost += distances[tour[i]][tour[i+1]]
        cost += distances[tour[-1]][tour[0]] # add the cost of returning to the starting vertex
        
        # Update the best tour and cost so far
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
    
    return min_tour, min_cost

def print_tsp_solution(tour, cost):
    for vertex in tour:
        print(vertex)
    print(cost)

if __name__ == "__main__":
    filename = input()
    distances = read_input_file(filename)
    tour, cost = compute_tsp(distances)
    print_tsp_solution(tour, cost)
