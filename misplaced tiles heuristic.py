
# 8 Puzzle using A* - Misplaced Tiles Heuristic

import heapq

def misplaced_tiles(state, goal):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = (
                new_state[new_zero], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def astar(start, goal):
    pq = []
    heapq.heappush(pq, (0, 0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while pq:
        f, g, current = heapq.heappop(pq)

        if g != g_cost[current]:
            continue

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current

                h = misplaced_tiles(neighbor, goal)
                new_f = new_g + h

                heapq.heappush(
                    pq, (new_f, new_g, neighbor)
                )

    return None


def print_board(state):
    for i in range(0, 9, 3):
        print(*state[i:i+3])


# Initial and goal states
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = astar(start, goal)

if solution:
    print("Solution Found!")
    print("Total Steps:", len(solution) - 1)

    for i, state in enumerate(solution):
        print("\nStep", i)
        print_board(state)
else:
    print("No solution found!")
