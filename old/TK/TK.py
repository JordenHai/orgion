#coding=gbk
# from tkinter import *
# master =Tk()
# def callback():
#     print('click!')
#最普通的返回操作，按钮返回一个值（通过一个函数传递）
#b=Button(master,text='OK',command=callback)

#DISABLED  state状态    表示不能按下这个按钮，无法操作这个按钮
#b = Button(master, text="Help", state=DISABLED)

#当你不设置大小的时候，按钮能容纳所有东西；当然你也可以指定大小：padx，pady
#b = Button(master, text="Help", state=DISABLED,padx=59,pady=99)

#当然我们也可以在按钮里面在写入一个窗体，窗体一般是用像素来表示的，所以按钮也是可以按照像素来进行表示的，位图也是可以的
# f = Frame(master, height=320, width=320)
# f.pack_propagate(0) # don't shrink
# f.pack()
# b = Button(f, text="Sure!")#将窗体导入
# b.pack(fill=BOTH, expand=1)#填充顶部，扩展

# #当text有多行的时候
# b = Button(master, text='longtext阿士大夫撒旦法士大夫撒旦法', anchor=W, justify=LEFT, padx=2)

# 这个操作是让按钮好像已经按下去了但是实际上没有触发按钮的功能，再点击就能触发
# b.config(relief=SUNKEN)

# b = Checkbutton(master, image=, variable='var', indicatoron=0)
# b = Button(master, text="Click me", image='pattern', compound=CENTER)


# b.pack()
#
# mainloop()
#coding=gbk
#
# activebackground, activeforeground:当按钮被激活时所使用的颜色
# anchor:控制按钮上内容的位置。使用N, NE, E, SE, S, SW, W, NW, or CENTER这些值之一。默认值是CENTER。
# background (bg), foreground (fg):按钮的颜色。默认值与特定平台相关。
# bitmap:显示在窗口部件中的位图。如果image选项被指定了，则这个选项被忽略。下面的位图在所有平台上都有 效：error, gray75, gray50, gray25, gray12, hourglass, info, questhead, question, 和 warning.
#
# borderwidth (bd):按钮边框的宽度。默认值与特定平台相关。但通常是1或2象素。
# command:当按钮被按下时所调用的一个函数或方法。所回调的可以是一个函数、方法或别的可调用的Python对象。
# cursor:当鼠标移动到按钮上时所显示的光标。
# default:如果设置了，则按钮为默认按钮。
# disabledforeground:当按钮无效时的颜色。
# image:在部件中显示的图象。如果指定，则text和bitmap选项将被忽略。
# justify:定义多行文本如何对齐。可取值有：LEFT, RIGHT, 或 CENTER。
# padx, pady:指定文本或图象与按钮边框的间距。
# state:按钮的状态：NORMAL, ACTIVE 或 DISABLED。默认值为NORMAL。
# relief:边框的装饰。通常按钮按下时是凹陷的，否则凸起。另外的可能取值有GROOVE, RIDGE, 和 FLAT。
# text:显示在按钮中的文本。文本可以是多行。如果bitmaps或image选项被使用，则text选项被忽略
# textvariable:
# underline:在文本标签中哪个字符加下划线。默认值为-1，意思是没有字符加下划线
# width, height:按钮的尺寸。如果按钮显示文本，尺寸使用文本的单位。如果按钮显示图象，尺寸以象素为单位（或屏幕的单位）。如果尺寸没指定，它将
# 根据按钮的内容来计算。


# #coding=gbk
# from tkinter import *
# master = Tk()

# w = Label(master, text="Hello, world!")
#
# w = Label(master, text="Rouge", fg="red")
w = Label(master, text="Helvetica", font=("Helvetica", 16))

# w = Label(master, text=longtext, anchor=W, justify=LEFT)
#
# v = StringVar()
# Label(master, textvariable=v).pack()
# v.set("New Text!")
#
# # b.pack()
# mainloop()
