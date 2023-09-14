def print_my_name():
    print(name)

print_my_name('Bob')

def trip_planner(start, end, duration, mode):
    print(f"It lookss like you're starting your trip from {start}")
    print(f"You are planning to go to {end}")
    print(f"It should take you about {duration} hours")
    print(f"I see you are taking a {mode}")

trip_planner('Paradigm', 'the Delta Center', 0.5, 'car')