secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number and    |
| guess what number I've         |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Kullanıcıdan ilk tahmini alıyoruz
guess = int(input("Enter an integer number: "))

# Doğru tahmin edilene kadar dönecek while döngüsü
while guess != secret_number:
    print("Ha, ha! You're stuck in my loop!")
    guess = int(input("Enter an integer number: "))

# Döngü bittiğinde (yani doğru tahmin edildiğinde) buraya düşer
print("Well done, muggle! You are free now.")
