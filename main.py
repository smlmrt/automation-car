print("Sshell benzin istasyonumuza hoşgeldiniz.")
print("Aşağıda işlemlerden birinisini seçiniz."
      "\n[1]-Yakıt alma"
      "\n[2]-Araç yıkama"
      "\n[3]-Teker hava basıncı ayarlama"
      "\n[4]-Çıkış")
islem = int(input("İşleminiz:"))

def kursunsuz_fiyat(litre, fiyat = 14.06):
      result = litre * fiyat
      print(f'fiyatı:{result} tl')
def motorin_fiyat(litre, fiyat = 14.3):
      result = litre * fiyat
      print(f'fiyatı: {result} tl')
def fuel_fiyat(litre, fiyat = 11.15):
      result = litre * fiyat
      print(f'fiyatı:{result} tl')

def kalanKursunsuz(litre,kursunsuz_benzin = 500):
      result = kursunsuz_benzin - litre
      print(f'Benzin istasyonunda kalan yakit miktari: {result} litre')
def kalanMotorin(litre,motorin_benzin = 300):
      result = motorin_benzin - litre
      print(f'Benzin istasyonunda kalan yakit miktari: {result} litre')
def kalanFuel(litre,fuel_benzin = 100):
      result = fuel_benzin - litre
      print(f'Benzin istasyonunda kalan yakıt miktarı: {result} litre')

while 1:
      if(islem == 1):
            print("Araç plakasını giriniz:")
            input("plaka:")
            print("Hangi yakıttan almak istersiniz? \n[1]-Kurşunsuz Benzin 95 \n[2]-Motorin \n[3]-Fuel Oil")
            input("Bir işlem seçiniz:")
            yakıtSecimi = int(input("Bir işlem seçiniz:"))
            if yakıtSecimi == 1:
                  print("Kaç litre satın almak istersiniz?")
                  litre = int(input("litre:"))
                  kursunsuz_fiyat(litre,fiyat = 14.06)
                  kalanKursunsuz(litre,kursunsuz_benzin = 500)
                  break
            elif yakıtSecimi == 2:
                  print("Kaç litre satın almak istersiniz?")
                  litre = int(input("litre:"))
                  motorin_fiyat(litre,fiyat=14.3)
                  kalanMotorin(litre,motorin_benzin=300)
                  break
            elif yakıtSecimi == 3:
                  print("Kaç litre satın almak istersiniz?")
                  litre = int(input("litre:"))
                  fuel_fiyat(litre,fiyat=11.15)
                  kalanFuel(litre,fuel_benzin=100)
                  break
            else:
                  print("yanlış bir işlem yaptınız...")
                  break

      elif islem == 2:
            print("Araç plakasını giriniz:")
            input("plaka:")
            print("Araç yıkama ücretiniz 10 tl. ")
            break
      elif islem == 3:
            print("Araç plakasını giriniz:")
            input("plaka:")
            print("Araçlarda ön teker için hava basıncı 34 Arka teker iiçn ise 38 olmalıdır.")
            print("işlem ücretiniz 20 tl")
            break
      elif islem == 4:
            print("Çıkış işlemi için herhangi bir tuşa basınız.")
            str(input("Çıkış:"))
            print("Bizleri tercih ettiğiniz için teşekkür ederiz.")
            break
      else:
            print("yanlış bir işlem yaptınız...")
            break