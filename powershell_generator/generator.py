# powershell_generator/generator.py

def generate_script(task_name):
    """
    Generates a simple PowerShell script with a comment indicating the task name.
    """
    if not task_name:
        task_name = "Untitled Task"

    script_content = f"# PowerShell script for task: {task_name}\n"
    script_content += "# Add your PowerShell commands here\n"
    script_content += f"Write-Host \"Script generated for task: {task_name}\"\n" # Corrected f-string usage

    return script_content

if __name__ == '__main__':
    # Example usage:
    example_task = "My Automated Task"
    generated_script = generate_script(example_task)
    print(f"--- Generated Script for '{example_task}' ---")
    print(generated_script)
    print("------------------------------------------")

    example_task_no_name = ""
    generated_script_no_name = generate_script(example_task_no_name)
    print(f"--- Generated Script for (no name) ---")
    print(generated_script_no_name)
    print("------------------------------------------")
