import csv
import random
from tkinter import *

tile = 100
canv_width = 8
canv_height = 4

with open('data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader :
        if line_count == 1: 
            canv_width = row[2]
            canv_height = row[3]
            line_count += 1
        else:
            line_count += 1
        

master = Tk()
c = Canvas(master, width=canv_width*tile, height=canv_height*tile)
c.pack()


with open('data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader :
        if line_count > 1: 
            de=("%02x"%random.randint(0,255))
            re=("%02x"%random.randint(0,255))
            we=("%02x"%random.randint(0,255))
            ge="#"
            color=ge+de+re+we
            c.create_rectangle(row[0]*tile, row[1]*tile, row[0]*tile+row[2]*tile, row[1]*tile+row[3]*tile, fill=color)
            line_count += 1
        else:
            line_count += 1

mainloop()
