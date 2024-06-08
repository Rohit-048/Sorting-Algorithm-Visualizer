import tkinter as tk
from home_screen import HomeScreen
from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
from selection_sort import SelectionSort
from merge_sort import MergeSort
from quick_sort import QuickSort
from constants import SCR_HEIGHT, SCR_WIDTH, SCREEN_MIN_HEIGHT_LIMIT, SCREEN_MIN_WIDTH_LIMIT
from visualizer_screen import VisualizerScreen

class Navigator:
    current_page = None

    def __init__(self, root):
        self.root = root
        self.screens = {}

    def addFrame(self, key, screen_class):
        self.screens[key] = screen_class
     
    def instantiateHome(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = HomeScreen(self.root, self)
        self.current_page.pack()

    def instantiateSortingAlgorithm(self, key):
        if self.current_page:
            self.current_page.destroy()
        screen_class = self.screens[key]
        self.current_page = screen_class(self.root, self)
        self.current_page.pack()

    def showPage(self, key):
        if self.current_page:
            self.current_page.destroy()

        screen_class = self.screens[key]
        self.current_page = screen_class(self.root, self)
        self.current_page.pack()

    def goHome(self):
        if self.current_page:
            self.current_page.destroy()

        self.showPage("home")

root = tk.Tk()
root.title("SAV")

navigator = Navigator(root)

root.geometry(f"{SCR_WIDTH}x{SCR_HEIGHT}")
root.minsize(SCREEN_MIN_WIDTH_LIMIT, SCREEN_MIN_HEIGHT_LIMIT)

navigator.addFrame("home", HomeScreen)
navigator.addFrame("bubble_sort", BubbleSort)
navigator.addFrame("insertion_sort", InsertionSort)
navigator.addFrame("selection_sort", SelectionSort)
navigator.addFrame("merge_sort", MergeSort)
navigator.addFrame("quick_sort", QuickSort)
navigator.addFrame("visualize", VisualizerScreen)

navigator.showPage("home")

root.mainloop()
