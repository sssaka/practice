import statistics
import math

s = input()
a = list(s.split(' '))
a_int = [int(s) for s in a]
print(statistics.median_high(a_int))
