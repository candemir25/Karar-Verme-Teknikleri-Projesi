import math

liste1 = []
liste2 = []
liste3 = []
x1 = []
y1 = []
a = 0
istenen_satir_olcutleri = int(input("İstenen satır sayısı:"))
istenen_sutun_olcutleri = int(input("İstenen sutun sayısı:"))

for i in range (istenen_satir_olcutleri):

    veri = str(input("Satır ölçütü giriniz:"))
    liste1 = liste1 + [veri]
    
    i = i+1

for i in range (istenen_sutun_olcutleri):

    veri_2 = str(input("Sütün ölçütü giriniz:"))
    liste2 = liste2 +[veri_2]

    i += 1

for i in range (istenen_satir_olcutleri*istenen_sutun_olcutleri):
    veri_3 = int(input("Satır değerlerini giriniz:"))
    liste3 = liste3 + [veri_3]

    i += 1

if(istenen_satir_olcutleri == 3 and istenen_sutun_olcutleri == 2):

    b = 0
    c = 2

    for i in range (istenen_satir_olcutleri):

        x1 = x1 + [liste1[a],liste3[b:c]]

        a += 1
        b = b + len(liste1)-1
        c = c + len(liste2)
        i += 1

elif((istenen_satir_olcutleri == 2 and istenen_sutun_olcutleri == 2) or (istenen_satir_olcutleri == 3 and istenen_sutun_olcutleri == 3)):
    b = 0
    c = len(liste1)
    for i in range (istenen_satir_olcutleri):
        x1 = x1 + [liste1[a],liste3[b:c]]

        a += 1
        b = b + len(liste1)
        c = c + len(liste1)
        i += 1

if(a!=0):
    a = 0
    b = 0

if(istenen_satir_olcutleri == 2 and istenen_sutun_olcutleri == 3):

    b = 0
    c = 3
    for i in range (istenen_satir_olcutleri):
        x1 = x1 + [liste1[a],liste3[b:c]]

        a += 1
        b = b + 3
        c = c + 3
        i += 1

if(a!=0):
    a = 0
    b = 0

for i in range (istenen_sutun_olcutleri):
    y1 = y1 + [liste2[a],liste3[b:len(liste3):istenen_sutun_olcutleri]]

    a += 1
    b = b + 1
    i += 1

if(a!=0):
    a = 0
    b = 0

sayac = 1
x1_maksimum_degerleri = []

kontrol = int(input("Tablonuz getiri yapılı ise 1 maliyet yapılı ise 2 yazınız:"))
alfa_katsayisi = float(input("Uzlaştırma ölçütü için alfa katsayısı belirleyiniz (0 ile 1 arasında bir değer giriniz):"))

