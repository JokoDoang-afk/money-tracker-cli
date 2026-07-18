nama_app = "Money Tracking App"
nama_user = input("Masukkan nama Anda: ")
mata_uang = "IDR"
saldo = 150000



print(f"Selamat datang, {nama_user}!")
print(f"\n\n========== {nama_app} ==========\n")
print("Menu Aplikasi:\n")
while True:
    print("1. Tambah pemasukan:")
    print("2. Tambah Pengeluaran:")
    print("3. Lihat saldo:")
    print("4. Keluar")
    menu = input("Pilih menu (1/2/3/4): ")
    if menu == "1":
        jumlah_pemasukan = int(input("Masukkan jumlah pemasukan: "))
        saldo += jumlah_pemasukan
        print(f"Pemasukan berhasil ditambahkan. Saldo Anda saat ini: {mata_uang} {saldo}")
    elif menu == "2":
        saldo_kurang = int(input("Silakan masukkan jumlah pengeluaran: "))
        if jumlah_pemasukan > saldo:
            print("Maaf, saldo Anda tidak cukup untuk melakukan pengeluaran ini.")
        else:
            saldo -= jumlah_pemasukan
            print(f"Pengeluaran berhasil ditambahkan. Saldo Anda saat ini: {mata_uang} {saldo}")
    elif menu == "3":
        print(f"Saldo Anda saat ini: {mata_uang} {saldo}")
    elif menu == "4":
        print("Terima kasih telah menggunakan aplikasi ini!")
        break
    else:
        print("Menu yang Anda pilih tidak tersedia. Silakan pilih menu yang tersedia.")