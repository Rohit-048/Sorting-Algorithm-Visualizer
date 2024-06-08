import tkinter as tk
from tkinter import ttk

class MyUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Custom UI Example")
        value = tk.IntVar()

        # Back button
        back_button = ttk.Button(self, text="<-", command=self.on_back_button_click, width=5)
        back_button.grid(row=0, column=0, padx=5, pady=5)

        # Title label
        title_label = tk.Label(self, text="Bubble Sort", font=('Helvetica', 24, 'bold'))
        title_label.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Buttons
        buttons_frame = ttk.Frame(self)
        buttons_frame.grid(row=0, column=2, padx=10, pady=5)

        button1 = ttk.Button(buttons_frame, text="Start", command=self.on_button1_click, width=5)
        button1.grid(row=0, column=0, padx=5, pady=5)

        button2 = ttk.Button(buttons_frame, text="Reset", command=self.on_button2_click, width=5)
        button2.grid(row=0, column=1, padx=5, pady=5)

        button3 = ttk.Button(buttons_frame, text="Re-Try", command=self.on_button3_click, width=5)
        button3.grid(row=0, column=2, padx=5, pady=5)

        # Slider
        value.set(20)
        self.slTxt = tk.Label(self,text=str(value.get()))
        self.slTxt.grid(row=1,column=0)

        def changeSliderValue(v):
            print(value.get())
            self.slTxt = tk.Label(self,text=str(value.get()))
            self.slTxt.grid(row=1,column=0)
        
        slider = ttk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL,variable=value,command=changeSliderValue)
        slider.grid(row=1, column=1, columnspan=3,  sticky=tk.W+tk.E)


    def on_back_button_click(self):
        print("Back button clicked!")

    def on_button1_click(self):
        print("Button B1 clicked!")

    def on_button2_click(self):
        print("Button B2 clicked!")

    def on_button3_click(self):
        print("Button B3 clicked!")

if __name__ == "__main__":
    app = MyUI()
    app.mainloop()
