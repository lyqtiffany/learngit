#56 画图，学用circle画圆形。
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import Canvas
if __name__ == '__main__':

    import tkinter
    canvas = Canvas(width=800, height=600, bg='yellow')
    canvas.pack()
    k = 1
    j = 1
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
        k += j
        j += 0.3
    root = tkinter.Tk()
    root.mainloop()