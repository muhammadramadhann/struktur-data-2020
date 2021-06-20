class Node():
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode

class Linkedlist():
    def __init__(self):  
        self.root = None
        self.lastNode = None  

    def create(self, data):  
        newNode = Node(data)
        if self.root == None:  
            self.root = newNode
            self.lastNode = newNode
        else:  
            self.lastNode.nextNode = newNode
            self.lastNode = newNode

    def sortData(self):  
        lastNode = self.root
        indexNode = None  
        if self.root == None:  
            return
        else:  
            while lastNode != None:  
                indexNode = lastNode.nextNode
                while indexNode != None:  
                    if(lastNode.data > indexNode.data):  
                        theNode = lastNode.data 
                        lastNode.data = indexNode.data
                        indexNode.data = theNode
                    indexNode = indexNode.nextNode  
                lastNode = lastNode.nextNode

    def read(self):  
        lastNode = self.root
        if self.root is None:  
            print("File masih kosong, silahkan ke menu tambah data") 
            return  
        while lastNode != None:  
            print(lastNode.data)
            lastNode = lastNode.nextNode;  
        print()

# ---------------------------------------------------------------------------------------------------
MyList = Linkedlist()

def tambahData():
    print("""
input: done, untuk mengakhiri inputan dan menampilkan data barang
data yang diinputkan otomatis akan diurut menurut alfabet
    """)
    while True:
        namaBarang = input("Masukkan barang : ")
        if namaBarang != "done":
            MyList.create(namaBarang)
            continue
        elif namaBarang == "done":
            MyList.sortData()
            print("\nData Barang:\n")
            MyList.read()
            break

def lihatData():
    MyList.read()

def showMenu():
    print("\nAPLIKASI PENGINPUTAN BARANG v.1.0\n")
    print("""
             |PT GUDANG SEJAHTERA INDONESIA|
    ---------------------------------------------------
    |1 Tambah Data | 2 Lihat Data | 3 Keluar Aplikasi |
    ---------------------------------------------------
    """)
    pilihMenu = input("Pilih Menu : ")
    print("-"*60)
    if pilihMenu == "1":
        tambahData()
        print("-"*60)
        balik = str(input("\nMasukkan barang lagi? [y/n] > "))
        while True:
            if balik == "y":
                print("-"*60)
                tambahData()
                print("-"*60)
                balik = str(input("\nMasukkan barang lagi? [y/n] > "))
            elif balik == "n":
                print("-"*60)
                showMenu()
                print("-"*60)
                balik = str(input("\nMasukkan barang lagi? [y/n] > "))
    
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