import tkinter as tk
import tkinter.font as tkFont
import subprocess
import os

class App:
    def __init__(self, root):
        root.title("Face Processing")
        
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
        GButton_756["text"] = "Phân tích Ảnh"
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
        GButton_417["command"] = self.call_file3

        self.output_label = tk.Label(root, text="")
        self.output_label.pack()

    def call_file1(self):
        subprocess.run(["python", "installer/FaceMesh.py"])

    def call_file2(self):
        result = subprocess.run(["python", "installer/FaceCheck.py"], capture_output=True, text=True)
        yes_count = result.stdout.count("Yes")
        total_count = len(result.stdout.splitlines())
        if total_count > 0 and (yes_count / total_count) > 0.5:
            self.show_result_window()

    def show_result_window(self):
        result_window = tk.Toplevel()
        result_window.title("Result")
        label = tk.Label(result_window, text="Yes")
        label.pack()
        result_window.after(3000, result_window.destroy)
        
    def call_file3(self):
        result_window = tk.Toplevel()
        result_window.title("Result")
        label = tk.Label(result_window, text="Yes")
        label.pack()
        result_window.after(3000, result_window.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()