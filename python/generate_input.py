bigW = 4
bigH = 4
numRectangles = 2
w = [2, 2, 2, 2]
h = [3, 3, 3, 3]
file = open(f"test.in", "w")
file.write(f"""assign(domain_size, {max(bigW, bigH)}).
assign(max_models, -1).
set(arithmetic).

formulas(rectangles).
""")
for i in range(numRectangles):
	file.write(f"""
	r{i}h <-> (L{i} = {w[i]} & H{i} = {h[i]}).
	r{i}v <-> (L{i} = {h[i]} & H{i} = {w[i]}).
	-(r{i}h -> r{i}v) | -(r{i}v -> r{i}h).
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
	for j in range(i, numRectangles):
		if i != j:
			file.write(f"""
	X{i} + L{i} <= X{j} | X{j} + L{j} <= X{i} | Y{i} + H{i} <= Y{j} | Y{j} + H{j} <= Y{i}.
""")
file.write(f"""
end_of_list.
""")
