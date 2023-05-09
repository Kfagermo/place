import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# define the function to handle the file renaming png to jpg
def rename_files(directory, ext_from, ext_to):
    # get a list of all files with ext_from extension in the directory
    files = [filename for filename in os.listdir(directory) if filename.endswith(ext_from)]
    num_files = len(files)
    if num_files == 0:
        status_label["text"] = f"No {ext_from} files found in directory."
        root.update()
        return

    progress_bar["maximum"] = num_files
    status_label["text"] = f"Renaming {num_files} {ext_from} files to {ext_to}..."
    root.update()

    # loop through each file and rename it to the new extension
    for i, filename in enumerate(files):
        try:
            # get the new file name by replacing the extension
            new_filename = filename.replace(ext_from, ext_to)
            # rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            # update the progress bar and status message
            progress_bar["value"] = i + 1
            status_label["text"] = f"Renamed {i + 1} of {num_files} files to {ext_to}."
            root.update()
        except Exception as e:
            # if there's an error, update the status message to show the error
            status_label["text"] = f"Error renaming file: {e}"
            root.update()

    # update the status message to show that the renaming is complete
    status_label["text"] = f"Finished renaming {num_files} files to {ext_to}."


# define the function to handle the button click for PNG to JPG conversion
def png_to_jpg_click():
    # prompt the user to select a directory
    directory = filedialog.askdirectory()
    # call the function to rename the PNG files to JPG
    rename_files(directory, ".png", ".jpg")


# define the function to handle the button click for JPG to PNG conversion
def jpg_to_png_click():
    # prompt the user to select a directory
    directory = filedialog.askdirectory()
    # call the function to rename the JPG files to PNG
    rename_files(directory, ".jpg", ".png")


# create the main window
root = tk.Tk()
root.title("File Renamer")
root.geometry("400x250")  # set the window size

# create a description label
description_label = tk.Label(root, text="Select a directory to rename all files of a certain extension.")
description_label.pack(pady=10)

# create a progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# create a status label
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# create a button to trigger the PNG to JPG file renaming
png_to_jpg_button = tk.Button(root, text="PNG to JPG", command=png_to_jpg_click)
png_to_jpg_button.pack(pady=5)

# create a button to trigger the JPG to PNG file renaming
jpg_to_png_button = tk.Button(root, text="JPG to PNG", command=jpg_to_png_click)
jpg_to_png_button.pack(pady=5)

# start the main event loop
root.mainloop()
