from visualizer_screen import VisualizerScreen
from constants import ALGO_DELAY_MS
import time

class SelectionSort(VisualizerScreen):
    def __init__(self, parent, navigator):
        super().__init__(parent, navigator, "Selection Sort")

    def on_start_click(self):
        self.selection_sort(0)

    def selection_sort(self, i):
        if i < self.length - 1:
            min_index = i
            for j in range(i + 1, self.length):
                if self.array[j] < self.array[min_index]:
                    min_index = j

            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.drawArray()
            self.after(ALGO_DELAY_MS, self.selection_sort, i + 1)
