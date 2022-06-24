import tkinter as tk
from tkinter import messagebox

def button_inport():
    print(a_num.get())
    print(b_num.get())
    print(c_num.get())
    print(d_num.get())
    root.quit()
    root.destroy()
  


root = tk.Tk()
root.title('進貨')
root.geometry('250x120+650+350')
root.wm_attributes('-topmost',1)

a_num = tk.StringVar()
b_num = tk.StringVar()
c_num = tk.StringVar()
d_num = tk.StringVar()


mylabel = tk.Label(root, text='文具數量:')
mylabel.grid(row=0, column=0)
myentry = tk.Entry(root, textvariable=a_num )
myentry.grid(row=0, column=1)

mylabel2 = tk.Label(root, text='便當數量:')
mylabel2.grid(row=1, column=0)
myentry2 = tk.Entry(root, textvariable=b_num )
myentry2.grid(row=1, column=1)

mylabel3 = tk.Label(root, text='安全帽數量:')
mylabel3.grid(row=2, column=0)
myentry3 = tk.Entry(root, textvariable=c_num )
myentry3.grid(row=2, column=1)

mylabel3 = tk.Label(root, text='珠寶數量:')
mylabel3.grid(row=3, column=0)
myentry3 = tk.Entry(root, textvariable=d_num )
myentry3.grid(row=3, column=1)

mybutton = tk.Button(root, text='確認', command=button_inport)
mybutton.grid(row=4, column=1)

root.mainloop()
