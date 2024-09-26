import tkinter as tk
class CounterApp:
    def __init__(self, root):
        self.count = 0
        self.label = tk.Label(root, text=f"Count: {self.count}", font=("Arial", 24))
        self.label.pack()
        self.default_entry_label = tk.Label(root, text="Count Value:", font=("Arial", 12))
        self.default_entry_label.pack()
        self.default_entry = tk.Entry(root, width=5, font=("Arial", 18))
        self.default_entry.insert(0, "0")
        self.default_entry.pack()
        self.set_default_button = tk.Button(root, text="Set", font=("Arial", 12), command=self.set_default)
        self.set_default_button.pack()
        self.default_entry_label = tk.Label(root, text="Increment Value:", font=("Arial", 12))
        self.default_entry_label.pack()
        self.entry = tk.Entry(root, width=5, font=("Arial", 18))
        self.entry.insert(0, "1")
        self.entry.pack()
        tk.Button(root, text="+", font=("Arial", 20), command=self.increment).pack(side=tk.LEFT, padx=20)
        tk.Button(root, text="-", font=("Arial", 20), command=self.decrement).pack(side=tk.RIGHT, padx=20)
    def set_default(self):
        try:
            self.count = int(self.default_entry.get())
        except ValueError:
            self.count = 0
        self.label.config(text=f"Count: {self.count}")
    def update_count(self, value):
        try:
            increment_value = int(self.entry.get())
        except ValueError:
            increment_value = 1
        self.count += value * increment_value
        self.label.config(text=f"Count: {self.count}")
    def increment(self):
        self.update_count(1)
    def decrement(self):
        self.update_count(-1)
root = tk.Tk()
root.title("Increment/Decrement Counter")
app = CounterApp(root)
root.mainloop()