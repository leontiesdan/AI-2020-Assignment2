import csv
import random
from tkinter import *

tile = 100
canv_width = 8
canv_height = 4

with open('rect.in') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader :
        if line_count == 1: 
            canv_width = int(row[2])
            canv_height = int(row[3])
            line_count += 1
        else:
            line_count += 1
        

master = Tk()
c = Canvas(master, width=canv_width*tile, height=canv_height*tile)
c.pack()


with open('rect.in') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader :
        if line_count > 1: 
            de=("%02x"%random.randint(0,255))
            re=("%02x"%random.randint(0,255))
            we=("%02x"%random.randint(0,255))
            ge="#"
            color=ge+de+re+we
            c.create_rectangle(int(row[0])*tile, int(row[1])*tile, int(row[0])*tile+int(row[2])*tile, int(row[1])*tile+int(row[3])*tile, fill=color)
            line_count += 1
        else:
            line_count += 1

mainloop()
