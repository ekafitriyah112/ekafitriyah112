print('==============================================')
print("     PROGRAM KASIR SEDERHANA     ")
print('===============================================')
print("Menu Warung Solo")
print("Pilih menu : ")
print("1. Mie ayam  : Rp15.000")
print("2. Bakso     : Rp10.000 ")
pilih = int(input("Masukkan menu : "))
if pilih == 1:
    print("Mie ayam : Rp15.000")
    jumlah = int(input("jumlah pesanan : "))
    total = jumlah*15000
    print("Total harga: ", total)
    print("====terimakasih====")
elif pilih == 2:
    print("Bakso : Rp10.000")
    jumlah = int(input("jumlah pesanan : "))
    total = jumlah*10000
    print("Total harga: ", total)
    print("====terimakasih====")
print('=============================================')
print('     Biodata Mahasiswa       '  )
Nama_lengkap = input("Siapa namamu? : ")
Alamat = input("Kamu berasal dari mana? : ")
Kelas = input("Kamu kelas apa? : ")
Npm = input("Berapa Npm kamu? : ")
print('==============================================')

class Kucing():
 def __init__(self, nama, umur, warna ):
    self.nama = nama
    self.umur = umur
    self.warna = warna

 def suara(self):
     print("Suara : Meow meow meow")

 def suara_makan(self):
     print("Suara Makan : Nyam nyam nyam")

mykucing = Kucing("Uti", 1, "putih")
anggo = Kucing("Anggo", 2, "hitam" )

print(mykucing.nama, mykucing.umur, mykucing.warna)
mykucing.suara()
print(anggo.nama, anggo.umur, anggo.warna)
mykucing.suara_makan()
