import display
import storage
import transactions
import utils


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


nama_app = "Money Tracking App"
nama_user = input("Masukkan nama Anda: ")
mata_uang = "IDR"
riwayat_transaksi = storage.load_data()
saldo = transactions.hitung_saldo(riwayat_transaksi)


print(f"Selamat datang, {nama_user.upper()}!")
print(f"\n\n========== {nama_app} ==========\n")
print("Menu Aplikasi:\n")
while True:
    display.tampilkan_menu()
    menu = input("Pilih menu (1/2/3/4/5/6/7/8): ")
    if menu == "1":
        jumlah_pemasukan = input_jumlah("Masukkan jumlah transaksi baru: ")
        kategori_pemasukan = input("Masukkan kategori pemasukan: ")
        saldo = transactions.tambah_pemasukan(saldo, jumlah_pemasukan, kategori_pemasukan, riwayat_transaksi)
        print("------------------------------")
        print(f"Pemasukan berhasil ditambahkan. \nSaldo Anda saat ini: {utils.format_currency(mata_uang, saldo)}\n")
        print("------------------------------")

    elif menu == "2":
        jumlah_pengeluaran = input_jumlah("Silakan masukkan jumlah pengeluaran: ")
        kategori_pengeluaran = input("Masukkan kategori pengeluaran: ")
        if jumlah_pengeluaran > saldo:
            print("Maaf, saldo Anda tidak cukup untuk melakukan pengeluaran ini.")
        else:
            saldo = transactions.tambah_pengeluaran(saldo, jumlah_pengeluaran, kategori_pengeluaran, riwayat_transaksi)
            print("------------------------------")
            print(f"Pengeluaran berhasil ditambahkan. \nSaldo Anda saat ini: {utils.format_currency(mata_uang, saldo)}\n")
            print("------------------------------")

    elif menu == "3":
        saldo = transactions.hitung_saldo(riwayat_transaksi)
        print(f"Saldo saat ini: {utils.format_currency(mata_uang, saldo)}\n")
            
        
    elif menu == "4":
        display.lihat_riwayat_transaksi(
            riwayat_transaksi, 
            mata_uang
            )
        print("\n\n")
                    
    elif menu == "5":
        kategori_dicari = input("Masukkan kategori yang ingin dicari: ")
        ditemukan = False
        print("=== Search Transaction ===\n\n")
        for transaksi in riwayat_transaksi:
            if kategori_dicari.lower() in transaksi["kategori"].lower():
                print("------------------------------")
                print(f"Jenis    : {transaksi['jenis'].capitalize()}")
                print(f"Jumlah   : {utils.format_currency(mata_uang, transaksi['jumlah'])}")
                print(f"Kategori : {transaksi['kategori'].title()}")
                print("------------------------------")
                ditemukan = True 
        if not ditemukan:
            print("Transaksi dengan kategori tersebut tidak ditemukan.\n\n")

    elif menu == "6":
        print("=== Edit Transaction ===\n\n")
        if not riwayat_transaksi:
            print("Belum ada transaksi yang dilakukan.\n\n")
        else:
            for index_transaksi, transaksi in enumerate(riwayat_transaksi):
                print(f"{index_transaksi + 1}. Jenis: {transaksi['jenis'].capitalize()}, Jumlah: {utils.format_currency(mata_uang, transaksi['jumlah'])}, Kategori: {transaksi['kategori'].title()}")
            try:
                index_edit = int(input("\nMasukkan nomor transaksi yang ingin diedit: ")) - 1
                if index_edit < 0 or index_edit >= len(riwayat_transaksi):
                    print("Nomor transaksi tidak valid.\n\n")
                    continue
                transaksi_dipilih = riwayat_transaksi[index_edit]
                print("\n=== Transaksi yang dipilih ===")
                print(f"Jenis    : {riwayat_transaksi[index_edit]['jenis'].capitalize()}")
                print(f"Jumlah   : {utils.format_currency(mata_uang, transaksi_dipilih['jumlah'])}")
                print(f"Kategori : {riwayat_transaksi[index_edit]['kategori'].title()}")
                print("===============================")
                print(f"\nAnda ingin mengedit apa?")
                print("1. Edit Jumlah transaksi")
                print("2. Edit kategori transaksi")
                print("3. Edit jumlah dan kategori transaksi")   
                pilihan_edit = input("Pilih opsi (1/2/3): ")
                if pilihan_edit == "1":
                    jumlah_baru = input_jumlah("Masukkan jumlah transaksi baru: ")
                    transactions.edit_transaksi(
                        riwayat_transaksi,
                        index_edit,
                        jumlah_baru=jumlah_baru
                    )
                    saldo = transactions.hitung_saldo(riwayat_transaksi)
                    print("Jumlah transaksi berhasil diperbarui.\n")

                elif pilihan_edit == "2":
                    kategori_baru = input("Masukkan kategori transaksi baru: ").strip()
                    if not kategori_baru:
                        print("Kategori tidak boleh kosong.\n\n")
                        continue
                    transactions.edit_transaksi(
                        riwayat_transaksi,
                        index_edit,
                        kategori_baru=kategori_baru
                    )
                    print("Kategori transaksi berhasil diperbarui.\n\n")
                    
                elif pilihan_edit == "3":
                    jumlah_baru = input_jumlah("Masukkan jumlah transaksi baru: ")
                    kategori_baru = input("Masukkan kategori transaksi baru: ").strip()
                    if not kategori_baru:
                        print("Kategori tidak boleh kosong.\n\n")
                        continue
                    transactions.edit_transaksi(
                        riwayat_transaksi,
                        index_edit,
                        jumlah_baru=jumlah_baru,
                        kategori_baru=kategori_baru
                    )
                    saldo = transactions.hitung_saldo(riwayat_transaksi)
                    print("Transaksi berhasil diperbarui.\n\n")
                else:
                    print("Opsi yang Anda pilih tidak valid.\n\n")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.\n\n")

    elif menu == "7":
        print("=== Hapus Transaksi ===")
        if not riwayat_transaksi:
            print("Belum ada transaksi yang dilakukan.\n")
        else:
            display.lihat_riwayat_transaksi(
            riwayat_transaksi,
            mata_uang
        )

        try:
            nomor_transaksi = int(input("\nMasukkan nomor transaksi yang ingin dihapus: ")) 

            index_transaksi = nomor_transaksi - 1

            if(index_transaksi < 0 or index_transaksi >= len(riwayat_transaksi)):
                print("Nomor tidak valid \n")
                continue
            transaksi_dipilih = riwayat_transaksi[index_transaksi]
            print("\n=== Transaksi yang Akan Dihapus ===")
            print(
                f"Jenis    : "
                f"{transaksi_dipilih['jenis'].capitalize()}"
            )
            print(
                f"Jumlah   : {utils.format_currency(mata_uang, transaksi_dipilih['jumlah'])}"
            )
            print(
                f"Kategori : "
                f"{transaksi_dipilih['kategori'].title()}"
            )
            print("====================================")

            konfirmasi = input("Yakin ingin menghapus transaksi ini? (y/n):").strip().lower()
            if konfirmasi == "y":
                transactions.hapus_transaksi(riwayat_transaksi, index_transaksi)
                saldo = transactions.hitung_saldo(riwayat_transaksi)
                print("Transaksi berhasil dihapus.\n")

            elif konfirmasi == "n":
                print("Penghapusan transaksi dibatalkan.\n")
            else:
                print("Pilihan konfirmasi tidak valid.\n ")

            
        except ValueError:
            print("Input tidak valid. Silahkan masukan angka")


    elif menu == "8":
        print("Terima kasih telah menggunakan aplikasi ini!")
        break
    else:
        print("Menu yang Anda pilih tidak tersedia. Silakan pilih menu yang tersedia.")