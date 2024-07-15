import heapq
from collections import deque

class SearchSolution:
    def __init__(self, maze, start, goal):
        """
        Initializes the search solution with the given maze, start position, and goal position.
        """
        self.maze = maze
        self.start = start
        self.goal = goal
        self.maze_map = maze.maze_map  # Access the maze structure

    def bfs(self):
        """
        Breadth-First Search (BFS) algorithm to find the shortest path from start to goal.
        Returns the path, depth, number of nodes created, number of nodes expanded, and max fringe size.
        """
        queue = deque([(self.start, [])])
        visited = set()
        numCreated = 1
        numExpanded = 0
        maxFringe = 1

        while queue:
            current, path = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            path = path + [current]
            numExpanded += 1

            if current == self.goal:
                depth = len(path) - 1
                return path, depth, numCreated, numExpanded, maxFringe

            for direction in 'NEWS':
                row, col = current
                if direction == 'N':
                    row -= 1
                elif direction == 'E':
                    col += 1
                elif direction == 'W':
                    col -= 1
                elif direction == 'S':
                    row += 1
                
                if (row, col) in self.maze_map and self.maze_map[(row, col)] == 1:
                    queue.append(((row, col), path))
                    numCreated += 1
                    maxFringe = max(maxFringe, len(queue))
        
        return None, -1, 0, 0, 0

    def dfs(self):
        """
        Depth-First Search (DFS) algorithm to find a path from start to goal.
        Returns the path, depth, number of nodes created, number of nodes expanded, and max fringe size.
        """
        stack = [(self.start, [])]
        visited = set()
        numCreated = 1
        numExpanded = 0
        maxFringe = 1

        while stack:
            current, path = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            path = path + [current]
            numExpanded += 1

            if current == self.goal:
                depth = len(path) - 1
                return path, depth, numCreated, numExpanded, maxFringe

            for direction in 'NEWS':
                row, col = current
                if direction == 'N':
                    row -= 1
                elif direction == 'E':
                    col += 1
                elif direction == 'W':
                    col -= 1
                elif direction == 'S':
                    row += 1
                
                if (row, col) in self.maze_map and self.maze_map[(row, col)] == 1:
                    stack.append(((row, col), path))
                    numCreated += 1
                    maxFringe = max(maxFringe, len(stack))
        
        return None, -1, 0, 0, 0

    def manhattan_distance(self, point1, point2):
        """
        Calculates the Manhattan Distance between two points.
        This is used as a heuristic for the search algorithms.
        """
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def greedy_search(self):
        """
        Greedy Search algorithm using Manhattan Distance as the heuristic to find a path from start to goal.
        Returns the path, depth, number of nodes created, number of nodes expanded, and max fringe size.
        """
        queue = [(self.manhattan_distance(self.start, self.goal), self.start, [])]
        visited = set()
        numCreated = 1
        numExpanded = 0
        maxFringe = 1

        while queue:
            _, current, path = heapq.heappop(queue)
            if current in visited:
                continue
            visited.add(current)
            path = path + [current]
            numExpanded += 1

            if current == self.goal:
                depth = len(path) - 1
                return path, depth, numCreated, numExpanded, maxFringe

            for direction in 'NEWS':
                row, col = current
                if direction == 'N':
                    row -= 1
                elif direction == 'E':
                    col += 1
                elif direction == 'W':
                    col -= 1
                elif direction == 'S':
                    row += 1
                
                if (row, col) in self.maze_map and self.maze_map[(row, col)] == 1:
                    heapq.heappush(queue, (self.manhattan_distance((row, col), self.goal), (row, col), path))
                    numCreated += 1
                    maxFringe = max(maxFringe, len(queue))
        
        return None, -1, 0, 0, 0

    def a_star(self):
        """
        A* Search algorithm using Manhattan Distance as the heuristic to find the shortest path from start to goal.
        Returns the path, depth, number of nodes created, number of nodes expanded, and max fringe size.
        """
        queue = [(self.manhattan_distance(self.start, self.goal), 0, self.start, [])]
        visited = set()
        numCreated = 1
        numExpanded = 0
        maxFringe = 1

        while queue:
            _, cost, current, path = heapq.heappop(queue)
            if current in visited:
                continue
            visited.add(current)
            path = path + [current]
            numExpanded += 1

            if current == self.goal:
                depth = len(path) - 1
                return path, depth, numCreated, numExpanded, maxFringe

            for direction in 'NEWS':
                row, col = current
                if direction == 'N':
                    row -= 1
                elif direction == 'E':
                    col += 1
                elif direction == 'W':
                    col -= 1
                elif direction == 'S':
                    row += 1
                
                if (row, col) in self.maze_map and self.maze_map[(row, col)] == 1:
                    heapq.heappush(queue, (self.manhattan_distance((row, col), self.goal) + cost + 1, cost + 1, (row, col), path))
                    numCreated += 1
                    maxFringe = max(maxFringe, len(queue))
        
        return None, -1, 0, 0, 0
