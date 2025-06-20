import tkinter as tk
from tkinter import ttk # Import ttk
from tkinter import scrolledtext, messagebox
from powershell_generator.generator import generate_script

def main():
    # Create the root window
    root = tk.Tk()
    root.title("PowerShell Automation Creator")

    # Set application icon
    try:
        photo = tk.PhotoImage(file='icon.png') # Assumes icon.png is in the same directory
        root.iconphoto(True, photo)
    except tk.TclError:
        print("Error: Could not load application icon 'icon.png'. Make sure it's in the project root directory.")

    # Apply a ttk theme
    style = ttk.Style(root)
    style.theme_use('clam')

    # Main content frame
    content_frame = ttk.Frame(root, padding=(10, 10, 10, 10))
    content_frame.pack(fill=tk.BOTH, expand=True)

    # Add a basic label (optional, could be removed if frame implies title)
    # For now, let's keep it simple and focused on the input elements within the frame
    # title_label = ttk.Label(content_frame, text="PowerShell Automation Creator", font=("Arial", 16))
    # title_label.pack(pady=(0, 20))


    # Task Name Label and Entry
    task_name_label = ttk.Label(content_frame, text="Task Name:")
    task_name_label.pack(pady=(5,0), padx=5, fill=tk.X)
    task_name_entry = ttk.Entry(content_frame, width=50)
    task_name_entry.pack(pady=(0,10), padx=5, fill=tk.X)

    # Custom style for the button
    # Important: Style configuration should ideally be done after theme_use,
    # and the style object 'style' is already defined earlier.
    style.configure('Custom.TButton', font=('Helvetica', 10, 'bold'), background='#4CAF50', foreground='white')
    # Note: Some themes might override background/foreground. 'clam' can be tricky with button backgrounds.
    # If background doesn't change, font should still apply.

    # Generate Script Button
    generate_button = ttk.Button(content_frame, text="Generate Script", command=generate_script_action, style='Custom.TButton')
    generate_button.pack(pady=10, padx=5)

    # Text area to display generated script
    script_display_area = scrolledtext.ScrolledText(content_frame, width=60, height=10, wrap=tk.WORD)
    script_display_area.pack(pady=(0,10), padx=5, fill=tk.BOTH, expand=True)
    script_display_area.insert(tk.INSERT, "Generated script will appear here...")
    script_display_area.configure(state='disabled') # Make it read-only initially

    # Function to handle script generation and display (needs to be defined before button command)
    def generate_script_action(): # Ensure this function is defined before being assigned to the button
        task_name = task_name_entry.get().strip() # Get and strip whitespace
        if not task_name:
            messagebox.showerror("Error", "Task Name cannot be empty.")
            return

        generated_code = generate_script(task_name)

        script_display_area.configure(state='normal') # Enable editing to insert text
        script_display_area.delete(1.0, tk.END) # Clear previous content
        script_display_area.insert(tk.INSERT, generated_code)
        script_display_area.configure(state='disabled') # Make it read-only again

    # Re-assign command to button if generate_script_action was defined after button creation
    # This is a bit of a reorder, so let's make sure the function is defined first.
    # The original code had the function definition after its first potential use by the button.
    # To fix this, the function generate_script_action is moved up or button configured later.
    # For this diff, I will assume the function definition is moved before this block.
    # The previous diff did not include the function definition, so I will redefine it here to ensure order.

    # (The diff will show the function being moved, effectively)
    # The button's command should be assigned after generate_script_action is defined.
    # The previous code structure was:
    # 1. Define button (referencing generate_script_action)
    # 2. Define generate_script_action
    # This is fine in Python as function names are just references.
    # The issue was the Welcome Label was outside the content_frame.
    # I'll remove the top "Welcome" label as the window title and frame are enough.

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    # The generate_script_action function is already defined above the button in the new structure.
    # The welcome label "label = ttk.Label(root, text="Welcome to PowerShell Automation Creator!")"
    # was outside the new content_frame. I'll remove it for a cleaner look,
    # relying on the window title and the frame for context.
    main()
