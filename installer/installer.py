import tkinter as tk
from tkinter import filedialog
import os
import subprocess

#############################################################################
# VARIABLES                                                                 #
installation_path = r""
pangolang_logo = """
    ⠀⣀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣿⡀⢻⣿⣿⣿⣿⣿⣶⠀⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠛⠓⠀⢻⣿⡿⠋⣉⣀⣀⢘⣿⣿⣿⡇⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣾⣿⣿⣿⣿⠀⣾⣿⣿⣿⣿⡿⠟⠛⠧⠈⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣿⣿⣿⡿⠿⠄⠹⣿⣿⣿⡃⢰⣶⣶⣶⣦⣴⣿⣿⠇⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣿⡏⢠⣴⣶⣦⣤⣼⣿⣿⡷⠄⠉⠉⣉⡉⠛⢿⡏⢰⣿⣦⡀⠀⠀⠀⠀⠀⠀
    ⠀⣿⡀⢿⣿⣿⣿⣿⣿⣿⠋⣠⣶⣧⡈⠛⠻⣷⣄⠁⠘⣿⣿⣷⡀⠀⠀⠀⠀⠀
    ⠀⢉⠁⠘⢿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠈⠛⢿⣷⡀⠀⠀⠀⠀
    ⠀⣿⣿⣷⣿⡿⠛⣉⡉⠁⢸⠃⠈⠙⠻⢿⣿⣿⣿⣷⣶⣾⣷⣄⠙⠳⠀⠀⠀⠀
    ⠀⣿⣿⣿⣿⡀⢾⣿⣿⡇⠘⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⣿⣿⣿⣿⣦⡀⠀⠀⠀
    ⠀⠿⠋⣉⣉⡁⠈⠻⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀
    ⠀⠀⣾⣿⣿⣿⣷⣶⣿⡏⢡⣤⣤⠀⢀⣤⣄⡐⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠙⢿⣿⣿⡿⠛⣉⣁⣀⣿⠃⠐⠛⠿⣿⣷⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠈⠉⠃⠘⠿⠟⠛⠋⠀⠀⠀⠀⢹⠃⠀⠀⠀
"""
pangolang_text = """
  ██▓███   ▄▄▄       ███▄    █   ▄████  ▒█████   ██▓    ▄▄▄       ███▄    █   ▄████ 
 ▓██░  ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▒██▒  ██▒▓██▒   ▒████▄     ██ ▀█   █  ██▒ ▀█▒
 ▓██░ ██▓▒▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▒██░  ██▒▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░
 ▒██▄█▓▒ ▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██   ██░▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓
 ▒██▒ ░  ░ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒░ ████▓▒░░██████▒▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒
 ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ 
 ░▒ ░       ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░   ░ ▒ ▒░ ░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░░         ░   ▒      ░   ░ ░ ░ ░   ░ ░ ░ ░ ▒    ░ ░    ░   ▒      ░   ░ ░ ░ ░   ░ 
                ░  ░         ░       ░     ░ ░      ░  ░     ░  ░         ░       ░ 
                                                                                   
"""

#                                                                           #
#############################################################################

#############################################################################
# FUNCTIONS                                                                 #
def browse_path():
    path = filedialog.askdirectory() # Open a file dialog window
    entry_path.delete(0, tk.END)  # Clear the current entry field
    entry_path.insert(0, path)   # Insert the selected path
    
    # Update the installation path variable
    global installation_path
    installation_path = r'{}'.format(path)

    

def add_to_path(path):
    # Check if the path already exists in the PATH environment variable
    if path not in os.environ['PATH']:
        # Append the program path to the PATH variable
        os.environ['PATH'] = f"{path};{os.environ['PATH']}"

        # Save the updated PATH environment variable
        cmd = 'setx PATH "{}"'.format(os.environ['PATH'])
        subprocess.call(cmd, shell=True)

        return 0
    else:
        return 1
    
def install_pangolang():
    pangobat_path = installation_path + "/pangolang_v1.2/pango.bat"
    # get pangolang files from github
    # install them to the path installation_path
    # add pangobat to the path
#                                                                           #
#############################################################################

#############################################################################
# TKINTER GUI                                                               #
root = tk.Tk()
root.title("Pangolang installer")


# Create a label for the combined text (ASCII art and additional text)
combined_label = tk.Label(root, text=pangolang_text + pangolang_logo, font=("Courier New", 10))
combined_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

# Create a label for the path entry
entry_label = tk.Label(root, text="Enter a folder to install Pangolang files in:")
entry_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# Create an entry widget for path input
entry_path = tk.Entry(root, width=50)
entry_path.grid(row=1, column=1, padx=10, pady=5)

# Create a "Browse" button
browse_button = tk.Button(root, text="Browse", command=browse_path)
browse_button.grid(row=1, column=2, padx=10, pady=5)

# Create an "Install" button
install_button = tk.Button(root, text="Install", command=install_pangolang)
install_button.config(height=2, width=20)  # Adjust the button size as needed
install_button.grid(row=2, column=0, columnspan=3, pady=20)

root.mainloop()
#                                                                           #
#############################################################################