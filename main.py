import tkinter
import time


def get_time():
    time_str = time.strftime("%H:%M:%S")  # 获取当前的时间并转化为字符串
    lb.configure(text=time_str)  # 重新设置标签文本
    root.after(1000, get_time)  # 每隔1s调用函数自身获取时间


root = tkinter.Tk()
root.title('CLOCK')
root.wm_attributes('-alpha', 0.7)   # 设置窗口不透明度为0.7

lb = tkinter.Label(root, text='', fg='blue', font=("黑体", 80))
lb.pack()
get_time()
root.mainloop()
