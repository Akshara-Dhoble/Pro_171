# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:08:04 2023

@author: Akshara Sagar Dhoble
"""

from tkinter import *
from PIL import ImageTk , Image
from datetime import datetime
import pytz 
import time

root = Tk()
root.title("Time")
root.geometry("600x600")

ind_img = ImageTk.PhotoImage(Image.open("india.jpg"))
usa_img = ImageTk.PhotoImage(Image.open("usa.jpg"))
japan_img = ImageTk.PhotoImage(Image.open("japan.jpg"))
australia_img = ImageTk.PhotoImage(Image.open("australia.jpg"))

root.mainloop()