'''
上機考規定的GUI的形式
'''

import tkinter as tk
import tkinter.messagebox


def getText():

    global output_matrix
    global user_matrix_name
    inputData1 = textField1.get()
    inputData2 = textField2.get()

    out = inputData1 + inputData2
    tk.messagebox.showinfo('info',out)


window = tk.Tk()
window.title('demo demo demo')

textField1 = tk.Entry(window)
textField1.pack()
textField2 = tk.Entry(window)
textField2.pack()

button1 = tk.Button(window,text="draw",width=15,height=2,command=getText)
button1.pack()

window.mainloop()
