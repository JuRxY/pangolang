import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import requests
import sys

#############################################################################
# VARIABLES                                                                 #
github_user = "JuRxY"
github_repo = "pangolang"
repo_folder_path = "/pangolang_v1.2/"
api_url = f"https://api.github.com/repos/{github_user}/{github_repo}/contents/{repo_folder_path}"

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
    
def install_pangolang():
    pangobat_path = installation_path + "/pangolang_v1.2/pango.bat"
    # get pangolang files from github
    response = requests.get(api_url, headers={})

    if response.status_code == 200: # IF GITHUB URL WORKS
        folder_contents = response.json()

        # Create a local folder to save the downloaded files
        os.makedirs(installation_path, exist_ok=True)

        # Iterate through the folder contents and download files
        for item in folder_contents:
            if item.get('type') == 'file':
                file_name = os.path.basename(item['path'])
                local_file_path = os.path.join(installation_path, file_name)

                # Download the file and save it locally
                file_url = item['download_url']
                file_content = requests.get(file_url).content
                with open(local_file_path, "wb") as local_file:
                    local_file.write(file_content)
    else: # CRASH IF IT DOESNT WORK
        print(response)
        print(response.status_code)
        sys.exit()

    # add pango.bat to the path
    add_to_path(pangobat_path)

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