import csv
bigW = 4
bigH = 8
numRectangles = 4
w = [2, 2, 2, 2]
h = [3, 3, 3, 3]

with open('data_problem.txt') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader :
		if line_count == 0:
			numRectangles = int(row[0])
			w = [] 
			h = []
		elif line_count == 1: 
			bigW = int(row[0])
			bigH = int(row[1])
			with open('rect.in',"w") as rect_in: 
				rect_in.write("x0,y0,width,height\n")
				rect_in.write(",,"+row[0]+","+row[1]+"\n")
		else:
			print(line_count)
			w.append(int(row[0]))
			h.append(int(row[1]))
		line_count+=1

file = open("test.in", "w")
file.write(f"""assign(domain_size, {max(bigW, bigH)}).
assign(max_models, 1).
set(arithmetic).

formulas(rectangles).
""")
for i in range(numRectangles):
	file.write(f"""
	r{i}h <-> (L{i} = {w[i]} & H{i} = {h[i]}).
	r{i}v <-> (L{i} = {h[i]} & H{i} = {w[i]}).
	r{i}v | r{i}h.
	""")
file.write(f"""
end_of_list.

formulas(bounds).
""")
for i in range(numRectangles):
	file.write(f"""
	X{i} >= 0 & (X{i} + L{i} <= {bigW}).
	Y{i} >= 0 & (Y{i} + H{i} <= {bigH}).
	""")
file.write(f"""
end_of_list.

formulas(intersections).
""")
for i in range(numRectangles):
	for j in range(numRectangles):
		if i != j and j > i:
			file.write(f"""
	X{i} + L{i} <= X{j} | X{j} + L{j} <= X{i} | Y{i} + H{i} <= Y{j} | Y{j} + H{j} <= Y{i}.
""")
file.write(f"""
end_of_list.
""")
