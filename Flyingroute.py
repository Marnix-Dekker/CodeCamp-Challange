def find_route(data):
    # Create a dictionary of sets to store the connections for each city
    connections = {}
    highest_city = 1
    for line in data.split('\n'):
        if line:
            a, b, p = line.split()
            a, b, p = int(a), int(b), int(p)
            highest_city = max(highest_city, a, b)
            if a not in connections:
                connections[a] = set()
            if b not in connections:
                connections[b] = set()
            connections[a].add((b, p))
            connections[b].add((a, p))

    # Initialize the queue with the starting city
    queue = [(1, 0)]
    visited = set()

    # Perform a breadth-first search to find the shortest path
    while queue:
        city, cost = queue.pop(0)
        if city == highest_city:
            # Return the path as a string
            return ' '.join(str(c) for c in visited) + ' ' + str(highest_city)
        visited.add(city)
        for next_city, next_cost in connections[city]:
            if next_city not in visited:
                queue.append((next_city, cost + next_cost))

if __name__ == "__main__":
    inputData = ""
    while True:
        line = input()
        if line == "":
            break
        inputData += line + "\n"
    result = find_route(inputData)
    print(result)
