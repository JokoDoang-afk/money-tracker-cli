def tampilkan_menu():
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Lihat riwayat transaksi")
    print("5. Keluar\n")


def tambah_pemasukan(saldo, jumlah_pemasukan):
    saldo += jumlah_pemasukan
    riwayat_transaksi.append(("pemasukan", jumlah_pemasukan))
    return saldo


def tambah_pengeluaran(saldo, jumlah_pengeluaran):
    saldo -= jumlah_pengeluaran
    riwayat_transaksi.append(("pengeluaran", jumlah_pengeluaran))
    return saldo



nama_app = "Money Tracking App"
nama_user = input("Masukkan nama Anda: ")
mata_uang = "IDR"
saldo = 15000
riwayat_transaksi = []


print(f"Selamat datang, {nama_user}!")
print(f"\n\n========== {nama_app} ==========\n")
print("Menu Aplikasi:\n")
while True:
    tampilkan_menu()
    menu = input("Pilih menu (1/2/3/4/5): ")
    if menu == "1":
        jumlah_pemasukan = int(input("Masukkan jumlah pemasukan: "))
        saldo = tambah_pemasukan(saldo, jumlah_pemasukan)
        print(f"Pemasukan berhasil ditambahkan. Saldo Anda saat ini: {mata_uang} {saldo}\n\n")

    elif menu == "2":
        jumlah_pengeluaran = int(input("Silakan masukkan jumlah pengeluaran: "))
        if jumlah_pengeluaran > saldo:
            print("Maaf, saldo Anda tidak cukup untuk melakukan pengeluaran ini.")
        else:
            saldo = tambah_pengeluaran(saldo, jumlah_pengeluaran)
            print(f"Pengeluaran berhasil ditambahkan. Saldo Anda saat ini: {mata_uang} {saldo}\n\n")

    elif menu == "3":
        print(f"Saldo Anda saat ini: {mata_uang} {saldo}\n\n")
        
    elif menu == "4":
        if not riwayat_transaksi:
            print("Belum ada transaksi yang dilakukan.\n\n")
        else:
            print("Riwayat Transaksi:")
            for transaksi in riwayat_transaksi:
                jenis, jumlah = transaksi
                print(f"{jenis.capitalize()}: {mata_uang} {jumlah}\n\n")

    elif menu == "5":
        print("Terima kasih telah menggunakan aplikasi ini!")
        break
    else:
        print("Menu yang Anda pilih tidak tersedia. Silakan pilih menu yang tersedia.")