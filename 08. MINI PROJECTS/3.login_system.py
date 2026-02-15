# data login sederhana
username_benar = "admin"
password_benar = "123"

# input dari user
u = input("Username: ")
p = input("Password: ")

# pengecekan login
if u == username_benar and p == password_benar:
    print("Login berhasil")
else:
    print("Login gagal")
