from visualizer_screen import VisualizerScreen
from constants import ALGO_DELAY_MS
import time

class InsertionSort(VisualizerScreen):
    def __init__(self, parent, navigator):
        super().__init__(parent, navigator, "Insertion Sort")

    def on_start_click(self):
        self.insertion_sort(0)

    def insertion_sort(self, i):
        if i < self.length:
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
            self.drawArray()
            self.after(ALGO_DELAY_MS, self.insertion_sort, i + 1)


