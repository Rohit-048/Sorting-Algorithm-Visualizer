import tkinter as tk

class PageNavigator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Page Navigation")
        self.geometry("400x300")

        self.pages = {}
        self.current_page = None

        # Create and add pages
        self.add_page("Page 1", Page1)
        self.add_page("Page 2", Page2)
        self.add_page("Page 3", Page3)

        # Show the initial page
        self.show_page("Page 1")

        # Add navigation buttons
        prev_button = tk.Button(self, text="Previous", command=self.show_previous_page)
        prev_button.pack(side=tk.LEFT, padx=10)
        next_button = tk.Button(self, text="Next", command=self.show_next_page)
        next_button.pack(side=tk.RIGHT, padx=10)

    def add_page(self, page_name, page_class):
        page = page_class(self)
        self.pages[page_name] = page

    def show_page(self, page_name):
        if self.current_page:
            self.current_page.pack_forget()  # Hide the current page

        self.current_page = self.pages[page_name]
        self.current_page.pack(fill=tk.BOTH, expand=True)  # Show the selected page

    def show_previous_page(self):
        page_names = list(self.pages.keys())
        current_index = page_names.index(self.current_page.page_name)
        previous_index = (current_index - 1) % len(page_names)
        self.show_page(page_names[previous_index])

    def show_next_page(self):
        page_names = list(self.pages.keys())
        current_index = page_names.index(self.current_page.page_name)
        next_index = (current_index + 1) % len(page_names)
        self.show_page(page_names[next_index])

class Page1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.page_name = "Page 1"
        label = tk.Label(self, text="This is Page 1")
        label.pack(pady=10)

class Page2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.page_name = "Page 2"
        label = tk.Label(self, text="This is Page 2")
        label.pack(pady=10)

class Page3(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.page_name = "Page 3"
        label = tk.Label(self, text="This is Page 3")
        label.pack(pady=10)

if __name__ == "__main__":
    app = PageNavigator()
    app.mainloop()
