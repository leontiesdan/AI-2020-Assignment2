import csv
import random 
import math

n = 5
width = 640
height = 480

with open('data.txt', mode='w', newline='') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(['width','height'])
    for i in range (n):
        data_writer.writerow([random.randint(1, int(math.sqrt(width))), 
                                  random.randint(1, int(math.sqrt(height)))])