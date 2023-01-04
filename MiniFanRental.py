def select_clients(data):
    # Create a list of tuples for each client
    clients = []
    for line in data.split('\n'):
        if line:
            index, start, end = line.split()
            clients.append((int(index), int(start), int(end)))

    # Sort the list of clients in ascending order based on start day
    clients.sort(key=lambda x: x[1])

    # Initialize an empty list to store the selected clients
    selected = []

    # Initialize the current day to the start day of the first client
    current_day = clients[0][1]

    # Iterate through the clients
    for index, start, end in clients:
        # If the current day is before the start day of the client, update the current day
        if current_day < start:
            current_day = start
        # If the current day is after the end day of the client, continue to the next iteration
        if current_day > end:
            continue
        # If the current day is between the start and end days of the client, add the client to the selected list and update the current day
        selected.append(index)
        current_day = end + 1

    # Return the selected clients as a single-line string
    return ' '.join(str(i) for i in selected)

if __name__ == "__main__":
    inputData = ""
    while True:
        line = input()
        if line == "":
            break
        inputData += line + "\n"
    result = select_clients(inputData)
    print(result)
