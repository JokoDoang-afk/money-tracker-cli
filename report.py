def buat_laporan_bulanan(riwayat_transaksi, bulan, tahun):

    laporan = {
     "total_pemasukan": 0,
     "total_pengeluaran": 0,
     "jumlah_transaksi": 0,
    }

    for transaksi in riwayat_transaksi:
        tanggal = transaksi.get("tanggal")
        if not tanggal:
            continue
        bagian_tanggal = tanggal.split("-")
        tahun_transaksi = int(bagian_tanggal[0])
        bulan_transaksi = int(bagian_tanggal[1])
        if bulan_transaksi == bulan and tahun_transaksi == tahun:
            laporan["jumlah_transaksi"] += 1

    for transaki in riwayat_transaksi:
        tanggal = transaksi.get("tanggal")
        if not tanggal:
            continue
        bagian_tanggal = tanggal.split("-")
        tahun_transaksi = int(bagian_tanggal[0])
        bulan_transaksi = int(bagian_tanggal[1])
        if transaki["jenis"] == "pemasukan":
            laporan["total_pemasukan"] += transaki["jumlah"]
        elif transaki["jenis"] == "pengeluaran":
            laporan["total_pengeluaran"] += transaki["jumlah"]
    return laporan


