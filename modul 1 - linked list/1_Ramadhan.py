class Node():
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode
    
    def getNext(self):
        return self.nextNode

    def hasNext(self):
        if self.getNext() is None:
            return False
        return True

    def toString(self):
        return self.data


class Linkedlist():
    def __init__(self, root = None):
        self.root = root

    def Root(self):
        if self.root == None:
            return True
        else:
            return False

    def create(self, data):
        newNode = Node(data, self.root)
        self.root = newNode

    def popdata(self): 
        if self.Root():
            print("\nTidak ada file yang dihapus") 
            return None
        else: 
            Node_pop = self.root 
            self.root = self.root.nextNode
            Node_pop.nextNode = None
            print("\nFile berhasil dihapus")
            return Node_pop.data

    def read(self):
        print("Data file saat ini:\n")
        if self.root is None:
            print("File masih kosong, silahkan ke menu tambah data")
            return
        thisNode = self.root
        print(thisNode.toString())
        while thisNode.hasNext():
            thisNode = thisNode.getNext()
            print(thisNode.toString())
        return

# ---------------------------------------------------------------------------------------------------
MyList = Linkedlist()

def tambahData():
    namaFile = input("Masukkan nama File : ")
    MyList.create(namaFile)
    print("Anda menambahkan file :",namaFile)
    print("File berhasil ditambahkan\n")
    MyList.read()

def lihatData():
    MyList.read()

def hapusData():
    hapus = input("Anda yakin menghapus data (data terakhir otomatis terhapus lebih dulu)[y/n]? : ")
    if hapus == "y":
        MyList.popdata()
        print("-"*60)
        MyList.read()
    elif hapus == "n":
        print("\nAnda belum menghapus file")

def showMenu():
    print("\nAPLIKASI PENGINPUTAN DAN PENGHAPUSAN FILE PERUSAHAAN MULTINASIONAL v.1.0\n")
    print("""
    ------------------------------------------------------------------
    |1 Tambah Data | 2 Lihat Data | 3 Hapus Data | 4 Keluar Aplikasi |
    ------------------------------------------------------------------
    * data yang dihapus adalah data terakhir
    """)
    pilihMenu = input("Pilih Menu : ")
    print("-"*60)
    if pilihMenu == "1":
        tambahData()
        print("-"*60)
        balik = str(input("\nTambah data lagi? [y/n] > "))
        while True:
            if balik == "y":
                print("-"*60)
                tambahData()
                print("-"*60)
                balik = str(input("\nTambah data lagi? [y/n] > "))
            elif balik == "n":
                print("-"*60)
                showMenu()
                print("-"*60)
                balik = str(input("\nTambah data lagi? [y/n] > "))

    elif pilihMenu == "2":
        lihatData()
        print("-"*60)
        balik = str(input("Kembali ke menu lihat data lagi? [y/n] > "))
        while True:
            if balik == "y":
                print("-"*60)
                lihatData()
                print("-"*60)
                balik = str(input("\nKembali ke menu lihat data lagi? [y/n] > "))
            elif balik == "n":
                print("-"*60)
                showMenu()
                print("-"*60)
                balik = str(input("\nKembali ke menu lihat data lagi? [y/n] > "))

    elif pilihMenu == "3":
        hapusData()
        print("-"*60)
        balik = str(input("\nKembali ke menu hapus data lagi? [y/n] > "))
        while True:
            if balik == "y":
                print("-"*60)
                hapusData()
                print("-"*60)
                balik = str(input("\nKembali ke menu hapus data lagi? [y/n] > "))
            elif balik == "n":
                print("-"*60)
                showMenu()
                print("-"*60)
                balik = str(input("\nKembali ke Menu hapus data lagi? [y/n] > "))

    elif pilihMenu == "4":
        yakin = input("Anda yakin ingin keluar? [y/n] > ")
        if yakin == "y":
            print(""" 
                    TERIMA KASIH TELAH MENGGUNAKAN APLIKASI INI
            |--------------------------------------------------------|
            | Developer : Muhammad Ramadhan Kurniawan                |
            | Adress    : Kabupaten Bekasi                           |
            | Phone     : 0812821650022                              |
            | Email     : ramadhanman@student.telkomuniversity.ac.id |
            |--------------------------------------------------------|
            |                  all rights reserved                   |
            |--------------------------------------------------------|
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

showMenu()