from State import State
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue
# pausar el programa
import time

#Breadth-first Search
def BFS(given_state , n):
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = Queue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        explored.append(current_node.state)
        
        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return

#Depth-first Search with limited depth
def DFS(given_state , n): 
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = LifoQueue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        max_depth = current_node.depth #current depth
        explored.append(current_node.state)
        
        if max_depth == 30:
            continue #go to the next branch

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return (("Couldn't find solution in the limited depth."), len(explored))



#Depth-first Search with unlimited depth
def DFS_unlimited(given_state , n): 
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = LifoQueue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        max_depth = current_node.depth #current depth
        explored.append(current_node.state)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)

    return (("Couldn't find solution in the limited depth."), len(explored))


# Depth-first Search with Iterative Deepening and adjustable starting depth
def DFS_iterative(given_state, n, max_depth_limit=30, initial_depth=5, depth_increment=1):
    depth_limit = initial_depth  # Set initial depth limit
    
    while depth_limit <= max_depth_limit:
        root = State(given_state, None, None, 0, 0)
        if root.test():
            return root.solution()
        
        frontier = LifoQueue()
        frontier.put(root)
        explored = set()
        
        while not frontier.empty():
            current_node = frontier.get()
            
            # Convert the current state to a tuple to make it hashable
            current_state_tuple = tuple(map(tuple, current_node.state)) if isinstance(current_node.state[0], list) else tuple(current_node.state)
            
            if current_state_tuple in explored:
                continue
            explored.add(current_state_tuple)
            
            if current_node.depth >= depth_limit:
                continue  # Skip expanding nodes that reach the current depth limit

            # Check if solution is found
            if current_node.test():
                return current_node.solution(), len(explored)

            # Expand the current node
            children = current_node.expand(n)
            for child in children:
                # Convert the child state to a tuple to make it hashable
                child_state_tuple = tuple(map(tuple, child.state)) if isinstance(child.state[0], list) else tuple(child.state)
                
                if child_state_tuple not in explored:
                    frontier.put(child)
        
        # Increase the depth limit and try again
        depth_limit += depth_increment

    return "Couldn't find solution within the maximum depth limit.", len(explored)
    
def Greedy(given_state , n, heuristic = 1):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    #root.evaluation()
    if heuristic == 1:
        evaluation = root.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
    elif heuristic == 2:
        evaluation = root.Misplaced_Tiles(n)
    else:
        evaluation = root.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.

    frontier.put((evaluation[0], counter, root)) #based on greedy evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                if heuristic == 1:
                    evaluation = child.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
                elif heuristic == 2:
                    evaluation = child.Misplaced_Tiles(n)
                else:
                    evaluation = child.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.

                frontier.put((evaluation[0], counter, child)) #based on greedy evaluation
    return


def AStar_search(given_state , n, heuristic = 1):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    if heuristic == 1:
        evaluation = root.Manhattan_Distance(n)
    elif heuristic == 2:
        evaluation = root.Misplaced_Tiles(n)
    frontier.put((evaluation[1], counter, root)) #based on A* evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                if heuristic == 1:
                    evaluation = child.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
                elif heuristic == 2:
                    evaluation = child.Misplaced_Tiles(n)
                frontier.put((evaluation[1], counter, child)) #based on A* evaluation
    return
