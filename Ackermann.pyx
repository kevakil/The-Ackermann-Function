#!/usr/bin/python3
import time


def memoize(func):
    memo = {}
    counter = 0

    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return wrapper


cdef count_calls(func):
    counter = 0

    def wrapper(*args):
        nonlocal counter
        counter += 1
        return func(*args), counter
    return wrapper


@count_calls
@memoize
def ackermann(int m, int n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m-1, 1)[0]
    if m > 0 and n > 0:
        return ackermann(m-1, ackermann(m, n-1)[0])[0]


result = open("Ackermann-results.txt", "w")
data = open("Ackermann-data.csv", "w")
result.write("The Ackermann function: We know it should always end \
              but we know it never will...\n")
data.write("m,n,ans,time(seconds),# of calls\n")

for i in range(0, 3):
    for j in range(0, 10):
        tot_time = time.time()
        temp, counter = ackermann(i, j)
        tot_time -= time.time()
        result.write(f"ackermann({i}, {j}) = {temp} and \
                took {tot_time} seconds to compute \
                with {counter} function calls\n")

        data.write(str(i) + "," + str(j) + "," + str(temp) + "," +
                   str(tot_time) + "," + str(counter) + "\n")

result.close()
data.close()
