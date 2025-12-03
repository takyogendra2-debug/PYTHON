
#python compound interest claculator
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("enter the principal amount:"))
    if principle < 0:
        print("principal can't be less than zero")
    else:
        break
while True:
    rate = float(input("enter the interest rate:"))
    if rate < 0:
        print("inserest rate can't be less than  zero")
    else:
        break
while True:
    time = int(input("enter the time in years:"))
    if time < 0:
        print("time can't be less than  zero")
    else:
        break
total = principle * pow((1 + rate / 100), time)
print(f"the total amount after {time} year/s:${total:.2f}")