import time

# 1'den 5'e kadar (5 dahil) döngü kuruyoruz
for i in range(1, 6):
    print(i, "Mississippi")
    # Kodun akışını simüle etmek için kısa bir bekleme (isteğe bağlıdır ama orijinal ödevde zaman fonksiyonu kullanılır)
    time.sleep(1)

# Döngü bittiğinde yazdırılacak metin
print("Ready or not, here I come!")
