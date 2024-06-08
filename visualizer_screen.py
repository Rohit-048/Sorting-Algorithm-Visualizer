import tkinter as tk
from tkinter import ttk
import random as ran
import time


from constants import *

class VisualizerScreen(tk.Frame):
    canvas_width, canvas_height = CANVAS_WIDTH, CANVAS_HEIGHT

    orgArray = []
    orgSliderVal = SLIDER_DEFAULT_VALUE


    def __init__(self, parent,navigator,title):
        super().__init__(parent)
        self.navigator = navigator
        self.sliderValue = tk.IntVar()
        self.sliderValue.set(SLIDER_DEFAULT_VALUE)
        # header
        header = tk.Frame(self)
        header.pack(fill='x',expand=True,side="top")
        self.build_header(title,header)

        # canvas
        self.canvas = tk.Canvas(self, height=self.canvas_height,width=self.canvas_width)
        self.canvas.pack()


        self.initialize_array()
        self.drawArray()
        
    
    def build_header(self,title,parent):
        #  Back button
        back_button = ttk.Button(parent, text="<-", command=self.on_back_click, width=5)
        back_button.grid(row=0, column=0,pady=5)

        tk.Label(parent,text=title,font=('Roman',24)).grid(row=0,column=1,columnspan=2)

        startBtn = ttk.Button(parent, text="Start", command=self.on_start_click, width=5)
        startBtn.grid(row=0, column=3, padx=5, pady=5)

        resetBtn = ttk.Button(parent, text="Reset", command=self.on_reset_click, width=5)
        resetBtn.grid(row=0, column=4, padx=5, pady=5)

        retryBtn = ttk.Button(parent, text="Re-Try", command=self.on_retry_click, width=5)
        retryBtn.grid(row=0, column=5, padx=5, pady=5)

        #slider
        self.build_slider(parent)

    def build_slider(self,parent):
        self.slTxt = tk.Label(parent,text=str(self.sliderValue.get()))
        self.slTxt.grid(row=1,column=0)

        def changeSliderValue(v):
            self.slTxt = tk.Label(parent,text=str(self.sliderValue.get()))
            self.slTxt.grid(row=1,column=0)
        
        slider = ttk.Scale(parent, from_=ARRAY_LENGTH_MIN_LIMIT, to=ARRAY_LENGTH_MAX_LIMIT, orient=tk.HORIZONTAL,variable=self.sliderValue,command=changeSliderValue)
        slider.grid(row=1, column=1, columnspan=4,  sticky=tk.W+tk.E)


    def initialize_array(self):
        # self.array = ran.sample((ARRAY_MIN_VALUE,ARRAY_MAX_VALUE),self.sliderValue.get())
        self.array = [ran.randrange(ARRAY_MIN_VALUE, ARRAY_MAX_VALUE) for i in range(self.sliderValue.get())]
        self.length = len(self.array)
        self.max =  max(self.array)
        self.w = self.canvas_width/self.length
        self.h = self.canvas_height/self.max

        # storing backup
        self.orgSliderVal = self.sliderValue.get()
        self.orgArray = self.array[:]

    def drawArray(self):
        print('draw')
        self.canvas.delete('all')

        for i in range(self.length):
            x1, x2 = self.w * i, self.w * (i+1)
            y1, y2 = 0, self.h * self.array[i]

            self.canvas.create_rectangle(x1,y1,x2,y2,fill=RECT_COLOR)


    def on_back_click(self):
        self.navigator.showPage("home")

    def on_start_click(self):
        """point of start for algorithm"""
        pass

    def on_reset_click(self):
        """Resets value of array to unsorted"""
        self.array = self.orgArray
        self.sliderValue.set(self.orgSliderVal)
        self.drawArray()

    def on_retry_click(self):
        """Creates new random array"""
        self.initialize_array()
        self.drawArray()
    def stopSorting(self):
        # Reset the array to its original state to stop sorting
        self.array = self.original_array.copy()
        self.drawArray()
        
