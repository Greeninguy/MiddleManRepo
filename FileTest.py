import datetime
from datetime import datetime
import os

lis = []
f = open("timedata.txt", r)

lis = f.read().splitlines()
f.close()
lis = list(map(int, lis))
for x in lis:
    print(x)
