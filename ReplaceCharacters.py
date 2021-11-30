import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path

root = tk.Tk()
root.withdraw()


messagebox.showinfo('Select Folder', 'Please select the folder containing the files you want to be renamed.')

# open file dialog and select a file manually
path = filedialog.askdirectory()

if len(path) == 0:
    messagebox.showinfo('Error', 'No file was selected.')
    quit()

print(path)


if messagebox.askyesno('Proceed?', 'You have selected "' + path + '". Do you want to proceed with renaming the files?') == True:

    selected_folder = Path(path).glob('*.*')

    for file in selected_folder:
        new_file = file.stem.replace("_"," ")
        new_file = path + '/' + new_file + file.suffix
 
        file.rename(new_file)
        print(new_file)
        
