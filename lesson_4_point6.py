from itertools import count
from itertools import cycle
from time import sleep


entered_number = int(input(f"Enter real number (should be > 0)"))
stop_number = int(input(f"Where we should stop? (should be > entered number"))

if stop_number<entered_number:
    print("No way, please try again")

for i in count(entered_number):
    if i > stop_number:
        break
    else:
        print(i)


cnt = 0
l = [3, 2, 1, 5, 8]
for x in cycle(l):
    print(x)
    sleep(0.5)
    cnt += 1
    if cnt == 15:
        break

