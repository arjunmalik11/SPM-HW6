class SprintVelocityCalculator:
    """
    A class to calculate the average sprint velocity for a team.

    Attributes:
        sprint_points (list): A list of integers representing the points completed in each sprint.
    """

    def __init__(self, sprint_points):
        """
        Initializes the SprintVelocityCalculator with a list of sprint points.

        :param sprint_points: A list of integers representing the completed points for each sprint.
        """
        self.sprint_points = sprint_points
    
    def calculate_average_velocity(self):
        """
        Calculates the average velocity of sprints based on completed points.

        :return: The average velocity as a float. Returns 0 if no sprint points are provided.
        """
        if not self.sprint_points:
            return 0  # Return 0 if sprint_points is empty
        return sum(self.sprint_points) / len(self.sprint_points)
    
    def print_average_velocity(self):
        """
        Prints the average sprint velocity.
        """
        average_velocity = self.calculate_average_velocity()
        print(f"Average Velocity: {average_velocity}")


class TeamEffortCalculator:
    """
    A class to calculate the total effort-hour capacity of a team for a sprint.

    Attributes:
        team_members (list): A list of dictionaries, each representing a team member's details.
    """

    def __init__(self, team_members):
        """
        Initializes the TeamEffortCalculator with team member details.

        :param team_members: A list of dictionaries, each containing details about a team member's availability and commitments.
        """
        self.team_members = team_members
    
    @staticmethod
    def calculate_effort_hours_per_person(days_in_sprint, hours_off, ceremony_hours, hours_per_day):
        """
        Calculates the available effort-hours for an individual team member.

        :param days_in_sprint: The total number of days in the sprint.
        :param hours_off: The number of hours the member is taking off during the sprint.
        :param ceremony_hours: The number of hours committed to sprint ceremonies.
        :param hours_per_day: The average number of hours the member is available for work per day.
        :return: The total available effort-hours for the team member.
        """
        return (days_in_sprint * hours_per_day) - hours_off - ceremony_hours
    
    def calculate_total_team_effort_hours(self):
        """
        Calculates the total available effort-hours for the entire team.

        :return: The sum of available effort-hours for all team members.
        """
        total_hours = 0
        for member in self.team_members:
            total_hours += self.calculate_effort_hours_per_person(
                member['days_in_sprint'],
                member['hours_off'],
                member['ceremony_hours'],
                member['hours_per_day']
            )
        return total_hours
    
    def print_total_team_effort_hours(self):
        """
        Prints the total available effort-hours for the team.
        """
        total_effort_hours = self.calculate_total_team_effort_hours()
        print(f"Total Available Effort-Hours for Team: {total_effort_hours}")

def main():
    """
    Main function to execute the program.
    """
    # Feature A: User Input for Sprint Points
    print("Enter the completed points for each sprint, separated by space:")
    sprint_points_input = input()  
    sprint_points = list(map(int, sprint_points_input.split()))
    velocity_calculator = SprintVelocityCalculator(sprint_points)
    velocity_calculator.print_average_velocity()

    # Feature B: User Input for Team Member Details
    print("\nEnter team member details for effort-hour calculation:")
    team_members = []
    more_members = True
    while more_members:
        print("\nEnter details for a new team member:")
        days_in_sprint = int(input("Number of sprint days: "))
        hours_off = int(input("Hours off (e.g., PTO): "))
        ceremony_hours = int(input("Hours committed to sprint ceremonies: "))
        hours_per_day = int(input("Number of hours available per day: "))
        team_members.append({
            'days_in_sprint': days_in_sprint,
            'hours_off': hours_off,
            'ceremony_hours': ceremony_hours,
            'hours_per_day': hours_per_day
        })
        
        add_more = input("Add more team members? (yes/no): ").lower()
        more_members = add_more == "yes"
    
    effort_calculator = TeamEffortCalculator(team_members)
    effort_calculator.print_total_team_effort_hours()

if __name__ == "__main__":
    main()