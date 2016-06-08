import sys
import re

N = int(raw_input().strip())
names = []
for a0 in xrange(N):
    firstName,emailID = raw_input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if (re.findall('(@gmail.com)+', emailID) != []):
        names.append(firstName)

names.sort()
for i in names:
    print i