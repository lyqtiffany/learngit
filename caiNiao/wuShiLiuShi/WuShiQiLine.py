# 57画图，学用line画直线。
import tkinter
from tkinter import Canvas

if __name__ == '__main__':

    import tkinter
    canvas = Canvas(width=300, height=300, bg='green')
    canvas.pack()
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
        x0 = x0 - 5
        y0 = y0 - 5
        x1 = x1 + 5
        y1 = y1 + 5

    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0, y0, x0, y1, fill='red')
        x0 += 5
        y0 += 5
        y1 += 5

    root = tkinter.Tk()
    root.mainloop()

# Python3 中使用 turtle 模块画图
# import turtle
# def drawline(n):
#     t=turtle.Pen()
#     t.color(0.3,0.8,0.6)  #设置颜色，在0--1之间
#     t.begin_fill()   #开始填充颜色
#     for i in range(n): #任意边形
#         t.forward(50)
#         t.left(360/n)
#     t.end_fill()    #结束填充颜色
# drawline(4)