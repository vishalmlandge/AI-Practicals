import heapq

# Define the goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Define the heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = divmod(state[i][j] - 1, 3)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

# Define a function to find the possible moves from the current state
def get_possible_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                if i > 0:
                    new_state = [row[:] for row in state]
                    new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
                    moves.append(new_state)
                if i < 2:
                    new_state = [row[:] for row in state]
                    new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
                    moves.append(new_state)
                if j > 0:
                    new_state = [row[:] for row in state]
                    new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
                    moves.append(new_state)
                if j < 2:
                    new_state = [row[:] for row in state]
                    new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
                    moves.append(new_state)
    return moves

# Define the A* search function
def astar(start_state):
    open_list = [(heuristic(start_state), start_state)]
    heapq.heapify(open_list)
    closed_set = set()
    g_score = {tuple(map(tuple, start_state)): 0}
    while open_list:
        current_state = heapq.heappop(open_list)[1]
        if current_state == goal_state:
            return current_state
        closed_set.add(tuple(map(tuple, current_state)))
        for neighbor_state in get_possible_moves(current_state):
            tentative_g_score = g_score[tuple(map(tuple, current_state))] + 1
            if tuple(map(tuple, neighbor_state)) in closed_set and tentative_g_score >= g_score.get(tuple(map(tuple, neighbor_state)), float('inf')):
                continue
            if tentative_g_score < g_score.get(tuple(map(tuple, neighbor_state)), float('inf')):
                g_score[tuple(map(tuple, neighbor_state))] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor_state)
                heapq.heappush(open_list, (f_score, neighbor_state))

# Define a function to print the path from the start state to the goal state
def print_path(path):
    for state in path:
        print_state(state)
        print()

# Define a function to print a state
def print_state(state):
    for row in state:
        print(' '.join(map(str, row)))
    print()

# Example usage:
start_state = [[1, 2, 3],
               [4, 5, 0],
               [7, 8, 6]]
print("Start State:")
print_state(start_state)
print("\nFinding solution...")
solution = astar(start_state)
print("\nSolution:")
print_path([start_state, solution])
