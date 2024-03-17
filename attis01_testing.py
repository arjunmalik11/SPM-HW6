import unittest
from unittest.mock import patch
from io import StringIO

from main import SprintVelocityCalculator, TeamEffortCalculator, main as project_main

class TestSprintVelocityCalculator(unittest.TestCase):
    """
    Test suite for the SprintVelocityCalculator class, which calculates average sprint velocity based on completed story points.
    """

    def test_with_non_empty_list(self):
        """
        Test the average velocity calculation with a non-empty list of completed story points.
        """
        calculator = SprintVelocityCalculator([10, 20, 30])
        self.assertAlmostEqual(calculator.calculate_average_velocity(), 20.0, "The calculated average velocity should be 20.0.")

    def test_with_empty_list(self):
        """
        Test the average velocity calculation with an empty list, which should default to 0.
        """
        calculator = SprintVelocityCalculator([])
        self.assertEqual(calculator.calculate_average_velocity(), 0, "The calculated average velocity should be 0 for an empty list.")


class TestCalculateEffortHoursPerPerson(unittest.TestCase):
    """
    Test suite for static method calculate_effort_hours_per_person in the TeamEffortCalculator class.
    Tests various input scenarios including zero values, maximum realistic values, and negative values.
    """

    def test_zero_values(self):
        """
        Test with all inputs set to zero, expecting the result also to be zero.
        """
        result = TeamEffortCalculator.calculate_effort_hours_per_person(0, 0, 0, 0)
        self.assertEqual(result, 0, "The calculated effort hours per person should be 0 for all zero inputs.")

    def test_max_values(self):
        """
        Test with maximum realistic values for sprint days and work hours, expecting a high number of effort-hours.
        """
        result = TeamEffortCalculator.calculate_effort_hours_per_person(30, 0, 0, 24)
        self.assertEqual(result, 720, "The calculated effort hours should reflect the maximum work capacity.")

    def test_negative_values(self):
        """
        Test with negative values to ensure method handles unexpected input gracefully.
        The exact result depends on the method's implementation.
        """
        result = TeamEffortCalculator.calculate_effort_hours_per_person(-10, -5, -2, -8)
        self.assertEqual(result, 87, "The calculated effort hours should handle negative inputs in a defined manner.")


class AcceptanceTests(unittest.TestCase):
    """
    Acceptance tests for verifying that the command-line interface of the application correctly interacts with user inputs and produces expected outputs.
    """

    @patch('builtins.input', side_effect=["10 20 30", "0", "0", "0", "0", "no"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_feature_a_average_velocity_output(self, mock_stdout, mock_input):
        """
        Test that the application correctly calculates and displays the average sprint velocity.
        """
        project_main()
        self.assertIn("Average Velocity: 20.0", mock_stdout.getvalue(), "The output should correctly display the calculated average velocity.")

    @patch('builtins.input', side_effect=["10 20 30", "10", "8", "2", "8", "no"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_feature_b_total_effort_hours_output(self, mock_stdout, mock_input):
        """
        Test that the application correctly calculates and displays the total available effort-hours for the team.
        """
        project_main()
        self.assertIn("Total Available Effort-Hours for Team: 70", mock_stdout.getvalue(), "The output should correctly display the total available effort-hours for the team.")


if __name__ == '__main__':
    unittest.main()