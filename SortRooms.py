def assign_rooms(groups):
  # Sort the groups by size, with the largest groups coming first
  groups.sort(reverse=True)
  # Keep track of the hostel rooms and their capacities
  rooms = []

  # Iterate through the groups of friends
  for group in groups:
    # Try to find a hostel room with enough capacity
    room_found = False
    for room in rooms:
        if room + group <= 10:
            # Assign the group to this room
            room = room + group
            room_found = True
            break
    
    if not room_found:
      # No room was found, so create a new one and assign the group to it
      rooms.append(group)

  return rooms


if __name__ == "__main__":
    inputData = "7 5 1 2 2 3 2 5 2 7 3 2 7 2 1 1 2 7 2 7 3 4 3 3 2 1 2 7 2 3 7 2 2 1 1 5 3 7 2 3 2 5 3 3 2 1 2 2 2 8 3 2 2 7 3 7 4 2 1 2 1 6 3 2 2 1 7 4 6 5 2 3 1 3 3 3 2 5 2 1 2 2 2 1 7 2 2 6 1 3 1 1 2 4 7 2 8 2 3 2 1 2 3 5 3 2 8 7 4 7 2 5 5 7 5 5 1 7 2 7 2 2 1 5 1 3 4 2 3 1 1 3 1 4 5 5 1 1 1 2 1 2 5 2 1 1 2 4 7 7 3 1 1 7 5 2 1 2 7 2 3 2 2 7 3 1 2 2 8 2 7 5 6 1 7 6 2 2 3 7 2 3 7 4 1 1 3 1 8 3 2 2 2 5 2 2 5 2 5 2 1 2 8 3 1 2 5 7 2 2 4 7 2 8 2 1 2 5 1 1 2 5 1 2 7 2 5 3 2 2 2 2 7 1 1 7 4 2 1 1 2 2 7 2 2 7 2 1 5 1 7 1 7 8 1 4 1 7 8 4 4 7 2 2 5 2 7 5 7 4 5 1 7 2 3 2 2 2 1 5 2 4 7 3 6 6 7 5 1 5 6 1 1 4 5 2 1 1 1 2 2 2 2 7 2 3 3 7 7 2 7 2 7 5 2 1 2 4 7 7 4 1 1 5 6 1 1 1 3 8 3 1 4 5 6 7 2 7 1 7 3 2 2 4 4 3 3 3 3 8 3 3 7 8 2 1 5 4 5 7 2 1 7 1 1 8 2 2 1 7 7 3 3 7 2 6 5 1 4 6 3 7 1 4 1 7 6 7 1 3 2 7 5 2 3 2 7 7 1 2 4 2 3"

    splitInputData = inputData.split()
    splitInputData = [ int(x) for x in splitInputData ]
    print(splitInputData)
    print("assigned groups:")
    print(str(assign_rooms(splitInputData)).replace(",", ""))
