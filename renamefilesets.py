import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
import re

root = tk.Tk()
root.withdraw()


messagebox.showinfo('Select Template', 'Please select the a file that will act as a template to rename other files in the same folder.')

# open file dialog and select a file manually
path_and_file = filedialog.askopenfilename()

if len(path_and_file) == 0:
    messagebox.showinfo('Error', 'No file was selected.')
    quit()
    
# template
path_name = os.path.split(path_and_file)[0]
file_name = os.path.split(path_and_file)[1]
file_number = str(re.findall(r'\d+', file_name)[-1])
file_number_len = len(file_number)
file_name_stem = file_name.rsplit('.', 1)[0].rstrip(file_number)


if messagebox.askyesno('Proceed?', 'You have selected "' + file_name + '" as your template. Do you want to proceed?') == True:

    selected_folder = Path(path_name).glob('*.*')

    for file in selected_folder:

        # correct cases with different numbering formats
        file_nr = str(re.findall(r'\d+', file.name)[-1])
        if len(file_nr) > file_number_len:
            if file_nr[0:1] == '0':                          # only remove zero if it is the first number
                file_nr = (file_nr)[1:len(file_nr)]
        elif len(file_nr) < file_number_len:
            file_nr = '0' + file_nr

        # rename files
        new_file = path_name + '/' + file_name_stem + file_nr + file.suffix
        file.rename(new_file)

        print(new_file)


