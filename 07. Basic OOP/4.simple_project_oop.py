# class Mahasiswa
class Mahasiswa:
    
    # constructor
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    # method menentukan status
    def status(self):
        if self.nilai >= 75:
            return "Lulus"
        return "Tidak Lulus"

# membuat objek
m = Mahasiswa("Budi", 80)

# menampilkan hasil
print(m.nama)
print(m.status())
