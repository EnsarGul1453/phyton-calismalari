import time
sayi = int(input("Pozitif bölen sayısını bulmak veya asal sayı bulmak için sayı giriniz: "))
sayi2 = abs(sayi)
sabit = 1
pozitif_bolen_sayisi = 0
while sabit <= sayi2:
   if sayi2 % sabit == 0:
      sabit += 1
      pozitif_bolen_sayisi += 1
   else:
      sabit += 1
if pozitif_bolen_sayisi == 2 and sayi > 0:
   print(f"{sayi} sayısı asal sayıdır.")
   time.sleep(30)
else:
   print(f"{sayi} sayisinin pozitif bolen sayisi {pozitif_bolen_sayisi} idir.")
   time.sleep(30)