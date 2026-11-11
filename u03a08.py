# Kullanıcıdan kelime alıp büyük harfe çeviriyoruz
user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    # Sesli harfleri kontrol edip continue ile atlıyoruz
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        # Sessiz harfleri ekrana yazdırıyoruz
        print(letter)
