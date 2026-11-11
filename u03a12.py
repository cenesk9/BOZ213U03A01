hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Adım 1: Ortadaki sayıyı (indeks 2) kullanıcıdan alınan yeni bir tamsayı ile değiştiriyoruz
hat_list[2] = int(input("Enter an integer number to replace the middle number: "))

# Adım 2: Listenin son öğesini listeden kaldırıyoruz
del hat_list[-1]
# veya: hat_list.pop()

# Adım 3: Mevcut listenin uzunluğunu yazdırıyoruz
print("The length of the list:", len(hat_list))

print(hat_list)
