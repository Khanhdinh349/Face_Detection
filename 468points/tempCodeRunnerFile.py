def call_file3(self):
        result_window = tk.Toplevel()
        result_window.title("Result")
        label = tk.Label(result_window, text="Yes")
        label.pack()
        result_window.after(3000, result_window.destroy)