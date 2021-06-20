# Muhammad Ramadhan Kurniawan (1202190178)
class Queue: # inisialisasi kelas queue
    def __init__(self):
        self.items = [] # wadah list items dari stok barang

    def isEmpty(self): # fungsi untuk me-return isi list yang nul/kosong
        return self.items == []

    def pushQueue(self, items): # fungsi untuk menambahkan data barang kedalam stok barang
        self.items.append(items) # barang masuk sesuai indeksnya (dari pertama)

    def popQueue(self): # fungsi untuk menghapus item berdasarkan prinsip FIFO pada queue
        return self.items.pop(0)

    def size(self): # fungsi untuk me-return panjang dari list items stok barang
        return len(self.items)
    
    def printQueue(self): # fungsi untuk menampilkan
        if self.items == []:
            print("Stok masih kosong, silahkan pilih menu tambah stok barang")
        else:
            number = 1
            for items in self.items: # menggunakan loop agar output tidak berbentuk list
                print("Queue",number,"-",items)
                number += 1

#========================================================================================================================================

q = Queue() # instance dari kelas Queue dengan nama 'q'

urutan = [] # Sebuah list untuk menampung nomor urut barang
nomorUrut = 0
def barangMasuk(): # fungsi untuk melengkapi pushQueue dengan sedikit modifikasi agar program mudah digunakan
    barang = input("Masukkan nama barang : ")
    q.pushQueue(barang)
    global nomorUrut
    nomorUrut += 1
    urutan.append(nomorUrut)
    print(barang,"berhasil masuk ke stok dan merupakan urutan ke -",nomorUrut)

def barangKeluar(): # fungsi untuk melengkapi popQueue dengan sedikit modifikasi agar program mudah digunakan
    yakin = input("Anda yakin akan menghapus stok barang terdepan? [y/n] > ")
    if yakin == "y":
        if q.isEmpty() == True:
            print("Stok masih kosong, silahkan pilih menu tambah stok barang")
        else:
            global nomorUrut
            urutan.pop()
            print(q.popQueue(),"yang merupakan urutan ke - ",(nomorUrut)-len(urutan),"berhasil dihapus dari stok\n")
            tampilBarang()
    elif yakin == "n":
        showMenu()
    else:
        print("Menu tidak tersedia")

def tampilBarang(): # fungsi untuk melengkapi printQueue dengan sedikit modifikasi agar program mudah digunakan
    print("Data stok barang saat ini :")
    print("="*60)
    q.printQueue()
    print("="*60)

def showMenu(): # fungsi tampilan menu agar user dapat lancar menggunakan programnya dengan keterangan yang lengkap juga
    print("""
=============================================================================================
|     Selamat Datang di Program Pendataan dan Penghapusan Stok Barang Perusahaan ABC        |
=============================================================================================
| pilih menu  |1| Tambah stok barang (masukkan nama barang)                                 |
| pilih menu  |2| Lihat stok barang                                                         |
| pilih menu  |3| Hapus stok barang (otomatis terhapus item paling pertama)                 |
| pilih menu  |4| Keluar program                                                            |
|                                                                                           |
|*Program ini menggunakan prinsip FIFO, barang yang pertama masuk akan dihapus pertama kali |
=============================================================================================
    """)
    pMenu = input("Menu : ")
    print("-"*60)
    if pMenu == "1":
        barangMasuk()
        print("-"*60)
        kembali = input("\nMasukkan stok barang lagi? [y/n] > ")
        while True:
            if kembali == "y":
                print("-"*60)
                barangMasuk()
                print("-"*60)
                kembali = input("\nMasukkan stok barang lagi? [y/n] > ")
            elif kembali == "n":
                print("-"*60)
                showMenu()
                print("-"*60)
                kembali = input("\nMasukkan stok barang lagi? [y/n] > ")
            else:
                print("\nMenu tidak tersedia!")
                kembali = input("\nMasukkan stok barang lagi? [y/n] > ")

    elif pMenu == "2":
        tampilBarang()
        print("-"*60)
        kembali = input("\nKembali ke menu lihat stok lagi? [y/n] > ")
        while True:
            if kembali == "y":
                print("-"*60)
                tampilBarang()
                print("-"*60)
                kembali = input("\nKembali ke menu lihat stok lagi? [y/n] > ")
            elif kembali == "n":
                print("-"*60)
                showMenu()
                print("-"*60)
                kembali = input("\nKembali ke menu lihat stok lagi? [y/n] > ")
            else:
                print("\nMenu tidak tersedia!")
                kembali = input("\nKembali ke menu lihat stok lagi? [y/n] > ")

    elif pMenu == "3":
        barangKeluar()
        print("-"*60)
        kembali = input("\nHapus stok(terdepan) lagi? [y/n] > ")
        while True:
            if kembali == "y":
                print("-"*60)
                barangKeluar()
                print("-"*60)
                kembali = input("\nHapus stok(terdepan) lagi? [y/n] > ")
            elif kembali == "n":
                print("-"*60)
                showMenu()
                print("-"*60)
                kembali = input("\nHapus stok(terdepan) lagi? [y/n] > ")
            else:
                print("\nMenu tidak tersedia!")
                kembali = input("\nHapus stok(terdepan) lagi? [y/n] > ")

    elif pMenu == "4":
        yakin = input("Anda yakin ingin keluar? [y/n] > ")
        if yakin == "y":
            print(""" 
                    TERIMA KASIH TELAH MENGGUNAKAN APLIKASI INI
             --------------------------------------------------------
            | Developer : Muhammad Ramadhan Kurniawan                |
            | Adress    : Kabupaten Bekasi                           |
            | Phone     : 0812821650022                              |
            | Email     : ramadhanman@student.telkomuniversity.ac.id |
            |--------------------------------------------------------|
            |                  all rights reserved                   |
             --------------------------------------------------------
            """)
            exit()
        elif yakin == "n":
            showMenu()

    else:
        print("""
 -----------------------
| Menu tidak tersedia ! |
 -----------------------
        """)
        showMenu()

showMenu() # memanggil seluruh kode diatas

# Terima kasih