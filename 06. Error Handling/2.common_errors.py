try:
    # contoh error pembagian dengan nol
    hasil = 10 / 0

# menangkap error khusus pembagian nol
except ZeroDivisionError:
    print("Terjadi error: tidak bisa membagi dengan nol")
