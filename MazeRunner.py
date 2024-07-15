import pyamaze as maze
import random
import argparse
from SearchSolution import SearchSolution

# Create a maze with fixed parameters
def create_maze(rows, cols):
    m = maze.maze(rows, cols)
    m.CreateMaze(loopPercent=100, theme=maze.COLOR.light, pattern='vertical')
    return m

# Generate a random position within the maze
def get_random_position(rows, cols):
    return random.randint(1, rows), random.randint(1, cols)

# Set up agents with fixed shapes and ensure they are not at the same position
def setup_agents(m, rows, cols):
    start_row, start_col = get_random_position(rows, cols)
    goal_row, goal_col = get_random_position(rows, cols)
    
    while (start_row, start_col) == (goal_row, goal_col):
        goal_row, goal_col = get_random_position(rows, cols)

    start_agent = maze.agent(m, start_row, start_col, shape="arrow", footprints=True)
    goal_agent = maze.agent(m, goal_row, goal_col, shape="square", footprints=True, color=maze.COLOR.red)
    
    return start_agent, goal_agent, (start_row, start_col), (goal_row, goal_col)

# Run the specified search algorithm
def run_search(m, search_method, start_pos, goal_pos):
    solver = SearchSolution(m)
    
    if search_method == 'BFS':
        path = solver.bfs(start_pos, goal_pos)
    elif search_method == 'DFS':
        path = solver.dfs(start_pos, goal_pos)
    elif search_method == 'GS':
        path = solver.greedy(start_pos, goal_pos)
    elif search_method == 'AStar':
        path = solver.astar(start_pos, goal_pos)
    else:
        raise ValueError(f"Unknown search method: {search_method}")
    
    return path, solver.depth, solver.numCreated, solver.numExpanded, solver.maxFringe

# Write the search results to a file
def write_results(size, search_method, depth, num_created, num_expanded, max_fringe):
    with open("Readme.txt", "a") as file:
        file.write(f"{size} {search_method}: {depth}, {num_created}, {num_expanded}, {max_fringe}\n")
        print(f"Written to Readme.txt: {size} {search_method}: {depth}, {num_created}, {num_expanded}, {max_fringe}")

# Main function to parse arguments and execute the program
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Maze Runner with search algorithms")
    parser.add_argument("rows", type=int, help="Total number of Maze rows")
    parser.add_argument("cols", type=int, help="Total number of Maze columns")
    parser.add_argument("searchmethod", type=str, choices=['BFS', 'DFS', 'GS', 'AStar'], help="Search method to use")
    
    args = parser.parse_args()
    
    maze_rows, maze_cols = args.rows, args.cols
    search_method = args.searchmethod
    
    #Create the maze
    m = create_maze(maze_rows, maze_cols)
    
    #Setup agents and their start and goal positions
    start_agent, goal_agent, start_position, goal_position = setup_agents(m, maze_rows, maze_cols)
    
    #Run the selected search algorithm
    path, depth, num_created, num_expanded, max_fringe = run_search(m, search_method, start_position, goal_position)
    
    #Trace the path if found
    if path:
        m.tracePath({start_agent: path}, delay=100)
    
    # Write the results to the file
    size = f"{maze_rows}x{maze_cols}"
    write_results(size, search_method, depth, num_created, num_expanded, max_fringe)
    
    #  Run the maze GUI
    m.run()
