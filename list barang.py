#List barang
class barang:
    def __init__(self, nama_barang, kode_barang, jumlah_barang, kondisi_barang):
        self.nama_barang = nama_barang
        self.kode_barang = kode_barang
        self.jumlah_barang = jumlah_barang
        self.kondisi_barang = kondisi_barang
    
    def daftar_barang (self):
        print(f"nama barang {self.nama_barang}")
        print(f"kode_barang {self.kode_barang}")
        print(f"jumlah barang {self.jumlah_barang}")
        print(f"kondisi brang {self.kondisi_barang}")

barang1 = barang("Komputer","KB001","40","Baik")
barang2 = barang("Proyektor","PJ002","1","Rusak")
barang3 = barang("Meja","MJ003","55", "Baik")

barang1.daftar_barang()
barang2.daftar_barang()
barang3.daftar_barang()