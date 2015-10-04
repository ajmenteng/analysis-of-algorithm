"""
This script is used for finding the size of the smallest instance
where an algorithm with larger complexity that takes n**2 days 
can outperform an algorithm with smaller complexity (2**n).

Author: John Wesly (johncha@bu.edu)
"""

import time
import matplotlib.pyplot as plt

def days(n):
	# 1 day = 86400 sec
	return (n*86400) ** 2

def sec(n):
	return 2**n

def to_day(s):
	return s/86400

def to_year(s):
	return to_day(s)/365

n=1

a = [0]
b = [0]

start=time.time()
while sec(n)<days(n) or n<45:
	a.append(days(n))
	b.append(sec(n))
	n+=1

print("n = {} : days: {} years and sec: {} years" . format(n-1, to_year(days(n-1)), to_year(sec(n-1))))
print("n = {} : days: {} years and sec: {} years" . format(n, to_year(days(n)), to_year(sec(n))))

runtime=time.time()-start
print("Runtime: %s sec" % runtime)

time.sleep(0.05)

plt.plot(a, label='n**n days', linestyle='--')
plt.plot(b, label='2**n sec', marker='o')
plt.ylabel('Output')
plt.xlabel('n value')
plt.title('Algorithm Comparison')
plt.legend()
plt.show()