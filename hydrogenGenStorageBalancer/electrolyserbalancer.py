import sys
import platform
import tkinter as tk
from tkinter import messagebox

def main():
    # Detect operating system
    os_name = platform.system()

    # Create main window
    root = tk.Tk()
    root.title(f"Running on {os_name}")
    root.geometry("400x200")

    # Create a label entry for max. electrolyser capacity
    tk.Label(root, text="Max. electrolsyer capacity: ").grid(row=0, column=0)
    ely_capacity_label = tk.Label(root, text="MW")
    ely_capacity_label.grid(row=0, column=2)
    max_ely_capacity = tk.Entry(root)
    max_ely_capacity.grid(row=0, column=1)


    # Validate max_ely_capacity as float
    def get_ely_capacity_as_float():
        try:
            return float(max_ely_capacity.get())
        except ValueError:
            root.statusvar = tk.StringVar()
            root.statusvar.set("Error: Invalid Input. Please enter a number.")
            status_label = tk.Label(root, textvariable=root.statusvar)
            status_label.grid(row=2, column=0, columnspan=3)    

    #Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except ImportError as e:
        # This block helps if tk is not available, such as if it it's not installed in Linux
        if "tkinter" in str(e):
            print("Error: Tkinter is not installed.")
            if platform.system() == "Linux":
                print("On Ubuntu/Debian, run: sudo apt install python3-tk")
                print("On Fedora, run: sudo dnf install python3-tkinter")
                print("On Arch, run: sudo pacman -S tk")
            else:
                raise e