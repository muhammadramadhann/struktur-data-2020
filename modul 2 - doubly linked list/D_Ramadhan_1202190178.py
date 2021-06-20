# Coder : Muhammad Ramadhan Kurniawan
# NIM   : 1202190178
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def addLast(self, data):
        if self.head is None:
            newNode = Node(data)
            newNode.previous = None
            self.head = newNode
        else:
            newNode = Node(data)
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode
            newNode.previous = currentNode
            newNode.next = None

    def addFirst(self, data):
        if self.head is None:
            newNode = Node(data)
            newNode.previous = None
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
            newNode.previous = None

    def delete(self, value):
        currentNode = self.head
        while currentNode:
            if currentNode.data == value and currentNode == self.head:
                if not currentNode.next:
                    currentNode = None
                    self.head = None
                    print("Stok berhasil dihapus\n")
                    return
                else:
                    nextNode = currentNode.next
                    currentNode.next = None
                    nextNode.previous = None
                    currentNode = None
                    self.head = nextNode
                    print("Stok berhasil dihapus\n")
                    return

            elif currentNode.data == value:
                if currentNode.next:
                    nextNode = currentNode.next
                    previous = currentNode.previous
                    previous.next = nextNode
                    nextNode.previous = previous
                    currentNode.next = None
                    currentNode.previous = None
                    currentNode = None
                    print("Stok berhasil dihapus\n")
                    return

                else:
                    previous = currentNode.previous
                    previous.next = None
                    currentNode.previous = None
                    currentNode = None
                    print("Stok berhasil dihapus")
                    return

            currentNode = currentNode.next
        
    def read(self):
        print("Stok alat musik toko:\n")
        if self.head is None:
            print("Stok habis, silahkan masukkan barang")
            return
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next

myList = DoublyLinkedList()

def tambahData():
    musikMasuk = input("Masukkan jenis alat musik : ")
    myList.addLast(musikMasuk)
    print("Alat musik yang masuk stok toko :",musikMasuk)
    print(musikMasuk,"berhasil masuk ke stok tokomu!")

def lihatData():
    myList.read()

def hapusData():
    hapus = input("Masukkan alat musik yang telah terjual : ")
    myList.delete(hapus)
    myList.read()

def showMenu():
    print("\n\tAPLIKASI TOKO PERALATAN MUSIK BABEH SAYANG JERRY versi 1.1")
    print("""
     ------------------------------------------------------------------
    | 1 Barang Masuk | 2 Lihat Stok | 3 Hapus Stok | 4 Keluar Aplikasi |
     ------------------------------------------------------------------
    * Apabila ingin melakukan pencatatan barang masuk pilih menu 1
    * Apabila ingin melihat stok toko pilih menu 2
    * Apabila barang terjual hapus stok melalui menu 3
    """)
    pilihMenu = input("Pilih Menu : ")
    print("-"*60)
    if pilihMenu == "1":
        tambahData()
        print("-"*60)
        balik = str(input("\nMasukkan stok barang lagi? [y/n] > "))
        while True:
            if balik == "y":
                print("-"*60)
                tambahData()
                print("-"*60)
                balik = str(input("\nMasukkan stok barang lagi? [y/n] > "))
            elif balik == "n":
                print("-"*60)
                showMenu()
                print("-"*60)
                balik = str(input("\nMasukkan stok barang lagi? [y/n] > "))
            else:
                print("\nMenu tidak tersedia!")
                balik = str(input("\nMasukkan stok barang lagi? [y/n] > "))

    elif pilihMenu == "2":
        lihatData()
        print("-"*60)
        balik = str(input("Kembali ke menu lihat stok lagi? [y/n] > "))
        while True:
            if balik == "y":
                print("-"*60)
                lihatData()
                print("-"*60)
                balik = str(input("\nKembali ke menu lihat stok lagi? [y/n] > "))
            elif balik == "n":
                print("-"*60)
                showMenu()
                print("-"*60)
                balik = str(input("\nKembali ke menu lihat stok lagi? [y/n] > "))
            else:
                print("\nMenu tidak tersedia!")
                balik = str(input("\nKembali ke menu lihat stok lagi? [y/n] > "))

    elif pilihMenu == "3":
        hapusData()
        print("-"*60)
        balik = str(input("\nKembali ke menu hapus stok lagi? [y/n] > "))
        while True:
            if balik == "y":
                print("-"*60)
                hapusData()
                print("-"*60)
                balik = str(input("\nKembali ke menu hapus stok lagi? [y/n] > "))
            elif balik == "n":
                print("-"*60)
                showMenu()
                print("-"*60)
                balik = str(input("\nKembali ke Menu hapus stok lagi? [y/n] > "))
            else:
                print("\nMenu tidak tersedia!")
                balik = str(input("\nKembali ke menu lihat stok lagi? [y/n] > "))

    elif pilihMenu == "4":
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

showMenu()