# PowerShell Automation Creator

A simple GUI application built with Python and Tkinter to help create PowerShell automation scripts.

## Features

- User-friendly graphical interface.
- Input field for specifying a task name or purpose for the script.
- Generates a basic PowerShell script based on the input.
- Displays the generated script in the GUI.
- Basic error handling for empty inputs.
- Themed interface for a more modern look.

## Requirements

- Python 3.x
- Tkinter (usually included with Python standard library)

## How to Run

1. Ensure you have Python 3 installed.
2. Clone this repository or download the source code.
3. Navigate to the project's root directory in your terminal.
4. Run the application using the command:
   ```bash
   python main.py
   ```
5. (Optional) To see the application icon, place an `icon.png` file in the root directory of the project.

## Project Structure

- `main.py`: The main application script containing the GUI and core logic.
- `gui/`: Directory intended for GUI components (currently minimal).
- `powershell_generator/`: Directory for PowerShell script generation logic.
  - `generator.py`: Contains functions for generating PowerShell scripts.
- `tests/`: Directory for unit tests.
  - `test_generator.py`: Unit tests for the script generation logic.
- `README.md`: This file.
