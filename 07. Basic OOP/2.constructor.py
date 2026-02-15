# class dengan constructor
class Mobil:
    def __init__(self, merk):
        # atribut objek
        self.merk = merk

# membuat objek dengan parameter
m1 = Mobil("Toyota")

# menampilkan merk mobil
print(m1.merk)
