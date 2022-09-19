import tkinter as tk


class MyGui:

    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Alarm Time", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)

        self.entry1 = tk.Entry(self.frame)
        self.entry1.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.entry2 = tk.Entry(self.frame)
        self.entry2.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.entry3 = tk.Entry(self.frame)
        self.entry3.grid(row=0, column=2, sticky=tk.W+tk.E)

        self.frame.pack(fill='x')

        self.button = tk.Button(self.root, text="Submit", font=("Arial", 12))
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

MyGui()