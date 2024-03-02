class SprintVelocityCalculator:
    def __init__(self, sprint_points):
        self.sprint_points = sprint_points
    
    def calculate_average_velocity(self):
        if not self.sprint_points:
            return 0
        return sum(self.sprint_points) / len(self.sprint_points)