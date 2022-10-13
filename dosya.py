file = open("litre.txt","r+",encoding="utf-8")
file.write("Depoda bulunan benzin oranları.\nKurşunsuz Benzin 95: 500 litre %50 doluluk.\nMotorin: 300 litre %30 doluluk.\nFuel Oil: 100 litre %10 doluluk.")

file.close()

file = open("fiyat.txt","r",encoding="utf-8")
file.write("Yakıt fiyat listesi:\nKurşunsuz Benzin 95: 14.06 TL/LT \nMotorin: 14.3 TL/LT \nFuel Oil: 11.15 TL/LT")

file.close()