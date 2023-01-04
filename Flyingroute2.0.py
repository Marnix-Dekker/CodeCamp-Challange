import sys

def find_shortest_route(connections_str):
  # Parse the input string into a dictionary of connections
  connections = {}
  for line in connections_str.s().split("\n"):
    print(line)
    a, b, p = line.split()
    a, b, p = int(a), int(b), int(p)
    if a not in connections:
      connections[a] = {}
    if b not in connections[a]:
      connections[a][b] = p
    else:
      connections[a][b] = min(connections[a][b], p)

  # Implement Dijkstra's algorithm to find the shortest route
  num_cities = max(connections.keys())
  distances = [sys.maxsize] * (num_cities + 1)
  previous = [None] * (num_cities + 1)
  distances[1] = 0
  visited = set()

  while len(visited) < num_cities:
    min_distance = sys.maxsize
    min_vertex = None
    for i in range(1, num_cities + 1):
      if i not in visited and distances[i] < min_distance:
        min_distance = distances[i]
        min_vertex = i
    visited.add(min_vertex)

    if min_vertex is None:
      break

    for neighbor, cost in connections[min_vertex].items():
      if neighbor not in visited:
        new_distance = cost + distances[min_vertex]
        if new_distance < distances[neighbor]:
          distances[neighbor] = new_distance
          previous[neighbor] = min_vertex

  # Construct the shortest route
  city = num_cities
  route = [city]
  while city != 1:
    city = previous[city]
    route.append(city)
  route = list(reversed(route))

  return route, distances[num_cities]

if __name__ == "__main__":
    inputData = ""
    while True:
        line = input()
        if line == "":
            break
        inputData += line + "\n"
    result, cost = find_shortest_route(inputData)
    print(result)
