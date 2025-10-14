import tkinter as tk
from tkinter import ttk
from c import Controller
from functools import partial

class SimpleGUI:
    """A minimal GUI window using Tkinter."""

    def __init__(self, controller=None):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Simple GUI Window")
        # Set a reasonable default size
        self.root.geometry("400x200")

        # Friendly label
        label = ttk.Label(
            self.root,
            text="To Do List",
            font=("Segoe UI", 12),
            anchor="center",
        )
        label.pack(pady=20)

        # Close button
        # close_btn = ttk.Button(self.root, text="Close", command=self.root.destroy)
        # close_btn.pack()

        # c1 = tk.Checkbutton(self.root, text='Test', command=self.root.destroy)
        # c1.pack()

    def show(self,items):
        for item in items:
            print("showing item:", item)
            action=partial(box_checked,item)
            cb = tk.Checkbutton(self.root, text=item, command=action)
            cb.pack()



    def run(self):
        """Start the Tkinter event loop."""
        self.root.mainloop()


def box_checked(item):
    print("Box checked! "+item)

if __name__ == "__main__":
    
    items=["Buy groceries", "Walk the dog", "Read a book"]
    sg = SimpleGUI()
    sg.show(items)
    sg.run()
    #SimpleGUI().show(items)
    #SimpleGUI().run()
