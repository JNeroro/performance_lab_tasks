import sys

file1 = sys.argv[1]
file2 = sys.argv[2]


def func(idd):
	value = 0
	f2 = open(file2, 'r')
	line = f2.readline()
	while line:
		data = line.split(':')
		if (data[0].strip() == '"id"') and (data[1].strip() == idd):
			line = f2.readline()
			line = line.strip()
			data = line.split()
			value = data[1]
			line = f2.readline()
		else:
			line = f2.readline()

	f2.close()
#	print(value)
	return value

value = 0

f1 = open(file1, 'r')
f3 = open('report.json', 'w')

line = f1.readline()
while line:
	if value != 0:
		data = line.split(':')
		d = data[0].strip()
		if d == '"value"':
			data[1] = value
			value = 0
			line = data[0] + ": " + data[1] + '\n'
			f3.write(line)
			line = f1.readline()
	data = line.split(':')
	d = data[0].strip()
	if d == '"id"':
		value = func(data[1].strip())
		f3.write(line)
		line = f1.readline()
	else:
		f3.write(line)
		line = f1.readline()
	
f1.close()
