# Import the unittest module and the classes from your code file
import unittest
from main import SprintVelocityCalculator, TeamEffortCalculator

class TestSprintVelocityCalculator(unittest.TestCase):
    def test_average_velocity_happy_path(self):
        """Test average velocity calculation with valid sprint points."""
        calculator = SprintVelocityCalculator([10, 20, 30])
        self.assertAlmostEqual(calculator.calculate_average_velocity(), 20.0)

    def test_average_velocity_unhappy_path(self):
        """Test average velocity calculation with an empty list."""
        calculator = SprintVelocityCalculator([])
        self.assertEqual(calculator.calculate_average_velocity(), 0)

class TestTeamEffortCalculator(unittest.TestCase):
    def test_total_team_effort_hours_happy_path(self):
        """Test total team effort hours calculation with valid team member details."""
        team_members = [
            {'days_in_sprint': 10, 'hours_off': 8, 'ceremony_hours': 2, 'hours_per_day': 8},
            {'days_in_sprint': 10, 'hours_off': 10, 'ceremony_hours': 2, 'hours_per_day': 8}
        ]
        calculator = TeamEffortCalculator(team_members)
        self.assertEqual(calculator.calculate_total_team_effort_hours(), 138)

    def test_total_team_effort_hours_unhappy_path(self):
        """Test total team effort hours calculation with an empty list of team members."""
        calculator = TeamEffortCalculator([])
        self.assertEqual(calculator.calculate_total_team_effort_hours(), 0)

if __name__ == '__main__':
    unittest.main()
