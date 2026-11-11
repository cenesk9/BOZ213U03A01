# Adım 1: Boş bir beatles listesi oluşturuyoruz
beatles = []
print("Step 1:", beatles)

# Adım 2: append() ile ilk üç üyeyi ekliyoruz
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Adım 3: Kullanıcıdan yeni üyeleri (Stu Sutcliffe ve Pete Best) eklemesini istiyoruz veya doğrudan ekliyoruz
for i in range(2):
    new_member = input("Yeni grup üyesi girin (Stu Sutcliffe / Pete Best): ")
    beatles.append(new_member)
print("Step 3:", beatles)

# Adım 4: del komutu ile Stu Sutcliffe ve Pete Best'i listeden çıkarıyoruz
del beatles[-2]
del beatles[-1]
print("Step 4:", beatles)

# Adım 5: insert() ile listenin başına (0 numaralı indekse) Ringo Starr'ı ekliyoruz
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)
