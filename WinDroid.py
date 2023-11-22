from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import os
from tkinter import messagebox
import zipfile

option=[]

'''def options():
    def destroy():
        option.append(n.get())
        option.append(na.get())
        option.append(naa.get())

        print(option)
        
    m5 = Tk()
    m5.geometry("400x350")
    m5.configure(bg="white")
    m5.resizable(0, 0)
    m5.iconbitmap("icon.ico")
    m5.title("Options")

    

    Label(m5,text="",bg="white").pack()
    Label(m5,text="",bg="white").pack()
    Label(m5, text="Options", font='san-serif 16 bold' ,bg="white", foreground="black").pack()
    Label(m5,text="",bg="white").pack()
    Label(m5,text="",bg="white").pack()
    Label(m5, text="Ram:", font='san-serif 12 bold' ,bg="white", foreground="black").pack()

   

    reschoosen2 = ["512M","1G","2G","3G","4G","6G","8G","12G","16G"]
    n = tk.StringVar()
    n.set(reschoosen2[0])

    reschoosena = ttk.Combobox(m5, width = 27,values=reschoosen2, textvariable = n)
    reschoosena.pack()

    Label(m5, text="Network:", font='san-serif 12 bold' ,bg="white", foreground="black").pack()
    
    
    reschoosen3 = ["e1000","i82551","i82557b","i82559er","ne2k_pci","ne2k_isa","pcnet","rtl8139","virtio"]
    na = tk.StringVar()
    na.set(reschoosen3[0])
    
    reschoosenaa = ttk.Combobox(m5, width = 27,values=reschoosen3, textvariable = na)
    reschoosenaa.pack()
    

    Label(m5, text="VGA:", font='san-serif 12 bold' ,bg="white", foreground="black").pack()
    reschoosen4 = ["std","vmware","cirrus","qxl"]

    naa = tk.StringVar()
    naa.set(reschoosen4[0])
    reschoosenaaa = ttk.Combobox(m5, width = 27,values=reschoosen4, textvariable = naa)
    reschoosenaaa.pack()

    Label(m5,text="",bg="white").pack()
    Label(m5,text="",bg="white").pack()
    f8 = Button(m5, text='Ok', font='san-serif 16 bold', background='#01A6F0',foreground="white",borderwidth="0", padx=2,width="10", command=destroy).pack()

    m5.mainloop()'''
    

def run():
    try:
        if (os.path.isfile("Files/qemu/android.IMG") == True):
            if (entry.get() != ""):
                os.system("Files\qemu\qemu-system-i386w -m "+ entry.get()+" -display sdl,frame=off,window_close=on -hda Files/qemu/android.IMG --accel tcg,thread=multi")
            else:
                msg = messagebox.showerror("Error", "Please Enter Ram Amount")
        else:
            if(os.path.isfile("Files/qemu/android.rom") == True):
                with zipfile.ZipFile("Files/qemu/android.rom", 'r') as zip_ref:
                    zip_ref.extractall("Files/qemu/")
                os.remove("Files/qemu/android.rom")
                if (entry.get() != ""):
                    os.system("Files\qemu\qemu-system-i386w -m "+ entry.get()+" -display sdl,frame=off,window_close=on -hda Files/qemu/android.IMG --accel tcg,thread=multi")
                else:
                    msg = messagebox.showerror("Error", "Please Enter Ram Amount")
            else:
                msg = messagebox.showerror("Error", "Rom File Not Found")
    except:
        msg = messagebox.showerror("Error", "SomeThing Wrong Happened!!")


root = tk.Tk()
root.geometry("400x600")
root.title('WinDroid')
root.iconbitmap("icon.ico")
root.resizable(0,0)
root.configure(bg = "white")
image1 = Image.open("icon.ico")
test = ImageTk.PhotoImage(image1)
label1 = Label(image=test,bg="white")
label1.image = test
# Position image
label1.pack()
Label(root,text="",bg="white").pack()
Label(root,text="",bg="white").pack()
Label(root,text="Ram:",font='san-serif 14 bold',bg="white").pack()
reschoosen2 = ["512M","1G","1.5G","2G","3G","4G"]

entry = tk.StringVar()
reschoosen = ttk.Combobox(root, width = 27,values=reschoosen2, textvariable = entry).pack()
Label(root,text="",bg="white").pack()
Label(root,text="",bg="white").pack()
Label(root,text="",bg="white").pack()
f8 = Button(root, text='Run',font='san-serif 16 bold', background='#01A6F0',foreground="white",borderwidth="0", padx=2,width="10",command=run).pack()
Label(root,text="",bg="white").pack()
Label(root,text="",bg="white").pack()

root.mainloop()