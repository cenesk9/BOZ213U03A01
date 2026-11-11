my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Tekrarlayan elemanları temizlemek için boş bir liste oluşturalım
unique_list = []

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

# Orijinal değişkenimize (my_list) güncel benzersiz listeyi aktarıyoruz
my_list = unique_list

print("The list with unique elements only:")
print(my_list)
