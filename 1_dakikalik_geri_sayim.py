import time
x = 61
while x <= 61:
    x -= 1
    if x == 0:
        print("Süre doldu")
        time.sleep(30)
        break
    print(x)
    time.sleep(1)

