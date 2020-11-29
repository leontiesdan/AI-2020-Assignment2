import csv
import random 
import math

n = 10
width = 6
height = 4

with open('data_problem.txt', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow([n])
    data_writer.writerow([width,height])
    for i in range (n):
        data_writer.writerow([random.randint(1, int(math.sqrt(width))), 
                                  random.randint(1, int(math.sqrt(height)))])