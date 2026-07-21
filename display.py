import utils


def tampilkan_menu():
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Lihat riwayat transaksi")
    print("5. Cari transaksi berdasarkan kategori")
    print("6. Edit transaksi")
    print("7. Hapus transaksi")
    print("8. Keluar\n")


def lihat_riwayat_transaksi(riwayat_transaksi, mata_uang):
    if not riwayat_transaksi:
        print("Belum ada transaksi yang dilakukan.\n\n")
        return
    
    print("Riwayat Transaksi:")
    
    for nomor, transaksi in enumerate(riwayat_transaksi, start=1):
            print(f"Nomor   : {nomor}")
            print(f"Jenis   : {transaksi['jenis'].capitalize()}")
            print(
                 f"Jumlah  : "
                 f"{utils.format_currency(mata_uang, transaksi['jumlah'])}")
            print(f"Kategori: {transaksi['kategori'].title()}")
            print("------------------------------")
