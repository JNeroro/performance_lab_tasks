import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

f1 = open(file1, 'r')
line = f1.readline()
line = line.split()
x_c, y_c = float(line[0].strip()), float(line[1].strip())
radius = float(f1.readline().strip())
f1.close()

f2 = open(file2, 'r')

for line in f2.readlines():
	line = line.strip()
	line = line.split()
	x,y = float(line[0]), float(line[1])
	res = (x-x_c)**(2) + (y-y_c)**(2)
	if res == radius**(2):
		print(0)
	elif res > radius**(2):
		print(2)
	else:
		print(1)

f2.close()
