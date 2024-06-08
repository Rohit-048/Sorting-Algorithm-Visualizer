import tkinter as tk
from home_screen import HomeScreen
from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from quick_sort import QuickSort
from constants import SCR_HEIGHT, SCR_WIDTH, SCREEN_MIN_HEIGHT_LIMIT, SCREEN_MIN_WIDTH_LIMIT
from navigator import Navigator
from visualizer_screen import VisualizerScreen

root = tk.Tk()
root.title("SAV")
root.geometry(f"{SCR_WIDTH}x{SCR_HEIGHT}")
root.minsize(SCREEN_MIN_WIDTH_LIMIT, SCREEN_MIN_HEIGHT_LIMIT)

navigator = Navigator(root)

navigator.addFrame("home", HomeScreen(root, navigator))
navigator.addFrame("bubble_sort", BubbleSort(root, navigator))
navigator.addFrame("insertion_sort", InsertionSort(root, navigator))
navigator.addFrame("merge_sort", MergeSort(root, navigator))
navigator.addFrame("quick_sort", QuickSort(root, navigator))
navigator.addFrame("visualize", VisualizerScreen(root, navigator, "Visualize"))  # Add Visualize frame

navigator.showPage("home")

root.mainloop()
