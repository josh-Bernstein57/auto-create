import unittest
import sys
import os

# Adjust sys.path to allow importing from the parent directory (project root)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from powershell_generator.generator import generate_script

class TestPowerShellGenerator(unittest.TestCase):

    def test_generate_script_with_task_name(self):
        """
        Tests if generate_script produces the expected output for a given task name.
        """
        task_name = "My Test Task"
        expected_comment = f"# PowerShell script for task: {task_name}"
        expected_command = f"Write-Host \"Script generated for task: {task_name}\""

        script_output = generate_script(task_name)

        self.assertIn(expected_comment, script_output, "Script should contain the task name in a comment.")
        self.assertIn(expected_command, script_output, "Script should contain the Write-Host command with the task name.")
        self.assertIn("# Add your PowerShell commands here", script_output, "Script should contain placeholder for commands.")

    def test_generate_script_without_task_name(self):
        """
        Tests if generate_script handles an empty task name gracefully.
        """
        task_name = ""
        # The generator.py assigns "Untitled Task" if task_name is empty
        expected_task_name = "Untitled Task"
        expected_comment = f"# PowerShell script for task: {expected_task_name}"
        expected_command = f"Write-Host \"Script generated for task: {expected_task_name}\""

        script_output = generate_script(task_name)

        self.assertIn(expected_comment, script_output, "Script should default to 'Untitled Task' in comment when no name is provided.")
        self.assertIn(expected_command, script_output, "Script should use 'Untitled Task' in Write-Host when no name is provided.")

    def test_generate_script_structure(self):
        """
        Tests the basic structure of the generated script.
        """
        task_name = "Structure Test"
        script_output = generate_script(task_name)
        lines = script_output.strip().split('\n')

        self.assertTrue(lines[0].startswith("# PowerShell script for task:"), "First line should be a comment with task name.")
        self.assertEqual(lines[1], "# Add your PowerShell commands here", "Second line should be the command placeholder.")
        self.assertTrue(lines[2].startswith("Write-Host"), "Third line should be a Write-Host command.")

if __name__ == '__main__':
    unittest.main()
