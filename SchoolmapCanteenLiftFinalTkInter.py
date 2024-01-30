import tkinter as tk
from tkinter import ttk
import heapq

def dijkstra(graph, start, end, is_disabled=False):
    # Priority queue to store nodes with their tentative distances
    priority_queue = [(0, start)]

    # Dictionary to store tentative distances
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Dictionary to store the previous node in the shortest path
    previous = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            # Reached the destination, reconstruct the path
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = previous[current_node]
            return current_distance, path

        if current_distance > distances[current_node]:
            # Skip if the current distance is greater than the known distance
            continue

        for neighbor in graph[current_node]:
            distance = current_distance + graph[current_node][neighbor].get('Weight', 0)

            # Check if the user is disabled and if there is a lift available
            if is_disabled and graph[current_node][neighbor].get('Type', '') == 'Stairs':
                # Skip stairs if the user is disabled
                continue
            elif not is_disabled and graph[current_node][neighbor].get('Type', '') == 'Lift':
                # Skip the lift for able users
                continue
            else:
                distance += graph[current_node][neighbor].get('Weight', 0)  # No adjustment needed for non-stairs/non-lift nodes

            if distance < distances[neighbor]:
                # Update the tentative distance and previous node
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # If no path is found
    return float('infinity'), []

def find_path():
    # Get values from GUI elements
    is_disabled_user = is_disabled_var.get()
    start_node = start_node_var.get()
    end_node = end_node_var.get()

    # Find the shortest path
    shortest_distance, path = dijkstra(school_map, start_node, end_node, is_disabled=is_disabled_user)

    if shortest_distance == float('infinity'):
        result_label.config(text=f"There is no path from {start_node} to {end_node}.")
    else:
        user_ability = "Disabled" if is_disabled_user else "Able"
        result_label.config(text=f"The user is {user_ability}.\n"
                                  f"The shortest distance from {start_node} to {end_node} is {shortest_distance} units.\n"
                                  f"The path is: {' -> '.join(path)}")

