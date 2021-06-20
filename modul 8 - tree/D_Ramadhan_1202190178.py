# Muhammad Ramadhan Kurniawan | 1202190178 | SI4303

from binarytree import *

def inOrderTree():
    item = [1] # pada list diberikan angka 1 yang akan menjadi root nya
    print("\n-------------------------------------------------------------------")
    print("Fact: jumlah inputan merupakan jumlah angka yang akan anda inputkan")
    print("-------------------------------------------------------------------\n")
    total = int(input("jumlah inputan : ")) # sebelum user menginput angka, user menentukan jumlah angka yang akan diinputkan

    for i in range (total):
        angka = int(input("masukkan angka : "))
        item.append(angka) # inputan yang telah dilakukan akan di append atau dimasukkan kedalam list

    print()
    tree = build(item) # dengan menggunakan item pada library binarytree, kita dapat membangun sebuah diagram tree dengan mudah dan cepat
    print(tree) # menampilkan tree dalam bentuk diagram
    print("Urutan inorder : ",tree.inorder) # menampilkan urutan secara inorder dari tree yang sudah dibuat tadi
    print("Konsep inorder : Left -> Root -> Right")
    print("Urutan preorder : ",tree.preorder)
    print("Urutan postorder : ",tree.postorder)
    # pada inputan user akan diurutkan dari tree yang telah dibentuk program dan diurutkan secara inorder
    # alur inorder nya adalah : left -> root -> right

    print("""\n
Peserta  : Bagas Subagas
Kategori : Pemrograman
Kasus    : Membuat tree dengan user input dan mengurutkannya secara inorder traversal""")

inOrderTree()