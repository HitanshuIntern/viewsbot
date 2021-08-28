import tkinter as tk
from selenium import webdriver
from time import sleep
import random
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def bot ():  
    x1 = entry1.get()
    
    while True:
        driver1 = webdriver.Chrome(executable_path="chromedriver")
        driver2 = webdriver.Chrome(executable_path="chromedriver")
        driver3 = webdriver.Chrome(executable_path="chromedriver")
        url = x1
        sleep(2)
        driver1.get(url)
        driver2.get(url)
        driver3.get(url)
        sleep(int(random.randrange(600, 900)))

        driver1.quit()
        driver2.quit()
        driver3.quit()
    
button1 = tk.Button(text='Submit', command=bot)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
