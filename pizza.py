kucukboy = 250
ortaboy = 400
buyukboy = 600
kucukpeynir = 80
digerpeynir = 160
icecekPara = 90
tutar = 0

pizza = input("Hangi Boy Pizza İstersiniz Küçük 'S' Orta 'M' Büyük boy için 'L' Seçiniz")

peynir = input("Fazladan Peynir İster Misiniz ? 'Evet' Veya 'Hayir.'")

icecek = input("İçecek İster Misiniz ? 'Evet' veya 'Hayir' ")

# print("Ato Babanın Pizzacısına Hoşgeldiniz")

if (pizza == "S"): 
    tutar += kucukboy
elif(pizza == "M"):
    tutar += ortaboy
elif(pizza == "L"):
    tutar += buyukboy

if(peynir == "Evet"):
    if(pizza == "S"):
        tutar += kucukpeynir
    else: 
        tutar+= digerpeynir
        if icecek == "Evet" :
            tutar += icecekPara

        print(f"Toplam Hesap {tutar} Tl Dir")



