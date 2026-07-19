import storage
import transactions


def tampilkan_menu():
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Lihat riwayat transaksi")
    print("5. Keluar\n")


def input_jumlah(pesan):
    while True:
        try:
            jumlah = int(input(pesan))
            if jumlah <= 0:
                print("Jumlah tidak boleh negatif atau nol. Silakan coba lagi.\n\n")
                continue
            return jumlah
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.\n\n")


def lihat_riwayat_transaksi():
    if not riwayat_transaksi:
        print("Belum ada transaksi yang dilakukan.\n\n")
    else:
        print("Riwayat Transaksi:")
        for transaksi in riwayat_transaksi:
            print(f"Jenis    : {transaksi['jenis'].capitalize()}")
            print(f"Jumlah   : {mata_uang} {transaksi['jumlah']}")
            print(f"Kategori : {transaksi['kategori'].title()}")
            print("------------------------------")


nama_app = "Money Tracking App"
nama_user = input("Masukkan nama Anda: ")
mata_uang = "IDR"
riwayat_transaksi = storage.load_data()
saldo = transactions.hitung_saldo(riwayat_transaksi)


print(f"Selamat datang, {nama_user}!")
print(f"\n\n========== {nama_app} ==========\n")
print("Menu Aplikasi:\n")
while True:
    tampilkan_menu()
    menu = input("Pilih menu (1/2/3/4/5): ")
    if menu == "1":
            jumlah_pemasukan = input_jumlah("Masukkan jumlah pemasukan: ")
            kategori_pemasukan = input("Masukkan kategori pemasukan: ") 
            saldo = transactions.tambah_pemasukan(saldo, jumlah_pemasukan, kategori_pemasukan, riwayat_transaksi)
            print("------------------------------")
            print(f"Pemasukan berhasil ditambahkan. \nSaldo Anda saat ini: {mata_uang} {saldo}\n")
            print("------------------------------")

    elif menu == "2":
            jumlah_pengeluaran = input_jumlah("Silakan masukkan jumlah pengeluaran: ")
            kategori_pengeluaran = input("Masukkan kategori pengeluaran: ")
            if jumlah_pengeluaran > saldo:
                print("Maaf, saldo Anda tidak cukup untuk melakukan pengeluaran ini.")
            else:
                saldo = transactions.tambah_pengeluaran(saldo, jumlah_pengeluaran, kategori_pengeluaran, riwayat_transaksi)
                print("------------------------------")
                print(f"Pengeluaran berhasil ditambahkan. \nSaldo Anda saat ini: {mata_uang} {saldo}\n")
                print("------------------------------")

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