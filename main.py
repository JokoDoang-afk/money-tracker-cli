def tampilkan_menu():
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Lihat riwayat transaksi")
    print("5. Keluar\n")


def tambah_pemasukan(saldo, jumlah_pemasukan, kategori_pemasukan):
    saldo += jumlah_pemasukan
    transaksi = {
        "jenis": "pemasukan",
        "jumlah": jumlah_pemasukan,
        "kategori": kategori_pemasukan
    }
    riwayat_transaksi.append(transaksi)
    return saldo


def tambah_pengeluaran(saldo, jumlah_pengeluaran, kategori_pengeluaran):
    saldo -= jumlah_pengeluaran
    transaksi = {
        "jenis": "pengeluaran",
        "jumlah": jumlah_pengeluaran,
        "kategori": kategori_pengeluaran
    }
    riwayat_transaksi.append(transaksi)
    return saldo


def lihat_riwayat_transaksi():
    if not riwayat_transaksi:
            print("Belum ada transaksi yang dilakukan.\n\n")
    else:
        print("Riwayat Transaksi:")
        for transaksi in riwayat_transaksi:
            print(transaksi["jenis"])
            print(transaksi["jumlah"])
            print(transaksi["kategori"])


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
        kategori_pemasukan = input("Masukkan kategori pemasukan: ") 
        saldo = tambah_pemasukan(saldo, jumlah_pemasukan, kategori_pemasukan)
        print(f"Pemasukan berhasil ditambahkan. Saldo Anda saat ini: {mata_uang} {saldo}\n\n")

    elif menu == "2":
        jumlah_pengeluaran = int(input("Silakan masukkan jumlah pengeluaran: "))
        kategori_pengeluaran = input("Masukkan kategori pengeluaran: ")
        if jumlah_pengeluaran > saldo:
            print("Maaf, saldo Anda tidak cukup untuk melakukan pengeluaran ini.")
        else:
            saldo = tambah_pengeluaran(saldo, jumlah_pengeluaran, kategori_pengeluaran)
            print(f"Pengeluaran berhasil ditambahkan. Saldo Anda saat ini: {mata_uang} {saldo}\n\n")

    elif menu == "3":
        print(f"Saldo Anda saat ini: {mata_uang} {saldo}\n\n")
        
    elif menu == "4":
        lihat_riwayat_transaksi()
        print("\n\n")
                    

    elif menu == "5":
        print("Terima kasih telah menggunakan aplikasi ini!")
        break
    else:
        print("Menu yang Anda pilih tidak tersedia. Silakan pilih menu yang tersedia.")