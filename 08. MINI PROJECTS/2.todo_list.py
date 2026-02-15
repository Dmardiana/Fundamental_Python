# list untuk menyimpan tugas
todo = []

while True:
    # input tugas
    tugas = input("Masukkan tugas (ketik 'exit' untuk keluar): ")

    # jika exit maka berhenti
    if tugas == "exit":
        break

    # simpan tugas
    todo.append(tugas)

# tampilkan semua tugas
print("Daftar tugas:", todo)
