import tkinter as tk
window = tk.Tk()  #creating window 
window.title("GUI")# rename the title window
# label=tkinter.Label(window,text="Hello World!").pack()

l1=tk.Label(window,text="Eruka",font=("Arial", 25)).pack()#using font here nad adding its size 
# window.geometry('350x200')# setting dimensions


bt=tk.Button(window,text="Enter")
bt=bt.grid(column=1,row=0)

window.mainloop()
