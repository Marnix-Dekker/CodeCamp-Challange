import datetime

def choose_performers(performers, opening_time, closing_time):
    # Sort the performers by their earnings per minute in descending order
    performers.sort(key=lambda x: x[2] / get_duration_in_minutes(x[1]), reverse=True)

    # Initialize the current time and the list of chosen performers
    current_time = datetime.datetime.strptime(opening_time, '%H:%M')
    chosen_performers = []

    # Iterate through the sorted list of performers
    for performer in performers:
        # Calculate the duration of the performer's performance in minutes
        duration = get_duration_in_minutes(performer[1])

        # If the performer can fit into the schedule, add them to the list of chosen performers and update the current time
        if current_time + datetime.timedelta(minutes=duration) <= datetime.datetime.strptime(closing_time, '%H:%M'):
            chosen_performers.append(performer[0])
            current_time += datetime.timedelta(minutes=duration)
        else:
            # If the performer cannot fit into the schedule, break out of the loop
            break

    return chosen_performers

def get_duration_in_minutes(duration_str):
    # Split the duration string into hours and minutes
    hours, minutes = duration_str.split(':')
    # Convert the hours and minutes to minutes and return the result
    return int(hours) * 60 + int(minutes)
if __name__ == "__main__":
    input = '''
1 1:10 243
2 1:13 250
3 1:17 268
4 1:20 270
5 1:22 281
6 1:27 293
7 1:30 311
8 1:34 331
9 1:38 346
10 1:46 362
11 1:50 378
12 1:53 385
13 1:55 398
14 1:58 412
15 2:00 432
'''
    performers = []
    for line in input.strip().split('\n'):
        source, destination, price = map(str, line.split())
        performers.append((int(source), destination, int(price)))
    print(performers)

    # Choose the performers for the lineup
    chosen_performers = choose_performers(performers, '08:30', '21:00')

    # Print the IDs of the chosen performers
    print(chosen_performers)

