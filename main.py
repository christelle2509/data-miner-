import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Define the window layout
        self.geometry("800x600")  # Window size
        self.title("RaptorVision Data Miner")  # Window title
        self.iconbitmap(r'C:\Users\nicke\OneDrive\Personal Files\Projects\RaptorVision-Data-Miner\RaptorVision-Data-Miner\gui_icon.ico')

        # Create a style for the frames
        style = ttk.Style()
        style.configure("TFrame", background="#fafafa")
        style.configure("TButton", background="#e4e5f1", foreground="#484b6a")

        # Create the main container
        self.container = ttk.Frame(self, style="TFrame")
        self.container.grid(sticky='nsew')
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)  # set the second column to expand more

        # Create a top bar
        self.top_bar = tk.Frame(self.container, relief="solid", borderwidth=1, background='#d2d3db')
        self.top_bar.grid(row=0, column=0, columnspan=2, sticky='ew')

        # Add buttons to the top bar
        top_bar_buttons = ["Modules", "Execute", "New", "Open", "Save", "Cancel", "Exit"]
        for i, button_name in enumerate(top_bar_buttons):
            self.top_bar.columnconfigure(i, weight=1)
            button = tk.Button(self.top_bar, text=button_name, background='#9394a5', foreground='#fafafa')
            if button_name == "Modules":
                button.configure(command=self.toggle_sidebar)
            button.grid(row=0, column=i, sticky="nsew")  # use grid instead of pack

        # Create a sidebar
        self.sidebar = tk.Frame(self.container, width=200, height=600, relief="solid", borderwidth=1, background='yellow')
        self.sidebar.grid(row=1, column=0, sticky='ns')

        # Create a new frame to hold the segment frames
        self.frames_container = ttk.Frame(self.container, style="TFrame")
        self.frames_container.grid(row=1, column=1, sticky='nsew')

        # Add squares to the sidebar
        self.frames = {}
        segments = ["Overview", "Data", "Testing", "Transformation", "Clustering", "Association", "Modeling", "Evaluation"]
        for segment in segments:
            frame_class = globals()[segment.replace(" ", "_")]
            frame = frame_class(parent=self.frames_container, controller=self)
            self.frames[segment] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            button = tk.Button(self.sidebar, text=segment, command=lambda segment=segment: self.show_frame(segment), background='#9394a5', foreground='#fafafa')
            button.pack(side="top", fill="x")

        self.show_frame("Overview")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def toggle_sidebar(self):
        # Hide or show the sidebar depending on its current state
        if self.sidebar.winfo_viewable():
            self.sidebar.grid_remove()
        else:
            self.sidebar.grid()

class Overview(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Overview page", font=("Helvetica", 18))
        label.pack(side="top", fill="x", pady=10)

class Data(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Data page", font=("Helvetica", 18))
        label.pack(side="top", fill="x", pady=10)

class Testing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Testing page", font=("Helvetica", 18))
        label.pack(side="top", fill="x", pady=10)

class Transformation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Transformation page", font=("Helvetica", 18))
        label.pack(side="top", fill="x", pady=10)

class Clustering(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Clustering page", font=("Helvetica", 18))
        label.pack(side="top", fill="x", pady=10)

class Association(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Association page", font=("Helvetica", 18))
        label.pack(side="top", fill="x", pady=10)

class Modeling(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Modeling page", font=("Helvetica", 18))
        label.pack(side="top", fill="x", pady=10)

class Evaluation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label

if __name__ == "__main__":
    app = Application()
    app.mainloop()
