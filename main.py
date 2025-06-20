import tkinter as tk
from tkinter import scrolledtext, messagebox # Import messagebox
from powershell_generator.generator import generate_script

def main():
    # Create the root window
    root = tk.Tk()
    root.title("PowerShell Automation Creator")

    # Add a basic label
    label = tk.Label(root, text="Welcome to PowerShell Automation Creator!")
    label.pack(padx=20, pady=20)

    # Task Name Label and Entry
    task_name_label = tk.Label(root, text="Task Name:")
    task_name_label.pack(pady=(10,0)) # Add some padding above the label
    task_name_entry = tk.Entry(root, width=50)
    task_name_entry.pack(pady=(0,10)) # Add some padding below the entry

    # Text area to display generated script
    script_display_area = scrolledtext.ScrolledText(root, width=60, height=10, wrap=tk.WORD)
    script_display_area.pack(pady=10)
    script_display_area.insert(tk.INSERT, "Generated script will appear here...")
    script_display_area.configure(state='disabled') # Make it read-only initially

    # Function to handle script generation and display
    def generate_script_action():
        task_name = task_name_entry.get().strip() # Get and strip whitespace
        if not task_name:
            messagebox.showerror("Error", "Task Name cannot be empty.")
            return

        generated_code = generate_script(task_name)

        script_display_area.configure(state='normal') # Enable editing to insert text
        script_display_area.delete(1.0, tk.END) # Clear previous content
        script_display_area.insert(tk.INSERT, generated_code)
        script_display_area.configure(state='disabled') # Make it read-only again

    # Generate Script Button
    generate_button = tk.Button(root, text="Generate Script", command=generate_script_action)
    generate_button.pack(pady=20)


    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
