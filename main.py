nama_app = "Money Tracking App"
nama_user = input("Masukkan nama Anda: ")
mata_uang = "IDR"
saldo = 150000



print(f"Selamat datang, {nama_user}!")
print(f"\n\n========== {nama_app} ==========\n")
print("1. Tambah pemasukan:")
print("2. Tambah Pengeluaran:")
print("3. Lihat saldo:")
menu = input("Pilih menu (1/2/3): ")
if menu == "1":
    print(f"Harap masukan jumlah pemasukan Anda yang ingin ditambahkan:")
    saldo_tambah = int(input())
    saldo += saldo_tambah
    print(f"Pemasukan berhasil ditambahkan. Saldo Anda saat ini: {mata_uang} {saldo}")

elif menu == "2":
    print(f"Fitur tambah pengeluaran masih dalam pengembangan.")

elif menu == "3":
    print(f"Saldo Anda saat ini: {mata_uang} {saldo}")