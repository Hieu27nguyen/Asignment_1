from pyamaze import maze, agent, COLOR
from SearchSolution import SearchSolution
import sys
import random

def create_maze_and_agent(rows, cols):
    """
    Create a maze of given size with loops and light theme.
    Returns the maze, the agent, and the start and goal positions.
    """
    # Create a maze of size rows x cols
    m = maze(rows, cols)
    m.CreateMaze(loopPercent=100, theme=COLOR.light)  # Setting theme and loop percent
    
    # Generate random positions for the agent and the goal state
    agent_row, agent_col = random.randint(1, rows), random.randint(1, cols)
    goal_row, goal_col = random.randint(1, rows), random.randint(1, cols)
    
    # Ensure the agent and goal are not in the same position
    while agent_row == goal_row and agent_col == goal_col:
        goal_row, goal_col = random.randint(1, rows), random.randint(1, cols)
    
    # Place the agent in the maze
    a = agent(m, agent_row, agent_col, shape='arrow', footprints=True)
    
    # Print positions for debugging purposes
    print(f"Agent starts at: ({agent_row}, {agent_col})")
    print(f"Goal state at: ({goal_row}, {goal_col})")
    
    return m, a, (agent_row, agent_col), (goal_row, goal_col)

def main():
    # Step 1: Parse command line arguments
    if len(sys.argv) != 4:
        print("Usage: MazeRunner.py [M] [N] [searchmethod]")
        return
    
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    search_method = sys.argv[3]

    # Step 2: Create the maze and agent
    m, a, start, goal = create_maze_and_agent(rows, cols)
    
    # Step 3: Initialize the search solution with the maze, start, and goal positions
    search = SearchSolution(m, start, goal)

    # Step 4: Select and run the search method
    path = None
    if search_method == "BFS":
        path = search.bfs()
    elif search_method == "DFS":
        path = search.dfs()
    elif search_method == "GS":
        path = search.greedy_search()
    elif search_method == "AStar":
        path = search.a_star()
    else:
        print("Invalid search method. Choose from BFS, DFS, GS, AStar.")
        return
    
    # Step 5: Trace the path if found
    if path:
        m.tracePath({a: path})
    else:
        print("No path found.")
    
    # Run the maze visualization
    m.run()

if __name__ == "__main__":
    main()
