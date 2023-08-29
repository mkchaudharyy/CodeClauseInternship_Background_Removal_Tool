from pathlib import Path
from tkinter import filedialog
import tkinter as tk
from rembg import remove
from PIL import Image
from tkinter import simpledialog
from tkinter import messagebox


def select_file():
    file_name=filedialog.askopenfilename(filetypes=(("PNG files", "*.png"),))
    file_path.insert(0,file_name)


def select_file_path_tosave():
    saved_file=filedialog.askdirectory()
    output_path1.insert(0,saved_file)


def removebg():
   
    input_path=file_path.get()


   
    # rename file to save
    re_name=simpledialog.askstring("Input", "Give a name to you are file ?")
   
    output_path=output_path1.get()
    lastsave=output_path+"/"+re_name+".png"
    # Processing the image
   
    input = Image.open(input_path)
    # # Removing the background from the given Image
    removebg_out = remove(input)
    # #Saving the image in the given path
    removebg_out.save(lastsave)
    messagebox.showinfo("Info","You file have saved in this path\n"+lastsave)




window =tk.Tk()
window.geometry("320x150")

# layout elemetys
open_file=tk.Button(text="Select Your File to Remove BG " , command=select_file)
file_path=tk.Entry()
save_path=tk.Button(text="Select Path to Save the File ", command=select_file_path_tosave)
output_path1=tk.Entry()
remove_bg=tk.Button(text="Remove Background", bg="red",command=removebg)


#  layou control desgin
open_file.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
file_path.grid(row=0, column=1,columnspan=3,padx=5, sticky="ew", pady=5)
save_path.grid(row=1, column=0, sticky="ew",padx=5, pady=5)
output_path1.grid(row=1, column=1,columnspan=3, sticky="ew",padx=5, pady=5)
remove_bg.grid(row=2,column=0, sticky="ew",padx=5, pady=10)
window.resizable(False,True )
window.mainloop()




