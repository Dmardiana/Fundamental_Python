# ==============================
# FINAL PROJECT PYTHON FUNDAMENTAL
# Sistem Manajemen Mahasiswa
# ==============================


# ---------- OOP ----------
# class untuk merepresentasikan Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nilai):
        # atribut objek
        self.nama = nama
        self.nilai = nilai

    # method untuk menentukan status kelulusan
    def status(self):
        if self.nilai >= 75:
            return "Lulus"
        else:
            return "Tidak Lulus"


# ---------- FUNCTION ----------
# function untuk menghitung rata-rata nilai
def hitung_rata(data):
    total = 0
    for m in data:
        total += m.nilai
    return total / len(data)


# ---------- LOGIN SYSTEM ----------
print("=== LOGIN SISTEM ===")

username_benar = "admin"
password_benar = "123"

username = input("Username: ")
password = input("Password: ")

# control flow untuk validasi login
if username != username_benar or password != password_benar:
    print("Login gagal. Program berhenti.")
    exit()

print("\nLogin berhasil!\n")


# ---------- DATA STRUCTURE ----------
# list untuk menyimpan objek mahasiswa
data_mahasiswa = []

try:
    jumlah = int(input("Masukkan jumlah mahasiswa: "))

    # loop input data
    for i in range(jumlah):
        print(f"\nData mahasiswa ke-{i+1}")

        # string input
        nama = input("Nama: ")

        # type casting ke integer
        nilai = int(input("Nilai: "))

        # membuat objek mahasiswa
        mhs = Mahasiswa(nama, nilai)

        # simpan ke list
        data_mahasiswa.append(mhs)

except ValueError:
    print("Input harus angka.")
    exit()


# ---------- OUTPUT DATA ----------
print("\n=== DATA MAHASISWA ===")

for m in data_mahasiswa:
    print(f"Nama: {m.nama} | Nilai: {m.nilai} | Status: {m.status()}")


# ---------- PERHITUNGAN ----------
rata = hitung_rata(data_mahasiswa)

print("\nRata-rata nilai:", rata)


# mencari nilai tertinggi
nilai_tertinggi = max(data_mahasiswa, key=lambda x: x.nilai)

print("Nilai tertinggi:", nilai_tertinggi.nama, "-", nilai_tertinggi.nilai)


# ---------- STRING HANDLING ----------
print("\n=== LAPORAN ===")

pesan = f"Total mahasiswa: {len(data_mahasiswa)}"
print(pesan.upper())  # ubah jadi huruf besar


print("\nProgram selesai. Terima kasih!")
