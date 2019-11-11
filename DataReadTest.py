import datetime
from datetime import datetime


testDay = []
testHour = []
testMinute = []


d = datetime.today()
t = d.timetuple()

f = open("timedata.txt", "w")

f.write(str(t[2]))
f.write("\n")
f.write(str(t[3]))
f.write("\n")
f.write(str(t[4]))
f.write("\n")
f.close

f = open("timedata.txt", 'r')
temp = f.read().splitlines()
testDay = testDay + temp
testDay = list(map(int, testDay))
print (testDay)
i = 0
for x in testDay:
    i = i + 1
print(i)
f.close()
print(int((13 / 5)))
