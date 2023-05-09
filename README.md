File Renamer
This program allows the user to easily rename all files of a certain extension in a directory. 
It includes options to rename PNG files to JPG and JPG files to PNG.

Installation
Clone or download this repository.
Make sure you have Python 3 installed on your computer.
Install the required dependencies by running pip install -r requirements.txt.

Usage
Open the terminal or command prompt and navigate to the directory where the program is saved.
Run the program by typing python file_renamer.py.
Select the directory containing the files you want to rename.
Click the "PNG to JPG" button to rename all PNG files to JPG or click the "JPG to PNG" button to rename all JPG files to PNG.
The progress bar will indicate the progress of the renaming process, and the status label will display any errors or the completion of the process.

How it works
The program uses the os and tkinter modules in Python. It defines a function rename_files that takes a directory, the extension of the files to be renamed, and the new extension as arguments. It then uses the os.listdir function to get a list of all files in the directory that have the old extension. It loops through each file and renames it to the new extension using the os.rename function.

The program also defines two functions png_to_jpg_click and jpg_to_png_click that are triggered when the corresponding buttons are clicked. These functions use the filedialog module from tkinter to prompt the user to select a directory, and then call the rename_files function to rename the files in that directory with the specified extensions.

The progress bar and status label are updated in real-time to keep the user informed about the progress of the renaming process.

Contributing
If you have suggestions for improvements or find any bugs, please feel free to open an issue or pull request on GitHub.

License
This program is licensed under the MIT License. See the LICENSE file for details.