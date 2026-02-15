# list untuk menyimpan data mahasiswa
data = []

# input data 2 mahasiswa
for i in range(2):
    nama = input("Nama: ")
    nilai = int(input("Nilai: "))
    
    # simpan dalam dictionary
    data.append({"nama": nama, "nilai": nilai})

# tampilkan data
print("Data mahasiswa:", data)
