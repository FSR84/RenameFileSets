import os
import tkinter as tk
from tkinter import Button, Entry, Label, filedialog
from tkinter import messagebox
from tkinter.constants import END
from pathlib import Path
import re

root = tk.Tk()
root.geometry('400x250')
root.title('Rename File Sets')


def get_template():

    path_and_file = filedialog.askopenfilename()
    path_name = os.path.split(path_and_file)[0]
    file_name = os.path.split(path_and_file)[1]

    entry_path.delete(0, END)
    entry_filename.delete(0, END)

    entry_path.insert(0, path_name)
    entry_filename.insert(0, file_name)

    return None


def rename_files():

    if len(entry_filename.get()) == 0:
        messagebox.showerror('Error','Template was not selected.')
        return None

    file_number = str(re.findall(r'\d+', entry_filename.get())[-1])
    file_number_len = len(file_number)
    file_name_stem = entry_filename.get().rsplit('.', 1)[0].rstrip(file_number)


    if messagebox.askyesno('Proceed?', 'You have selected "' + entry_filename.get() + '" as your template. \nAll files will be renamed in the folder below: \n"' + entry_path.get() + '" \nDo you want to proceed?') == True:

        selected_folder = Path(entry_path.get()).glob('*.*')

        for file in selected_folder:

            # try getting the number from the file name
            try:
                file_nr = str(re.findall(r'\d+', file.name)[-1])
                
                # correct cases with different numbering formats (leading zeros)
                if len(file_nr) > file_number_len:
                    file_nr = file_nr.lstrip('0')
                if len(file_nr) < file_number_len:
                    file_nr = file_nr.rjust(file_number_len,'0')

            except:
                file_nr = ''


            # rename files
            if file_nr != '':

                new_file = entry_path.get() + '/' + file_name_stem + file_nr + file.suffix

                try:
                    file.rename(new_file)
                    print(new_file)
    
                except: # for case where there are two files with the same number in the folder
                    print(f"Cannot rename {file}. A file with the same number already exists.")

    return None


label0 = Label(root,text="").pack()

Button(root, text="Select Template", command=get_template).pack()

label0 = Label(root,text="").pack()

label1 = Label(root,text="Folder for renaming:").pack()

entry_path = Entry(root, width=40)
entry_path.pack()

label0 = Label(root,text="").pack()

label2 = Label(root,text="Template:").pack()

entry_filename = Entry(root, width=40)
entry_filename.pack()

label0 = Label(root,text="").pack()

Button(root, text="Rename Files", command=rename_files).pack()


root.mainloop()