class iyimserlik_olcutu:

    if(kontrol == 1):

        if(istenen_satir_olcutleri == 2 and istenen_sutun_olcutleri == 2):
            
            for i in range (2):
                x1_maksimum_degerleri.append(max(x1[sayac]))
                sayac += 2
            
            maximax = max(x1_maksimum_degerleri)

            if(maximax == x1[3][1] or maximax == x1[3][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[2])

            elif(maximax == x1[1][1] or maximax == x1[1][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[0])

        if(istenen_satir_olcutleri == 3 and istenen_sutun_olcutleri == 2):

            for i in range (3):
                x1_maksimum_degerleri.append(max(x1[sayac]))
                sayac += 2
            
            maximax = max(x1_maksimum_degerleri)

            if(maximax == x1[5][1] or maximax == x1[5][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[4])

            elif(maximax == x1[3][1] or maximax == x1[3][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[2])
            
            elif(maximax == x1[1][1] or maximax == x1[1][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[0])

        if(istenen_satir_olcutleri == 3 and istenen_sutun_olcutleri == 3):

            for i in range (3):
                x1_maksimum_degerleri.append(max(x1[sayac]))
                sayac += 2
            
            maximax = max(x1_maksimum_degerleri)

            if(maximax == x1[5][2] or maximax == x1[5][1] or maximax == x1[5][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[4])

            elif(maximax == x1[3][2] or maximax == x1[3][1] or maximax == x1[3][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[2])

            elif(maximax == x1[1][2] or maximax == x1[1][1] or maximax == x1[1][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[0])

    if(kontrol == 2):

        if(istenen_satir_olcutleri == 2 and istenen_sutun_olcutleri == 2):

            for i in range (2):
                x1_maksimum_degerleri.append(min(x1[sayac]))
                sayac += 2
            
            maximax = min(x1_maksimum_degerleri)

            if(maximax == x1[3][1] or maximax == x1[3][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[2])

            elif(maximax == x1[1][1] or maximax == x1[1][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[0])

        if(istenen_satir_olcutleri == 3 and istenen_sutun_olcutleri == 2):

            for i in range (3):
                x1_maksimum_degerleri.append(min(x1[sayac]))
                sayac += 2
            
            maximax = min(x1_maksimum_degerleri)

            if(maximax == x1[5][1] or maximax == x1[5][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[4])

            elif(maximax == x1[3][1] or maximax == x1[3][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[2])
            
            elif(maximax == x1[1][1] or maximax == x1[1][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[0])

        if(istenen_satir_olcutleri == 3 and istenen_sutun_olcutleri == 3):

            for i in range (3):
                x1_maksimum_degerleri.append(min(x1[sayac]))
                sayac += 2
            
            maximax = min(x1_maksimum_degerleri)

            if(maximax == x1[5][2] or maximax == x1[5][1] or maximax == x1[5][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[4])

            elif(maximax == x1[3][2] or maximax == x1[3][1] or maximax == x1[3][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[2])

            elif(maximax == x1[1][2] or maximax == x1[1][1] or maximax == x1[1][0]):
                print("İyimserlik ölçütüne göre hedefiniz:", x1[0])

class kotumserlik_olcutu:

    if(kontrol == 1):

        if(istenen_satir_olcutleri == 2 and istenen_sutun_olcutleri == 2):

            for i in range (2):
                x1_maksimum_degerleri.append(max(x1[sayac]))
                sayac += 2
            
            maximax = min(x1_maksimum_degerleri)

            if(maximax == x1[3][1] or maximax == x1[3][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[2])

            elif(maximax == x1[1][1] or maximax == x1[1][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[0])

        if(istenen_satir_olcutleri == 3 and istenen_sutun_olcutleri == 2):

            for i in range (3):
                x1_maksimum_degerleri.append(max(x1[sayac]))
                sayac += 2
            
            maximax = min(x1_maksimum_degerleri)

            if(maximax == x1[5][1] or maximax == x1[5][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[4])

            elif(maximax == x1[3][1] or maximax == x1[3][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[2])
            
            elif(maximax == x1[1][1] or maximax == x1[1][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[0])

        if(istenen_satir_olcutleri == 3 and istenen_sutun_olcutleri == 3):

            for i in range (3):
                x1_maksimum_degerleri.append(max(x1[sayac]))
                sayac += 2
            
            maximax = min(x1_maksimum_degerleri)

            if(maximax == x1[5][2] or maximax == x1[5][1] or maximax == x1[5][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[4])

            elif(maximax == x1[3][2] or maximax == x1[3][1] or maximax == x1[3][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[2])

            elif(maximax == x1[1][2] or maximax == x1[1][1] or maximax == x1[1][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[0])

    if(kontrol == 2):

        if(istenen_satir_olcutleri == 2 and istenen_sutun_olcutleri == 2):

            for i in range (2):
                x1_maksimum_degerleri.append(min(x1[sayac]))
                sayac += 2
            
            maximax = max(x1_maksimum_degerleri)

            if(maximax == x1[3][1] or maximax == x1[3][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[2])

            elif(maximax == x1[1][1] or maximax == x1[1][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[0])

        if(istenen_satir_olcutleri == 3 and istenen_sutun_olcutleri == 2):

            for i in range (3):
                x1_maksimum_degerleri.append(min(x1[sayac]))
                sayac += 2
            
            maximax = max(x1_maksimum_degerleri)

            if(maximax == x1[5][1] or maximax == x1[5][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[4])

            elif(maximax == x1[3][1] or maximax == x1[3][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[2])
            
            elif(maximax == x1[1][1] or maximax == x1[1][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[0])

        if(istenen_satir_olcutleri == 3 and istenen_sutun_olcutleri == 3):

            for i in range (3):
                x1_maksimum_degerleri.append(min(x1[sayac]))
                sayac += 2
            
            maximax = max(x1_maksimum_degerleri)

            if(maximax == x1[5][2] or maximax == x1[5][1] or maximax == x1[5][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[4])

            elif(maximax == x1[3][2] or maximax == x1[3][1] or maximax == x1[3][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[2])

            elif(maximax == x1[1][2] or maximax == x1[1][1] or maximax == x1[1][0]):
                print("Kötümserlik ölçütüne göre hedefiniz:", x1[0])

class es_olasilik_olcutu():

    carpim_x1 = []
    carpim_x2 = []
    carpim_x3 = []

    if(istenen_sutun_olcutleri == 2):

        if(kontrol == 1):
            if(istenen_satir_olcutleri == 2):

                carpim_x1.append(x1[1][0] + x1[1][1])
                carpim_x2.append(x1[3][0] + x1[3][1])

                es_olasilik_toplam1 = sum(carpim_x1)/2
                es_olasilik_toplam2 = sum(carpim_x2)/2

                cikti = max(es_olasilik_toplam1,es_olasilik_toplam2)
                if(es_olasilik_toplam1 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[0],"sonuç",cikti)
                
                elif(es_olasilik_toplam2 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[2],"sonuç",cikti)
                
            elif(istenen_satir_olcutleri == 3):

                carpim_x1.append(x1[1][0] + x1[1][1])
                carpim_x2.append(x1[3][0] + x1[3][1])
                carpim_x3.append(x1[5][0] + x1[5][1])

                es_olasilik_toplam1 = sum(carpim_x1)/2
                es_olasilik_toplam2 = sum(carpim_x2)/2
                es_olasilik_toplam3 = sum(carpim_x3)/2

                cikti = max(es_olasilik_toplam1,es_olasilik_toplam2,es_olasilik_toplam3)
                if(es_olasilik_toplam1 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[0],"sonuç",cikti)

                elif(es_olasilik_toplam2 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[2],"sonuç",cikti)

                elif(es_olasilik_toplam3 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[4],"sonuç",cikti)
        
        if(kontrol == 2):
            if(istenen_satir_olcutleri == 2):

                carpim_x1.append(x1[1][0] + x1[1][1])
                carpim_x2.append(x1[3][0] + x1[3][1])

                es_olasilik_toplam1 = sum(carpim_x1)/2
                es_olasilik_toplam2 = sum(carpim_x2)/2

                cikti = min(es_olasilik_toplam1,es_olasilik_toplam2)
                if(es_olasilik_toplam1 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[0],"sonuç",cikti)
                
                elif(es_olasilik_toplam2 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[2],"sonuç",cikti)

            elif(istenen_satir_olcutleri == 3):

                carpim_x1.append(x1[1][0] + x1[1][1])
                carpim_x2.append(x1[3][0] + x1[3][1])
                carpim_x3.append(x1[5][0] + x1[5][1])

                es_olasilik_toplam1 = sum(carpim_x1)/2
                es_olasilik_toplam2 = sum(carpim_x2)/2
                es_olasilik_toplam3 = sum(carpim_x3)/2

                cikti = min(es_olasilik_toplam1,es_olasilik_toplam2,es_olasilik_toplam3)
                print("Eş olasılığa göre çıkan sonuç:",cikti)

    elif(istenen_sutun_olcutleri == 3):
        
        if(kontrol == 1):
            if(istenen_satir_olcutleri == 2):

                carpim_x1.append(x1[1][0] + x1[1][1] + x1[1][2])
                carpim_x2.append(x1[3][0] + x1[3][1] + x1[3][2])

                es_olasilik_toplam1 = sum(carpim_x1)/3
                es_olasilik_toplam2 = sum(carpim_x2)/3

                cikti = max(es_olasilik_toplam1,es_olasilik_toplam2)
                if(es_olasilik_toplam1 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[0],"sonuç",cikti)
                
                elif(es_olasilik_toplam2 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[2],"sonuç",cikti)

            elif(istenen_satir_olcutleri == 3):

                carpim_x1.append(x1[1][0] + x1[1][1] + x1[1][2])
                carpim_x2.append(x1[3][0] + x1[3][1] + x1[3][2])
                carpim_x3.append(x1[5][0] + x1[5][1] + x1[5][2])

                es_olasilik_toplam1 = sum(carpim_x1)/3
                es_olasilik_toplam2 = sum(carpim_x2)/3
                es_olasilik_toplam3 = sum(carpim_x3)/3

                cikti = max(es_olasilik_toplam1,es_olasilik_toplam2,es_olasilik_toplam3)
                if(es_olasilik_toplam1 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[0],"sonuç",cikti)

                elif(es_olasilik_toplam2 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[2],"sonuç",cikti)

                elif(es_olasilik_toplam3 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[4],"sonuç",cikti)
        
        if(kontrol == 2):
            if(istenen_satir_olcutleri == 2):

                carpim_x1.append(x1[1][0] + x1[1][1] + x1[1][2])
                carpim_x2.append(x1[3][0] + x1[3][1] + x1[3][2])

                es_olasilik_toplam1 = sum(carpim_x1)/3
                es_olasilik_toplam2 = sum(carpim_x2)/3

                cikti = min(es_olasilik_toplam1,es_olasilik_toplam2)
                if(es_olasilik_toplam1 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[0],"sonuç",cikti)
                
                elif(es_olasilik_toplam2 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[2],"sonuç",cikti)

            elif(istenen_satir_olcutleri == 3):

                carpim_x1.append(x1[1][0] + x1[1][1] + x1[1][2])
                carpim_x2.append(x1[3][0] + x1[3][1] + x1[3][2])
                carpim_x3.append(x1[5][0] + x1[5][1] + x1[5][2])

                es_olasilik_toplam1 = sum(carpim_x1)/3
                es_olasilik_toplam2 = sum(carpim_x2)/3
                es_olasilik_toplam3 = sum(carpim_x3)/3

                cikti = min(es_olasilik_toplam1,es_olasilik_toplam2,es_olasilik_toplam3)
                if(es_olasilik_toplam1 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[0],"sonuç",cikti)

                elif(es_olasilik_toplam2 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[2],"sonuç",cikti)

                elif(es_olasilik_toplam3 == cikti):
                    print("Eş olasılığa göre hedefiniz:",x1[4],"sonuç",cikti)

class uzlastirma_olcutu():

    buyuk_sayi = []
    kucuk_sayi = []
    a = 1

    if ((istenen_sutun_olcutleri == 2 and istenen_satir_olcutleri == 2) or (istenen_sutun_olcutleri == 3 and istenen_satir_olcutleri == 2)):
            
        for i in range(2):
            buyuk_sayi.append(max(x1[a]))
            kucuk_sayi.append(min(x1[a]))
            i += 1
            a += 2
            if(len(buyuk_sayi) == 2):
                a = 1
                break
            
        if(kontrol == 1):
            toplam_1 = (buyuk_sayi[0]*alfa_katsayisi) + (kucuk_sayi[0]*(1 - alfa_katsayisi))
            toplam_2 = (buyuk_sayi[1]*alfa_katsayisi) + (kucuk_sayi[1]*(1 - alfa_katsayisi))
        
            if(toplam_1 > toplam_2):       
                print("Uzlaştırma ölçütüne göre hedefiniz:",x1[0],"sonuç",toplam_1)

            else:           
                print("Uzlaştırma ölçütüne göre hedefiniz:",x1[2],"sonuç",toplam_2)

        elif (kontrol == 2):
            toplam_1 = (buyuk_sayi[0]*(1 - alfa_katsayisi)) + (kucuk_sayi[0]*alfa_katsayisi)
            toplam_2 = (buyuk_sayi[1]*(1 - alfa_katsayisi)) + (kucuk_sayi[1]*alfa_katsayisi)
        
            if(toplam_1 > toplam_2):       
                print("Uzlaştırma ölçütüne göre hedefiniz:",x1[0],"sonuç",toplam_2)

            else:           
                print("Uzlaştırma ölçütüne göre hedefiniz:",x1[2],"sonuç",toplam_1)

    elif ((istenen_sutun_olcutleri == 2 and istenen_satir_olcutleri == 3) or (istenen_sutun_olcutleri == 3 and istenen_satir_olcutleri == 3)):
            
        for i in range(3):
            buyuk_sayi.append(max(x1[a]))
            kucuk_sayi.append(min(x1[a]))
            i += 1
            a += 2
            if(len(buyuk_sayi) == 3):
                a = 1
                break

        if (kontrol == 1):
            toplam_1 = (buyuk_sayi[0]*alfa_katsayisi) + (kucuk_sayi[0]*(1 - alfa_katsayisi))
            toplam_2 = (buyuk_sayi[1]*alfa_katsayisi) + (kucuk_sayi[1]*(1 - alfa_katsayisi))
            toplam_3 = (buyuk_sayi[2]*alfa_katsayisi) + (kucuk_sayi[2]*(1 - alfa_katsayisi))

            yeni_liste = [toplam_1,toplam_2,toplam_3]

            if(max(yeni_liste) == toplam_1):       
                print("Uzlaştırma ölçütüne göre hedefiniz:",x1[0],"sonuç",toplam_1)

            elif(max(yeni_liste) == toplam_2):           
                print("Uzlaştırma ölçütüne göre hedefiniz:",x1[2],"sonuç",toplam_2)

            else:
                print("Uzlaştırma ölçütüne göre hedefiniz:",x1[4],"sonuç",toplam_3)

        elif (kontrol == 2):
            toplam_1 = (buyuk_sayi[0]*(1 - alfa_katsayisi)) + (kucuk_sayi[0]*alfa_katsayisi)
            toplam_2 = (buyuk_sayi[1]*(1 - alfa_katsayisi)) + (kucuk_sayi[1]*alfa_katsayisi)
            toplam_3 = (buyuk_sayi[2]*(1 - alfa_katsayisi)) + (kucuk_sayi[2]*alfa_katsayisi)

            yeni_liste = [toplam_1,toplam_2,toplam_3]

            if(min(yeni_liste) == toplam_1):       
                print("Uzlaştırma ölçütüne göre hedefiniz:",x1[0],"sonuç",toplam_1)

            elif(min(yeni_liste) == toplam_2):           
                print("Uzlaştırma ölçütüne göre hedefiniz:",x1[2],"sonuç",toplam_2)

            else:
                print("Uzlaştırma ölçütüne göre hedefiniz:",x1[4],"sonuç",toplam_3)

class pismanlik_olcutu:
    a = 1
    b = 0

    max_deger_1 = []
    pismanlik_tablosu_1 = []

    if(kontrol == 1):

        if((istenen_sutun_olcutleri == 2 and istenen_satir_olcutleri == 2) or (istenen_sutun_olcutleri == 2 and istenen_satir_olcutleri == 3)):

            c = 1

            for i in range(2):
                max_deger_1.append(max(y1[c]))
                i += 1
                c += 2
                if(len(max_deger_1) == 2):
                    c = 0

            for i in range (istenen_satir_olcutleri*2):
                
                pismanlik_tablosu_1.append(max_deger_1[c] - y1[a][b])
                i += 1
                b += 1
                if(b == istenen_satir_olcutleri):
                    a += 2
                    b = 0
                    c += 1             

            for i in range (2):
                pismanlik_tablosu_1.remove(0)

            print("Pişmanlık ölçütüne göre çıkan değer:",min(pismanlik_tablosu_1))

        if((istenen_sutun_olcutleri == 3 and istenen_satir_olcutleri == 2) or (istenen_sutun_olcutleri == 3 and istenen_satir_olcutleri == 3)):

            c = 1

            for i in range(3):
                max_deger_1.append(max(y1[c]))
                i += 1
                c += 2
                if(len(max_deger_1) == 3):
                    c = 0

            for i in range (istenen_satir_olcutleri*3):
                
                pismanlik_tablosu_1.append(max_deger_1[c] - y1[a][b])
                i += 1
                b += 1
                if(b == istenen_satir_olcutleri):
                    a += 2
                    b = 0
                    c += 1

            for i in range (3):
                pismanlik_tablosu_1.remove(0)

            print("Pişmanlık ölçütüne göre çıkan değer:",min(pismanlik_tablosu_1))

    if(kontrol == 2):

        if((istenen_sutun_olcutleri == 2 and istenen_satir_olcutleri == 2) or (istenen_sutun_olcutleri == 2 and istenen_satir_olcutleri == 3)):

            c = 1

            for i in range(2):
                max_deger_1.append(min(y1[c]))
                i += 1
                c += 2
                if(len(max_deger_1) == 2):
                    c = 0

            for i in range (istenen_satir_olcutleri*2):
                
                pismanlik_tablosu_1.append(max_deger_1[c] - y1[a][b])
                i += 1
                b += 1
                if(b == istenen_satir_olcutleri):
                    a += 2
                    b = 0
                    c += 1             

            for i in range (2):
                pismanlik_tablosu_1.remove(0)

            print("Pişmanlık ölçütüne göre çıkan değer:",abs(min(pismanlik_tablosu_1)))

        if((istenen_sutun_olcutleri == 3 and istenen_satir_olcutleri == 2) or (istenen_sutun_olcutleri == 3 and istenen_satir_olcutleri == 3)):

            c = 1

            for i in range(3):
                max_deger_1.append(min(y1[c]))
                i += 1
                c += 2
                if(len(max_deger_1) == 3):
                    c = 0

            for i in range (istenen_satir_olcutleri*3):
                
                pismanlik_tablosu_1.append(max_deger_1[c] - y1[a][b])
                i += 1
                b += 1
                if(b == istenen_satir_olcutleri):
                    a += 2
                    b = 0
                    c += 1

            for i in range (3):
                pismanlik_tablosu_1.remove(0)

            print("Pişmanlık ölçütüne göre çıkan değer:",abs(min(pismanlik_tablosu_1)))

input("Çıkış için herhangi bir tuşa basınız ")
exit
