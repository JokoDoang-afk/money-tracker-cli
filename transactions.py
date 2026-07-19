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
