#!/usr/bin/python3
import time
import sys

def memoize(f):
        """Memoize decorator for functions taking one or more arguemtns"""
        class memodict(dict):
                def __init__(self, f):
                        self.f = f
                def __call__(self, *args):
                        return self[args]
                def __missing__(self, key):
                        ret = self[key] = self.f(*key)
                        return ret
        return memodict(f)


# this doesn't work because of stuff on this page (not really a python bug) http://bugs.python.org/issue7296
# sys.setrecursionlimit(sys.maxint)	
sys.setrecursionlimit(999999999)

# not the best way to count the calls but it works
# i got it from MAK's answer in this post: http://stackoverflow.com/questions/5441244/counting-recursion-in-a-python-program
counter = [0]

@memoize
def ackermann(m, n):
	counter[0] += 1
	if(m == 0):
		ans = n + 1
	elif(n == 0):
		ans = ackermann(m-1, 1)
	else:
		ans = ackermann(m-1, ackermann(m, n-1))
	return ans

file = open("Ackermann-results.txt", "w")
file2 = open("Ackermann-data.csv", "w")
file.write("The Ackermann function: We know it should always end but we know it never will...\n")
file2.write("m,n,ans,time(seconds),# of calls\n")
for i in range(0, 3):
	for j in range(0, 10):
		counter[0] = 0
		start_time = time.time()
		temp = ackermann(i, j)
		tot_time = time.time() - start_time
		file.write("ackermann("+str(i)+", "+str(j)+") = " + str(temp))
		file.write(" and took "+ str(tot_time) + " seconds to compute with " + str(counter[0]) + " function calls.")
		file.write("\n")
		
		file2.write(str(i) + "," + str(j) + "," + str(temp) + "," + str(tot_time) + "," + str(counter[0]) + "\n")

file.close()
file2.close()
