import tkinter as tk
import tkinter.font as tkFont
import os

class App:
    def __init__(self, root):
        root.title("Check")
        
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_103 = tk.Button(root)
        GButton_103["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_103["font"] = ft
        GButton_103["fg"] = "#000000"
        GButton_103["justify"] = "center"
        GButton_103["text"] = "Chụp Ảnh"
        GButton_103.place(x=160, y=110, width=231, height=83)
        GButton_103["command"] = self.call_file1

        GButton_756 = tk.Button(root)
        GButton_756["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_756["font"] = ft
        GButton_756["fg"] = "#000000"
        GButton_756["justify"] = "center"
        GButton_756["text"] = "phân tích ảnh"
        GButton_756.place(x=160, y=210, width=231, height=83)
        GButton_756["command"] = self.call_file2

        GButton_417 = tk.Button(root)
        GButton_417["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_417["font"] = ft
        GButton_417["fg"] = "#000000"
        GButton_417["justify"] = "center"
        GButton_417["text"] = "Check Face"
        GButton_417.place(x=160, y=310, width=231, height=83)
        GButton_417["command"] = self.print_abc

    def call_file1(self):
        os.system('Face_take_a_photo.py')

    def call_file2(self):
        os.system('Face_image_processing.py')

    def print_abc(self):
        os.system('Face_check.py')

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()