import heapq
import time

# ============================================
# 1. Map of Mahikeng Local Municipality
# Complete graph with all connections
# ============================================
graph = {
    "Disaneng": ["Mahikeng", "Madibogo"],
    "Mahikeng": ["Disaneng", "Mmabatho", "Slurry", "Bakerville", "Madibogo"],
    "Mmabatho": ["Mahikeng", "Slurry"],
    "Slurry": ["Mahikeng", "Mmabatho", "Zeerust", "Groot Marico", "Bakerville"],
    "Zeerust": ["Slurry", "Groot Marico"],
    "Groot Marico": ["Slurry", "Zeerust"],
    "Bakerville": ["Mahikeng", "Slurry", "Lichtenburg"],
    "Lichtenburg": ["Bakerville", "Coligny"],
    "Coligny": ["Lichtenburg", "Ottosdal"],
    "Ottosdal": ["Coligny", "Sannieshof"],
    "Sannieshof": ["Ottosdal", "Delareyville", "Madibogo"],
    "Delareyville": ["Sannieshof"],
    "Madibogo": ["Disaneng", "Mahikeng", "Sannieshof"]
}

# ============================================
# 2. Distance between areas (km)
# ============================================
weights = {
    ("Disaneng", "Mahikeng"): 25,
    ("Disaneng", "Madibogo"): 35,
    ("Mahikeng", "Mmabatho"): 10,
    ("Mahikeng", "Slurry"): 20,
    ("Mahikeng", "Bakerville"): 35,
    ("Mahikeng", "Madibogo"): 30,
    ("Mmabatho", "Slurry"): 15,
    ("Slurry", "Zeerust"): 35,
    ("Slurry", "Groot Marico"): 40,
    ("Slurry", "Bakerville"): 25,
    ("Zeerust", "Groot Marico"): 20,
    ("Bakerville", "Lichtenburg"): 20,
    ("Lichtenburg", "Coligny"): 30,
    ("Coligny", "Ottosdal"): 35,
    ("Ottosdal", "Sannieshof"): 25,
    ("Sannieshof", "Delareyville"): 30,
    ("Madibogo", "Sannieshof"): 35
}

# ============================================
# 3. Heuristic values to goal (Coligny)
# Taken from the Traffic table in the PDF
# ============================================
heuristic = {
    "Disaneng": 70,
    "Mahikeng": 50,
    "Mmabatho": 55,
    "Slurry": 45,
    "Zeerust": 65,
    "Groot Marico": 75,
    "Bakerville": 30,
    "Lichtenburg": 20,
    "Coligny": 0,
    "Ottosdal": 25,
    "Sannieshof": 40,
    "Delareyville": 55,
    "Madibogo": 60
}

# ============================================
# 4. Function to get undirected edge cost
# ============================================
def get_cost(a, b, weights):
    """Returns the distance between two connected nodes"""
    if (a, b) in weights:
        return weights[(a, b)]
    elif (b, a) in weights:
        return weights[(b, a)]
    else:
        raise ValueError(f"No weight found between '{a}' and '{b}'")

# ============================================
# 5. A* Search Algorithm
# ============================================
def astar(graph, weights, heuristic, start, goal):
    """
    Implements A* Search to find optimal path from start to goal
    Returns: (optimal_path, visited_order, total_cost)
    """
    # Priority queue for open set
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start))
    
    # Track where each node came from
    came_from = {}
    
    # g_score: actual cost from start to node
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0
    
    # f_score: estimated total cost (g_score + heuristic)
    f_score = {node: float("inf") for node in graph}
    f_score[start] = heuristic[start]
    
    # Track order of visited nodes
    visited_order = []
    
    while open_set:
        # Get node with lowest f_score
        _, current = heapq.heappop(open_set)
        
        # Record visit order
        if current not in visited_order:
            visited_order.append(current)
        
        # Goal reached?
        if current == goal:
            # Reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, visited_order, g_score[goal]
        
        # Explore neighbors
        for neighbor in graph[current]:
            cost = get_cost(current, neighbor, weights)
            tentative_g = g_score[current] + cost
            
            # Found better path?
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    # No path found
    return None, visited_order, float("inf")

# ============================================
# 6. Main Execution
# ============================================
if __name__ == "__main__":
    start = "Disaneng"
    goal = "Coligny"
    
    print("=" * 50)
    print("TRUCK LOGISTICS - A* SEARCH ROUTE OPTIMIZATION")
    print("=" * 50)
    print(f"Starting Point: {start}")
    print(f"Destination:    {goal}")
    print("=" * 50)
    
    # Run A* Search
    path, visited_order, total_cost = astar(graph, weights, heuristic, start, goal)
    
    # Display results
    print("\n✅ SEARCH COMPLETE")
    print("-" * 30)
    print(f"Optimal Path:   {' → '.join(path)}")
    print(f"Visited Order:  {visited_order}")
    print(f"Total Distance: {total_cost} km")
    print("-" * 30)
    
    # Simulate truck journey
    print("\n🚛 Truck Journey Simulation")
    print("=" * 30)
    for i, node in enumerate(path, 1):
        print(f"  {i}. Now at: {node}")
        time.sleep(1)
    
    print("\n🎯 Destination Reached! Delivery Complete!")
    print("=" * 50)