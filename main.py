import random

def tahmin_oyunu():
    sayi = random.randint(0, 100)
    puan = 100
    tahmin_hakki = 10

    while tahmin_hakki > 0:
        print("\nKalan tahmin hakkınız: " + str(tahmin_hakki))
        try:
            tahmin = int(input("0 ile 100 arasında bir sayı tahmin edin: "))
        except ValueError:
            input("Hata: Lütfen sadece sayı girin.")
            exit()

        if tahmin == sayi:
            print("Tebrikler " + str(sayi) + " sayısını doğru tahmin ettiniz.")
            input("Oyunu bitirdiğiniz puanınız: " + str(puan))
            break

        if tahmin > 100:
            puan -= 20
            tahmin_hakki -= 1
            print('1-100 arasında bir sayı girin, -20 puan alındı')
            print("Puanınız: " + str(puan))
            continue

        if tahmin < 0:
            puan -= 20
            tahmin_hakki -= 1
            print('1-100 arasında bir sayı girin, -20 puan alındı')
            print("Puanınız: " + str(puan))
            continue

        elif tahmin > sayi:
            puan -= 10
            print("Daha küçük bir sayı tahmin edin.")
            print("Puanınız: " + str(puan))

        elif tahmin < sayi:
            puan -= 10
            print("Daha büyük bir sayı tahmin edin.")
            print("Puanınız: " + str(puan))
        tahmin_hakki -= 1

        if tahmin_hakki == 0:
            print("\nTahmin hakkınız kalmadı. Doğru cevap: " + str(sayi))
            input("Oyunu kaybettiniz.")


tahmin_oyunu()