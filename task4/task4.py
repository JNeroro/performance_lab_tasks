import sys
import math

file = sys.argv[1]

nums = []
sum = 0
result = 0

f = open(file, 'r')
for line in f.readlines():
	nums.append(float(line))
f.close()

for i in range(len(nums)):
	sum += nums[i]
avr = sum // len(nums)

for i in range(len(nums)):
	result += abs(nums[i] - avr)
	
print(int(result))
