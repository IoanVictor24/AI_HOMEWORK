import heapq
from collections import deque

def calculate_max_distance(distances, path):
    max_distance = 0
    for i in range(len(path) - 1):
        current_distance = distances[path[i]][path[i + 1]]
        if current_distance > max_distance:
            max_distance = current_distance
    return_distance = distances[path[-1]][path[0]]
    if return_distance > max_distance:
        max_distance = return_distance
    return max_distance

def heuristic(distances, path, n):
    unvisited = set(range(n)) - set(path)
    min_estimate = float('inf')
    for city in unvisited:
        min_distance = min(distances[city])
        if min_distance < min_estimate:
            min_estimate = min_distance
    return min_estimate

def solve_tsp_bfs(distances):
    n = len(distances)
    q = deque([[0]])
    best_path = []
    min_max_distance = float('inf')

    while q:
        path = q.popleft()

        if len(path) == n:
            current_max_distance = calculate_max_distance(distances, path)
            if current_max_distance < min_max_distance:
                min_max_distance = current_max_distance
                best_path = path
        else:
            for i in range(n):
                if i not in path:
                    new_path = path + [i]
                    q.append(new_path)

    return best_path, min_max_distance

def solve_tsp_uniform_cost(distances):
    n = len(distances)
    pq = []
    heapq.heappush(pq, (0, [0]))

    best_path = []
    min_max_distance = float('inf')

    while pq:
        g_cost, path = heapq.heappop(pq)

        if len(path) == n:
            current_max_distance = calculate_max_distance(distances, path)
            if current_max_distance < min_max_distance:
                min_max_distance = current_max_distance
                best_path = path
        else:
            for i in range(n):
                if i not in path:
                    new_path = path + [i]
                    new_g_cost = g_cost + distances[path[-1]][i]
                    heapq.heappush(pq, (new_g_cost, new_path))

    return best_path, min_max_distance

def solve_tsp_a_star(distances):
    n = len(distances)
    pq = []
    heapq.heappush(pq, (heuristic(distances, [0], n), 0, [0]))

    best_path = []
    min_max_distance = float('inf')

    while pq:
        f_cost, g_cost, path = heapq.heappop(pq)

        if len(path) == n:
            current_max_distance = calculate_max_distance(distances, path)
            if current_max_distance < min_max_distance:
                min_max_distance = current_max_distance
                best_path = path
        else:
            for i in range(n):
                if i not in path:
                    new_path = path + [i]
                    new_g_cost = g_cost + distances[path[-1]][i]
                    new_f_cost = new_g_cost + heuristic(distances, new_path, n)
                    heapq.heappush(pq, (new_f_cost, new_g_cost, new_path))

    return best_path, min_max_distance

def main():
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    best_path_bfs, cost_bfs = solve_tsp_bfs(distances)
    print(f"Traseul optim (BFS): {best_path_bfs + [best_path_bfs[0]]} | Cost: {cost_bfs}")

    best_path_ucs, cost_ucs = solve_tsp_uniform_cost(distances)
    print(f"Traseul optim (Uniform Cost Search): {best_path_ucs + [best_path_ucs[0]]} | Cost: {cost_ucs}")

    best_path_a_star, cost_a_star = solve_tsp_a_star(distances)
    print(f"Traseul optim (A*): {best_path_a_star + [best_path_a_star[0]]} | Cost: {cost_a_star}")

if __name__ == "__main__":
    main()
