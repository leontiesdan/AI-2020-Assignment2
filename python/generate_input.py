import csv
bigW = 3
bigH = 3
numRectangles = 3
w = [3, 2, 1]
h = [1, 1, 1]

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
			w.append(int(row[0]))
			h.append(int(row[1]))
		line_count+=1

file = open("test.in", "w")
file.write(f"""assign(domain_size, {max(bigW, bigH)+1}).
assign(max_models, 1).
set(arithmetic).

formulas(rectangles).
""")
for i in range(numRectangles):
	file.write(f"""
	R{i}v <-> (L{i} = {h[i]} & H{i} = {w[i]}).
	R{i}h <-> (L{i} = {w[i]} & H{i} = {h[i]}).
 	(L{i} != H{i}) -> (-(R{i}v -> R{i}h) | -(R{i}h -> R{i}v)).
 	(L{i} = H{i}) -> R{i}v.	
 		""")

file.write(f"""
end_of_list.

formulas(bounds).
""")
for i in range(numRectangles):
	file.write(f"""
	Y{i} >= 0 & (Y{i} + H{i} <= {bigH}).
	X{i} >= 0 & (X{i} + L{i} <= {bigW}).
	""")
file.write(f"""
end_of_list.

formulas(intersections).
""")
for i in range(numRectangles):
	for j in range(i, numRectangles):
		if i != j:
			file.write(f"""
	(X{i} + L{i} <= X{j}) | (X{j} + L{j} <= X{i}) | (Y{i} + H{i} <= Y{j}) |(Y{j} + H{j} <= Y{i}).
""")
file.write(f"""
end_of_list.
""")
