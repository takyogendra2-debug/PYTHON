#countdown timer program
import time
my_time = int(input("enter the time in seconds:"))
for x in range(my_time, 0 ,-1):
    secands = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) 
    print(f"{hours:02}:{minutes:02}:{secands:02}")
    print(x)
    time.sleep(1)