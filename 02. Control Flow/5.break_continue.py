angka_rahasia = 7

while True:
    tebakan = int(input("Tebak angka: "))

    if tebakan == angka_rahasia:
        print("Benar!")
        break
    else:
        print("Coba lagi")
