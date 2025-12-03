import numpy as np
from .graph import Cell
from .utils import trace_path

"""
General graph search instructions:

First, define the correct data type to keep track of your visited cells
and add the start cell to it. If you need to initialize any properties
of the start cell, do that too.

Next, implement the graph search function. When you find a path, use the
trace_path() function to return a path given the goal cell and the graph. You
must have kept track of the parent of each node correctly and have implemented
the graph.get_parent() function for this to work. If you do not find a path,
return an empty list.

To visualize which cells are visited in the navigation webapp, save each
visited cell in the list in the graph class as follows:
     graph.visited_cells.append(Cell(cell_i, cell_j))
where cell_i and cell_j are the cell indices of the visited cell you want to
visualize.
"""


def depth_first_search(graph, start, goal):
    """Depth First Search (DFS) algorithm. This algorithm is optional for P3.
    Args:
        graph: The graph class.
        start: Start cell as a Cell object.
        goal: Goal cell as a Cell object.
    """
    graph.init_graph()  # Make sure all the node values are reset.

    """TODO (P3): Implement DFS (optional)."""

    # If no path was found, return an empty list.
    return []


from collections import deque

def breadth_first_search(graph, start, goal):
    """
    Breadth First Search (BFS) algorithm using Pythonic data structures.

    Args:
        graph: The graph class (must have methods: is_cell_in_bounds, 
               check_collision, cell_to_idx, idx_to_cell, find_neighbors).
        start: Start cell as a Cell object.
        goal: Goal cell as a Cell object.
    """

    graph.init_graph()
    start_idx = graph.cell_to_idx(start.i, start.j)
    goal_idx = graph.cell_to_idx(goal.i, goal.j)

    if (not graph.is_cell_in_bounds(start.i, start.j) or 
        not graph.is_cell_in_bounds(goal.i, goal.j) or
        graph.check_collision(start.i, start.j) or 
        graph.check_collision(goal.i, goal.j)):
        return []

    if start_idx == goal_idx:
        return [start]

    queue = deque([start_idx])
    
    visited = {start_idx}
    
    graph.visited_cells.append(start)

    while queue:
        current_idx = queue.popleft()
        current_cell = graph.idx_to_cell(current_idx)

        for neighbor_idx in graph.find_neighbors(current_cell.i, current_cell.j):
            
            if neighbor_idx in visited:
                continue
            
            neighbor_cell = graph.idx_to_cell(neighbor_idx)
            
            if graph.check_collision(neighbor_cell.i, neighbor_cell.j):
                visited.add(neighbor_idx)
                continue
            
            graph.parents[neighbor_idx] = current_idx
            visited.add(neighbor_idx)
            queue.append(neighbor_idx)
            graph.visited_cells.append(neighbor_cell)

            if neighbor_idx == goal_idx:
                path = []
                walk = goal_idx
                while walk != -1: 
                    path.append(graph.idx_to_cell(walk))
                    walk = graph.parents[walk]
                
                return path[::-1]

    return [] # No path


def a_star_search(graph, start, goal):
    """A* Search (BFS) algorithm.
    Args:
        graph: The graph class.
        start: Start cell as a Cell object.
        goal: Goal cell as a Cell object.
    """
    graph.init_graph()  # Make sure all the node values are reset.

    """TODO (P3): Implement A*."""

    # If no path was found, return an empty list.
    return []
