import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

sorted = True
swaps = 0
while (sorted):
    sorted = False
    for j in range(n - 1):
        if (a[j] > a[j + 1]):
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            swaps += 1
            sorted = True
print "Array is sorted in", swaps, "swaps."
print "First Element:", a[0]
print "Last Element:", a[len(a) - 1]