import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

s = 0
st = ''
while s != n:
	st = st + str(s+1)
	s = s + (m - 1)
	if s > n:
		s = s - n
		
print(st)
