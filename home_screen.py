import tkinter as tk
from tkinter import ttk

class HomeScreen(tk.Frame):
    def __init__(self, parent, navigator):
        super().__init__(parent)

        tk.Label(self, text="Welcome Geek!", font=('Roman', 40)).pack(padx=10, pady=10)
        tk.Label(self, text="Select One Algorithm to visualize.").pack()
        tk.Label(self).pack(pady=4)
        fr = tk.Frame(self)

        btn_bubble_sort = ttk.Button(fr, text="Bubble Sort", padding=(20, 20), command=lambda: navigator.showPage('bubble_sort'))
        btn_bubble_sort.grid(row=0, column=0)

        btn_insertion_sort = ttk.Button(fr, text="Insertion Sort", padding=(20, 20), command=lambda: navigator.showPage('insertion_sort'))
        btn_insertion_sort.grid(row=0, column=1)

        btn_selection_sort = ttk.Button(fr, text="Selection Sort", padding=(20, 20), command=lambda: navigator.showPage('selection_sort'))
        btn_selection_sort.grid(row=1, column=0)  

        btn_merge_sort = ttk.Button(fr, text="Merge Sort", padding=(20, 20), command=lambda: navigator.showPage('merge_sort'))
        btn_merge_sort.grid(row=1, column=1) 

        btn_quick_sort = ttk.Button(fr, text="Quick Sort", padding=(20, 20), command=lambda: navigator.showPage('quick_sort'))
        btn_quick_sort.grid(row=2, column=0)

        fr.pack()

        back_button = ttk.Button(self, text="Back to Home", command=navigator.goHome)
        back_button.pack(pady=10)
