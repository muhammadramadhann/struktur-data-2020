#DOUBLY LINKED LIST
#=======================================================================
 
# Class Node
class Node(object):
    def _init_(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
 

class DoubleList(object):
 
    dataAwal = None
    dataAkhir = None

    def appendItem(self):
        items = str(input('Input New Item                = '))
        new_barang = Node(items, None, None)
        if (self.dataAwal is None):
            self.dataAwal = self.dataAkhir = new_barang
        else:
            new_barang.prev = self.dataAkhir
            new_barang.next = None
            self.dataAkhir.next = new_barang
            self.dataAkhir = new_barang

    # Menampilkan isi dari list    
    def showItem(self):
        print(" BERIKUT ADALAH BARANG- BARANG YANG TERSEDIA DI RAVIN'S MUSIC IND : ")
        print(" ================================================================= ")
        # Membuat pointer yang menunjuk ke node pertama
        cur_barang = self.dataAwal
        if (self.dataAwal == None):
            print("      ** Maaf, Tidak ada barang yang tersedia :) ** ")
            return

        while(cur_barang != None):
            print(cur_barang.data)
            cur_barang = cur_barang.next 

    # Menghapus node
    def deleteItem(self):
        items = str(input('Masukkan data yang akan dihapus = '))
        cur_barang = self.dataAwal
       
        # Melakukan perulangan saat list tidak kosong
        while cur_barang is not None:
            if cur_barang.data == items:
                if cur_barang.next is None:
                    cur_barang.prev.next = None
                elif cur_barang.prev is not None:
                    cur_barang.prev.next = cur_barang.next
                    cur_barang.next.prev = cur_barang.prev
                else:
                    self.head = cur_barang.next #memindahkan head ke elemen berikutnya
                    cur_barang.next.prev = None #menunjuk head prev menjadi none
 
            cur_barang = cur_barang.next
           

    # Menampilkan menu program     
    def showProgram(self):
        print(" ")
        print("                     >>>>>>>   W E L C O M E   T O   <<<<<<< ")
        print("              >>>>>>>  R A V I N ' S    M U S I C   I N D   <<<<<<<")
        print("""
        ------------------------------------------------------------------
        |1 Tambah Data | 2 Lihat Data | 3 Hapus Data | 4 Keluar Aplikasi |
        ------------------------------------------------------------------
        """)
        pilih = "y"
        while ((pilih == "y") or (pilih == "Y")):
            pilihan = str(input(" >> Masukkan Menu yang anda pilih = "))
            print("------------------------------------------------------------------------")
            if(pilihan == "1"):
                self.appendItem()
                print("------------------------------------------------------------------------")
                print(" * ITEM TELAH DITAMBAHKAN ! * ")
                print("------------------------------------------------------------------------")
                self.showProgram()
                self.showProgram()
            elif(pilihan == "2"):
                self.showItem()
                self.showProgram()
            elif(pilihan == "3"):
                self.deleteItem()
                print("------------------------------------------------------------------------")
                print(" * ITEM TELAH TERHAPUS ! * ")
                print("------------------------------------------------------------------------")
                self.showProgram()
            else :
                pilih = " Anda Telah Keluar dari Program"
                break
               
if _name_ == "_main_":
    d = DoubleList()
    d.showProgram()