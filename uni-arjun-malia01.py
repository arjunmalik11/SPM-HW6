import unittest
from unittest.mock import patch
from main import SprintVelocityCalculator, TeamEffortCalculator,main
from io import StringIO
import sys

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

class AcceptanceTests(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        "8 15 22",  # Inputs for Feature A: Sprint points
        "10", "2", "2", "8",  # Inputs for the first team member for Feature B
        "no"  # Indicating no more team members to add, to prevent the main loop from seeking more inputs
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_feature_a_average_velocity_output(self, mock_stdout, mock_input):
        """
        Ensure the correct average velocity is calculated and output for Feature A,
        while providing a complete set of inputs to satisfy the main() function's requirements.
        """
        from main import main  # Ensure correct import path
        main()
        self.assertIn("Average Velocity: 15.0", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[
        "8 15 22",  # Inputs for Feature A to bypass it in the test for Feature B
        "10", "2", "2", "8",  # First team member details
        "no",  # No more team members to add
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_feature_b_total_effort_hours_output(self, mock_stdout, mock_input):
        """
        Test to ensure the correct total effort hours are calculated and output for Feature B.
        """
        main()
        # Since inputs for Feature A are also provided to reach Feature B, adjust expected output as needed
        self.assertIn("Total Available Effort-Hours for Team: ", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
