blocks = int(input("Enter the number of blocks: "))

height = 0
in_layer = 1

# Elimizdeki blok sayısı, yeni kat için gereken blok sayısından büyük veya eşit olduğu sürece devam et
while blocks >= in_layer:
    blocks -= in_layer
    height += 1
    in_layer += 1

print("The height of the pyramid:", height)
