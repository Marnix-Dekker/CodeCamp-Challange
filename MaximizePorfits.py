def maximize_profit(artists, opening_time):
  # Convert the opening time to minutes
  opening_time_minutes = int(opening_time.split(':')[0]) * 60 + int(opening_time.split(':')[1])

  # Sort the artists by their earnings per minute
  artists.sort(key=lambda x: x[2] / x[1], reverse=True)

  # Keep track of the schedule and the total earnings
  schedule = []
  total_earnings = 0
  time_remaining = opening_time_minutes

  # Iterate through the artists in order of decreasing earnings per minute
  for artist in artists:
    if artist[1] <= time_remaining:
      # There is enough time to schedule this artist
      schedule.append(artist[0])
      total_earnings += artist[2]
      time_remaining -= artist[1]
  
  return schedule, total_earnings

if __name__ == "__main__":
    artists = [[1, 60, 100], [2, 30, 60], [3, 90, 200], [4, 20, 50]]
    opening_time = "4:30"

    schedule, total_earnings = maximize_profit(artists, opening_time)
    print(schedule)
    print(total_earnings)
