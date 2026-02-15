try:
    # meminta input angka dari user
    angka = int(input("Masukkan angka: "))
    
    # menampilkan angka jika berhasil
    print("Angka yang dimasukkan:", angka)

# menangkap error jika input bukan angka
except ValueError:
    print("Input harus berupa angka")
