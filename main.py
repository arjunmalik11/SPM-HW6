class SprintVelocityCalculator:
    def __init__(self, sprint_points):
        self.sprint_points = sprint_points
    
    def calculate_average_velocity(self):
        if not self.sprint_points:
            return 0
        return sum(self.sprint_points) / len(self.sprint_points)
    
    def print_average_velocity(self):
        average_velocity = self.calculate_average_velocity()
        print(f"Average Velocity: {average_velocity}")

class TeamEffortCalculator:
    def __init__(self, team_members):
        self.team_members = team_members


def main():
    # Feature A: User Input for Sprint Points
    print("Enter the completed points for each sprint, separated by space:")
    sprint_points_input = input()  
    sprint_points = list(map(int, sprint_points_input.split()))
    velocity_calculator = SprintVelocityCalculator(sprint_points)
    velocity_calculator.print_average_velocity()

if __name__ == "__main__":
    main()