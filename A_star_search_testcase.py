import time

def simulate_path(path, visit_order, tot_cost):
    """Simulate truck traveling along the path"""
    print("\n🚛 Truck traveling...\n")
    for node in path:
        print(f"Car is now at: {node}")
        time.sleep(1)
    print("\n🎯 Destination reached!")
    
    print(f"\nVisited Order: {visit_order}")
    print(f"Optimal Path: {path}")
    print(f"Total Cost: {tot_cost} km")

# This would be called from the main program
# simulate_path(path, visited_order, total_cost)