# Updated example graph representation with floor information, divisions, and corrected connections
# Format: {node: {neighbor1: {'Type': type1, 'Weight': weight1}, neighbor2: {...}, ...}}
school_map = {
    'Classroom1-3-B': {'Hallway3-B': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom2-3-B': {'Hallway3-B': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom3-3-B': {'Hallway3-B': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom4-3-B': {'Hallway3-B': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom5-3-B': {'Hallway3-B': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom6-3-B': {'Hallway3-B': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom7-3-B': {'Hallway3-B': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom8-3-B': {'Hallway3-B': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom1-3-C': {'Hallway3-C': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom2-3-C': {'Hallway3-C': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom3-3-C': {'Hallway3-C': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom4-3-C': {'Hallway3-C': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom5-3-C': {'Hallway3-C': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom6-3-C': {'Hallway3-C': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom7-3-C': {'Hallway3-C': {'Type': 'Hallway', 'Weight': 1}},
    'Classroom8-3-C': {'Hallway3-C': {'Type': 'Hallway', 'Weight': 1}},
    'Hallway0-B': {'Stairs0-B': {'Type': 'Stairs', 'Weight': 1},
                  'MainHall': {'Type': 'Hallway', 'Weight': 1}},
    'Hallway1-B': {'Stairs1-B': {'Type': 'Stairs', 'Weight': 1},
                  'Hallway1-C': {'Type': 'Hallway', 'Weight': 1}},
    'Hallway2-B': {'Stairs2-B': {'Type': 'Stairs', 'Weight': 1},
                  'Hallway2-C': {'Type': 'Hallway', 'Weight': 1}},                  
    'Hallway3-B': {'Classroom1-3-B': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom2-3-B': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom3-3-B': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom4-3-B': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom5-3-B': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom6-3-B': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom7-3-B': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom8-3-B': {'Type': 'Classroom', 'Weight': 1},
                  'Stairs3-B': {'Type': 'Stairs', 'Weight': 1},
                  'Hallway3-C': {'Type': 'Hallway', 'Weight': 1}},
    'Stairs0-B': {'Hallway0-B': {'Type': 'Hallway', 'Weight': 1},
                  'Stairs1-B': {'Type': 'Stairs', 'Weight': 1}},
    'Stairs1-B': {'Hallway1-B': {'Type': 'Hallway', 'Weight': 1},
                  'Stairs2-B': {'Type': 'Stairs', 'Weight': 1},
                  'Stairs0-B': {'Type': 'Stairs', 'Weight': 1}},
    'Stairs2-B': {'Hallway2-B': {'Type': 'Hallway', 'Weight': 1},
                  'Stairs3-B': {'Type': 'Stairs', 'Weight': 1},
                  'Stairs1-B': {'Type': 'Stairs', 'Weight': 1}},
    'Stairs3-B': {'Hallway3-B': {'Type': 'Hallway', 'Weight': 1},
                  'Stairs2-B': {'Type': 'Stairs', 'Weight': 1}},
    'Hallway0-C': {'Stairs0-C': {'Type': 'Stairs', 'Weight': 1},
                  'Lift': {'Type': 'Lift', 'Weight': 1},
                  'MainHall': {'Type': 'Hallway', 'Weight': 1}},
    'Hallway1-C': {'Stairs1-C': {'Type': 'Stairs', 'Weight': 1},
                  'Lift': {'Type': 'Lift', 'Weight': 1},
                  'Hallway1-B': {'Type': 'Hallway', 'Weight': 1}},
    'Hallway2-C': {'Stairs2-C': {'Type': 'Stairs', 'Weight': 1},
                  'Lift': {'Type': 'Lift', 'Weight': 1},
                  'Hallway2-B': {'Type': 'Hallway', 'Weight': 1}},
    'Hallway3-C': {'Classroom1-3-C': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom2-3-C': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom3-3-C': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom4-3-C': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom5-3-C': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom6-3-C': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom7-3-C': {'Type': 'Classroom', 'Weight': 1},
                  'Classroom8-3-C': {'Type': 'Classroom', 'Weight': 1},
                  'Stairs3-C': {'Type': 'Stairs', 'Weight': 1},
                  'Lift': {'Type': 'Lift', 'Weight': 1},
                  'Hallway3-B': {'Type': 'Hallway', 'Weight': 1}},
    'Stairs0-C': {'Hallway0-C': {'Type': 'Hallway', 'Weight': 1},
                  'Stairs1-C': {'Type': 'Stairs', 'Weight': 1}},
    'Stairs1-C': {'Hallway1-C': {'Type': 'Hallway', 'Weight': 1},
                  'Stairs2-C': {'Type': 'Stairs', 'Weight': 1},
                  'Stairs0-C': {'Type': 'Stairs', 'Weight': 1}},
    'Stairs2-C': {'Hallway2-C': {'Type': 'Hallway', 'Weight': 1},
                  'Stairs3-C': {'Type': 'Stairs', 'Weight': 1},
                  'Stairs1-C': {'Type': 'Stairs', 'Weight': 1}},
    'Stairs3-C': {'Hallway3-C': {'Type': 'Hallway', 'Weight': 1},
                  'Stairs2-C': {'Type': 'Stairs', 'Weight': 1}},
    'Lift': {'Hallway0-C': {'Type': 'Lift', 'Weight': 1},
                  'Hallway1-C': {'Type': 'Lift', 'Weight': 1},
                  'Hallway2-C': {'Type': 'Lift', 'Weight': 1},
                  'Hallway3-C': {'Type': 'Lift', 'Weight': 1}},
    'MainHall': {'Hallway0-B': {'Type': 'Hallway', 'Weight': 1},
                  'Hallway0-C': {'Type': 'Hallway', 'Weight': 1},
                  'Canteen': {'Type': 'Hallway', 'Weight': 1}},
    'Canteen': {'MainHall': {'Type': 'Hallway', 'Weight': 1}}
}

# Create the main Tkinter window
root = tk.Tk()
root.title("School Map Navigation")

# Create a main frame
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Variables for GUI elements
is_disabled_var = tk.BooleanVar()
start_node_var = tk.StringVar()
end_node_var = tk.StringVar()

# Create GUI elements
is_disabled_checkbox = tk.Checkbutton(mainframe, text="Disabled", variable=is_disabled_var)
start_node_label = tk.Label(mainframe, text="Start Node:")
start_node_dropdown = ttk.Combobox(mainframe, textvariable=start_node_var)
start_node_dropdown['values'] = tuple(school_map.keys())
end_node_label = tk.Label(mainframe, text="End Node:")
end_node_dropdown = ttk.Combobox(mainframe, textvariable=end_node_var)
end_node_dropdown['values'] = tuple(school_map.keys())
find_path_button = ttk.Button(mainframe, text="Find Path", command=find_path)
result_label = ttk.Label(mainframe, text="")

# Arrange GUI elements in a grid
is_disabled_checkbox.grid(row=0, column=0, columnspan=2, sticky=tk.W)
start_node_label.grid(row=1, column=0, sticky=tk.W)
start_node_dropdown.grid(row=1, column=1, sticky=(tk.W, tk.E))
end_node_label.grid(row=2, column=0, sticky=tk.W)
end_node_dropdown.grid(row=2, column=1, sticky=(tk.W, tk.E))
find_path_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))
result_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))

# Run the Tkinter event loop
root.mainloop()
