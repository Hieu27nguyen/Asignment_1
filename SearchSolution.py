from collections import deque  # Import deque for BFS
import heapq  # Import heapq for priority queue operations in Greedy and A* search

class SearchSolution:
    def __init__(self, maze):
        # Initialize the search solution with the maze and initial values for metrics
        self.maze = maze
        self.rows = maze.rows
        self.cols = maze.cols
        self.depth = -1
        self.numCreated = 0
        self.numExpanded = 0
        self.maxFringe = 0

    def reset_metrics(self):
        # Reset all metrics to their initial values before running a search algorithm
        self.depth = -1
        self.numCreated = 0
        self.numExpanded = 0
        self.maxFringe = 0

    def bfs(self, start, goal):
        # Breadth-First Search (BFS) algorithm implementation
        self.reset_metrics()
        queue = deque([(start, [])])  # Queue for BFS
        visited = set()
        self.numCreated += 1

        while queue:
            self.maxFringe = max(self.maxFringe, len(queue))
            current, path = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            self.numExpanded += 1
            path = path + [current]
            if current == goal:
                self.depth = len(path) - 1
                return path
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    queue.append((neighbor, path))
                    self.numCreated += 1
        return None

    def dfs(self, start, goal):
        # Depth-First Search (DFS) algorithm implementation
        self.reset_metrics()
        stack = [(start, [])]  # Stack for DFS
        visited = set()
        self.numCreated += 1

        while stack:
            self.maxFringe = max(self.maxFringe, len(stack))
            current, path = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            self.numExpanded += 1
            path = path + [current]
            if current == goal:
                self.depth = len(path) - 1
                return path
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    stack.append((neighbor, path))
                    self.numCreated += 1
        return None

    def greedy(self, start, goal):
        # Greedy Best-First Search algorithm implementation
        self.reset_metrics()
        
        # Define a heuristic function (Manhattan distance)
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        queue = []
        heapq.heappush(queue, (0, start, []))  # Priority queue for Greedy search
        visited = set()
        self.numCreated += 1

        while queue:
            self.maxFringe = max(self.maxFringe, len(queue))
            cost, current, path = heapq.heappop(queue)
            if current in visited:
                continue
            visited.add(current)
            self.numExpanded += 1
            path = path + [current]
            if current == goal:
                self.depth = len(path) - 1
                return path
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    heapq.heappush(queue, (heuristic(neighbor, goal), neighbor, path))
                    self.numCreated += 1
        return None

    def astar(self, start, goal):
        # A* Search algorithm implementation
        self.reset_metrics()
        
        # Define a heuristic function (Manhattan distance)
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        queue = []
        heapq.heappush(queue, (0, start, []))  # Priority queue for A* search
        visited = set()
        g_costs = {start: 0}  # Cost from start to current node
        self.numCreated += 1

        while queue:
            self.maxFringe = max(self.maxFringe, len(queue))
            f_cost, current, path = heapq.heappop(queue)
            if current in visited:
                continue
            visited.add(current)
            self.numExpanded += 1
            path = path + [current]
            if current == goal:
                self.depth = len(path) - 1
                return path
            for neighbor in self.get_neighbors(current):
                tentative_g_cost = g_costs[current] + 1
                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + heuristic(neighbor, goal)
                    heapq.heappush(queue, (f_cost, neighbor, path))
                    self.numCreated += 1
        return None

    def get_neighbors(self, position):
        # Get valid neighbors of a position considering the maze's walls
        row, col = position
        neighbors = []
        if row > 1 and self.maze.maze_map[row, col]['N']:
            neighbors.append((row - 1, col))
        if row < self.rows and self.maze.maze_map[row, col]['S']:
            neighbors.append((row + 1, col))
        if col > 1 and self.maze.maze_map[row, col]['W']:
            neighbors.append((row, col - 1))
        if col < self.cols and self.maze.maze_map[row, col]['E']:
            neighbors.append((row, col + 1))
        return neighbors