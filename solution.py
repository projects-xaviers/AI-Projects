import heapq

def astar(start, goal, grid):
    open_list = [(0, start)]
    closed_set = set()
    came_from = {}

    g_score = {point: float('inf') for row in grid for point in row}
    g_score[start] = 0

    f_score = {point: float('inf') for row in grid for point in row}
    f_score[start] = heuristic(start, goal)

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        closed_set.add(current)

        for neighbor in get_neighbors(current, grid):
            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)

                if neighbor not in closed_set:
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None

def heuristic(point, goal):
    return abs(point[0] - goal[0]) + abs(point[1] - goal[1])

def get_neighbors(point, grid):
    x, y = point
    neighbors = []

    if x > 0 and not grid[x-1][y]:
        neighbors.append((x-1, y))
    if x < len(grid)-1 and not grid[x+1][y]:
        neighbors.append((x+1, y))
    if y > 0 and not grid[x][y-1]:
        neighbors.append((x, y-1))
    if y < len(grid[0])-1 and not grid[x][y+1]:
        neighbors.append((x, y+1))

    return neighbors

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

# Example usage
grid = [[0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]]

start = (0, 0)
goal = (4, 4)

path = astar(start, goal, grid)

if path:
    print("Path found:", path)
else:
    print("No path found")
