# Create a class called ‘triathlon’
class Triathlon:
    # Introduce the name, location, time of the athletes
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        # total time is the total of the different events
        self.total_time = swim_time + cycle_time + run_time
# Describe the results of the whole process
    def print_details(self):
      # All times are in minutes 
      print(f"{self.first_name} {self.last_name} completed the Triathlon at {self.location} with a swim time of {self.swim_time} minutes, a cycle time of {self.cycle_time} minutes, a run time of {self.run_time} minutes, and a total time of {self.total_time} minutes.")
# For example
athlete = Triathlon("Jack", "Young", "Haining", 20, 30, 40)
athlete.print_details()
