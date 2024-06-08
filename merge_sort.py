from visualizer_screen import VisualizerScreen
from constants import ALGO_DELAY_MS

class MergeSort(VisualizerScreen):
    def __init__(self, parent, navigator):
        super().__init__(parent, navigator, "Merge Sort")
        self.sorting = False  # Flag to indicate if sorting is in progress

    def on_start_click(self):
        if not self.sorting:
            self.sorting = True
            array = self.array.copy()
            self.merge_sort(array, 0, len(array) - 1)

    def merge_sort(self, array, left, right):
        if self.sorting and left < right:
            mid = (left + right) // 2

            self.merge_sort(array, left, mid)
            self.merge_sort(array, mid + 1, right)

            if self.sorting:  # Check if sorting should continue
                self.merge(array, left, mid, right)

    def merge(self, array, left, mid, right):
        if self.sorting:
            n1 = mid - left + 1
            n2 = right - mid

            L = [array[left + i] for i in range(n1)]
            R = [array[mid + 1 + i] for i in range(n2)]

            i = j = 0
            k = left

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1

            while i < n1:
                array[k] = L[i]
                i += 1
                k += 1

            while j < n2:
                array[k] = R[j]
                j += 1
                k += 1

            if self.sorting:  # Check if sorting should continue
                self.array = array.copy()
                self.drawArray()
                self.update_idletasks()
                self.after(ALGO_DELAY_MS, self.merge_sort, array, left, right)
        else:
            # Sorting is stopped, reset the array to the original state
            self.array = self.original_array.copy()
            self.drawArray()

    def stopSorting(self):
        self.sorting = False  # Set sorting to False to stop the sorting process
