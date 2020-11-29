import re

pattern = re.compile("([A-Z][0-9]+), \[\s?([0-9]+)\s?\]")

file = open(f"test.out", "r")
data = file.read()
file.close()
result = pattern.findall(data)
len_attributes = len(result)
x = [0] * (len_attributes // 4)
y = [0] * (len_attributes // 4)
w = [0] * (len_attributes // 4)
h = [0] * (len_attributes // 4)

for i in range(len_attributes):
	if result[i][0][0] == "X":
		x[int(result[i][0][1:])] = int(result[i][1])
	if result[i][0][0] == "Y":
		y[int(result[i][0][1:])] = int(result[i][1])
	if result[i][0][0] == "L":
		w[int(result[i][0][1:])] = int(result[i][1])
	if result[i][0][0] == "H":
		h[int(result[i][0][1:])] = int(result[i][1])

rect_file = open(f"rect.in", "a")
for i in range(len_attributes // 4):
	rect_file.write(str(x[i])+","+str(y[i])+","+str(w[i])+","+str(h[i])+"\n")
