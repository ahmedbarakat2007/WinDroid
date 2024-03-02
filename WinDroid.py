from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import os
import time
import psutil
from tkinter import messagebox
import zipfile

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x =(screen_width - width) // 2
    y =(screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def run():
    mem_byte = psutil.virtual_memory().total
    mem_gib = str(int(mem_byte / (1024.**2)))
    cpu_count = str(int(os.cpu_count()))
    try:
        if (os.path.isfile("Files/qemu/android.IMG") == True):
            os.system('Files\qemu\qemu-system-i386 -m '+ mem_gib +' -smp '+ cpu_count +' -display sdl,frame=off,window_close=on -hda Files/qemu/android.IMG --accel tcg,thread=multi -name "Windroid : Running"')
            root.destroy()
        else:
            if(os.path.isfile("Files/qemu/android.rom") == True):
                with zipfile.ZipFile("Files/qemu/android.rom", 'r') as zip_ref:
                    zip_ref.extractall("Files/qemu/")
                    os.remove("Files/qemu/android.rom")
                    os.system('Files\qemu\qemu-system-i386 -m '+ mem_gib +' -smp '+ cpu_count +' -display sdl,frame=off,window_close=on -hda Files/qemu/android.IMG --accel tcg,thread=multi -name "Windroid : Running"')
                    root.destroy()
            else:
                msg = messagebox.showerror("Error", "Rom File Not Found")
                root.destroy()
    except:
        msg = messagebox.showerror("Error", "SomeThing Wrong Happened!!")
        root.destroy()
    


root = tk.Tk()
center_window(root, 500, 100)
root.title('WinDroid')
root.iconbitmap("icon.ico")
root.resizable(0,0)
root.overrideredirect(True)
root.configure(bg = "white")
image1 = Image.open("icon.ico")
img = image1.resize((75, 70))  
test = ImageTk.PhotoImage(img)
label1 = Label(image=test,bg="white")
label1.image = test
# Position image
label1.place(x="90px",y="6px")

Label(text="WinDroid", font='san-serif 26 bold', fg="#01a6f0", bg="white").place(x="160px", y="24px")
root.after(5000,run)
root.mainloop()




