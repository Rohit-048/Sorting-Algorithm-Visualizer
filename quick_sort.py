from visualizer_screen import VisualizerScreen
from constants import ALGO_DELAY_MS

class QuickSort(VisualizerScreen):
    def __init__(self, parent, navigator):
        super().__init__(parent, navigator, "Quick Sort")

    def on_start_click(self):
        self.quick_sort(0, len(self.array) - 1)

    def quick_sort(self, low, high):
        if low < high:
            partition_index = self.partition(low, high)
            self.quick_sort(low, partition_index - 1)
            self.quick_sort(partition_index + 1, high)

    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1

        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.drawArray()
                self.update_idletasks()
                self.after(ALGO_DELAY_MS)

        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        self.drawArray()
        self.update_idletasks()
        self.after(ALGO_DELAY_MS)

        return i + 1

    def stopSorting(self):
        # You may need to add additional logic to stop Quick Sort if needed
        pass
