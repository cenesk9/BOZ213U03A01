# Kullanıcıdan bir girdi alıyoruz
bitki = input("Bitki adını girin: ")

# Girdi tam olarak "Spathiphyllum" ise
if bitki == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")

# Girdi tamamen küçük harflerle "spathiphyllum" ise
elif bitki == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")

# Bunların dışındaki herhangi bir şey girildiyse
else:
    print("Spathiphyllum! Not " + bitki + "!")
