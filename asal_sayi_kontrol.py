import time
sayi = int(input("Asal kontrolü için sayı giriniz: "))
sabit = 1
while sabit <= sayi:
    if sabit == 1:
        sabit += 1
    if sabit == sayi:
        print("Bu sayı kesinlikle asaldır.")
        time.sleep(30)
        break
    if sayi % sabit == 0:
        print("Bu sayı kesinlikle asal değildir.")
        time.sleep(30)
        break
    else:
        sabit += 1
    if sayi == 1:
        print("Bu sayı kesinlikle asal değildir.")
        time.sleep(30)
        break