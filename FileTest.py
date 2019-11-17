import datetime
from datetime import datetime
import os

x = [0, 0, 0]
f = open("LEDOnAuto.txt", 'w')
for i in x:
    f.write(str(i))
    f.write('\n')
f.close()

f = open("LEDOffAuto.txt", 'w')
for i in x:
    f.write(str(i))
    f.write('\n')
f.close()

f = open("LockAuto.txt", 'w')
for i in x:
    f.write(str(i))
    f.write('\n')
f.close()

f = open("UnlockAuto.txt", 'w')
for i in x:
    f.write(str(i))
    f.write('\n')
f.close()
