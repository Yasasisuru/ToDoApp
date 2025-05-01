import tkinter as tk
from tkinter import ttk


root=tk.Tk()
root.title("TodoApp")


width=400
height=600
root.geometry(f"{width}x{height}+{int((root.winfo_screenwidth()/2)-(width/2))}+{int((root.winfo_screenheight()/2)-(height/2))}") #OPEN IN CENTER 
root.iconbitmap("icon.ico")
root.resizable(False,False)

hedding=ttk.Label(root,text="ALL TASKS" ,font="arial 16 bold")
hedding.pack()



frame=ttk.Frame(root,width=400,height=50)
tasks=ttk.Entry(frame,font="arial  12", width=30)
frame.pack(pady=12)
tasks.pack()

listFrame=ttk.Frame(root,height=250,width=300)
listFrame.pack()

listBox=tk.Listbox(listFrame,font="arial 12", width=40,height=22)
listBox.pack(pady=12)



root.mainloop()