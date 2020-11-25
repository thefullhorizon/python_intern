# -*- coding=utf-8 -*-
"""

Tkinter 的简单学习,仅了解，不专业学习

Author       :   Cucumber
Date         :   11/16/20

"""
import tkinter as tk


def analysis():

    pass


window = tk.Tk()
window.title('Job analysis')
window.geometry('500x300')

label = tk.Label(window, text='hello Tkinter', font=('Arial', 20))
label.pack()

# tk.Label(window, text='The key :', font=('Arial', 16)).place(x=10, y=170)

# var_usr_name = tk.StringVar()
# var_usr_name.set('xx')
# entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
# entry_usr_name.place(x=120, y=175)
#
# btn_analysis = tk.Button(window, text='analysis', command=analysis)
# btn_analysis.place(x=120, y=240)

window.mainloop()
