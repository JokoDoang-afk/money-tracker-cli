import storage

def tambah_pemasukan(saldo, jumlah_pemasukan, kategori_pemasukan, riwayat_transaksi):
    saldo += jumlah_pemasukan
    transaksi = {
        "jenis": "pemasukan",
        "jumlah": jumlah_pemasukan,
        "kategori": kategori_pemasukan
    }
    riwayat_transaksi.append(transaksi)
    storage.save_data(riwayat_transaksi)
    return saldo
    


def tambah_pengeluaran(saldo, jumlah_pengeluaran, kategori_pengeluaran, riwayat_transaksi):
    saldo -= jumlah_pengeluaran
    transaksi = {
        "jenis": "pengeluaran",
        "jumlah": jumlah_pengeluaran,
        "kategori": kategori_pengeluaran
    }
    riwayat_transaksi.append(transaksi)
    storage.save_data(riwayat_transaksi)
    return saldo


def hitung_saldo(riwayat_transaksi):
    saldo = 0
    for transaksi in riwayat_transaksi:
        if transaksi["jenis"] == "pemasukan":
            saldo += transaksi["jumlah"]
        elif transaksi["jenis"] == "pengeluaran":
            saldo -= transaksi["jumlah"]
    return saldo

def edit_transaksi(
        riwayat_transaksi, 
        index, 
        jumlah_baru=None, 
        kategori_baru=None
):
    transaksi = riwayat_transaksi[index]

    if jumlah_baru is not None:
        transaksi["jumlah"] = jumlah_baru
    if kategori_baru is not None:
        transaksi["kategori"] = kategori_baru

    storage.save_data(riwayat_transaksi)

def input_kategori(pesan):
    while True:
        kategori = input(pesan).strip()
        if not kategori:
            print("Kategori tidak boleh kosong. Silakan coba lagi.\n")
            continue
        return kategori
    
def hapus_transaksi(
        riwayat_transaksi, 
        index
):
    riwayat_transaksi.pop(index)
    storage.save_data(riwayat_transaksi)