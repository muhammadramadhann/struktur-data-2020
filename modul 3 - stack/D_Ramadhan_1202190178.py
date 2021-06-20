class StackMadhan: # mendefinisikan kelas stack
    def __init__(self, length):
        self.stack = [None for _ in range(length)] # sebuah loop tak aktif dan tidak memerlukan syarat variabel(menggunakan "_")
        self.top = -1                                 # loop sebanyak lenght nya
        self.lenght = length

    def push(self, value): # fungsi untuk melakukan push pada stack
        if self.top == self.lenght - 1:
            return -999
        self.top += 1
        self.stack[self.top] = value
        return 1

    def pop(self): # fungsi untuk melakukan penghapusan (pop) dari stack
        if self.top == -1:
            return -999
        value = self.stack[self.top]
        self.stack[self.top] = None
        self.top-=1
        return value
#-------------------------------------------------------------------------------------------------------------------------------------------
def karakter(stringInput): # fungsi untuk mengecek karakter yang ada dalam inputan apakah sebuah operator, huruf atau sebuah angka
    # isalpha () metode untuk mendeteksi string hanya terdiri dari huruf
    # isdigit () metode untuk mendeteksi string hanya terdiri dari angka
    if not(stringInput.isalpha() or stringInput.isdigit()): # apabila sebuah huruf dan angka return 1
        return True # mengembalikan nilai 1 atau true
    else: # opsi lainnya
        return False # mengembalikan nilai 0 atau false

def priority(operand): # memberikan informasi precedence tiap operator, 
    # misal operator ^ memiliki prioritas utama dari opeprator lainnya
    if operand == "+" or operand == "-":
        return 1 # mengembalikan nilai 1
    elif operand == "*" or operand == "/":
        return 2 # mengembalikan nilai 2
    elif operand == "^":
        return 3 # mengembalikan nilai 3
    else:
        return 0 # kondisi else (tidak ada prioritas yang terdata)

def infixToPrefix(infix): # fungsi mengeksekusi infix menjadi prefix
    prefix = " " # local variabel perfix
    reverseInfix = " " # local variabel infix di reverse
    for i in range(len(infix)-1, -1, -1): # melakukan reverse pada inputan berupa infix
        value = infix[i]
        if value == "(": # mengganti tanda kurung buka dengan tanda kurung tutup
            value = ")"
        elif value == ")": # mengganti tanda kurung tutup dengan tanda kurung buka
            value = "("
        reverseInfix += value # menambahkan variabel value yang berisi tanda kurung kedalam variabel infix reverse
    infix = reverseInfix # variabel yang berisi string reverse infix merupakan infix nya
    myStack = StackMadhan(len(infix)) # melakukan deklarasi pada stack
    for i in infix: # penjabaran karakter dalam infix apabila ada buka kurung, maka akan di push kedalam stack
        if i == "(":
            myStack.push(i)
        elif i == ")": # ketika dalam karakter tersebut bertemu dengan tutup kurung, maka element pada stack akan di pop
            x = myStack.stack[myStack.top]
            while myStack.top > -1 and x != "(": # syarat dalam stack nya lebih dari -1 dan karakter tidak ada buka kurungnya
                prefix += myStack.pop()
                x = myStack.stack[myStack.top]
            myStack.pop()
        elif not karakter(i): # jika karakter merupakan angka atau huruf akan ditambahkan kedalam prefix
            prefix += i
        elif karakter(i): # jika karakter merupakan suatu operator, akan dikeluarkan dari stack sampai stack kosong sepenuhnya
            y = myStack.stack[myStack.top] 
            while myStack.top > -1 and priority(i) <= priority(y): # menentukan priorotas utama dari operator
                prefix += myStack.pop() # mengeluarkan karakter dari stack
                y = myStack.stack[myStack.top]
            myStack.push(i) # melakukan push karakter operator kembali ke stack
    while myStack.top > -1: # ketika isi stack lebih dari -1
        prefix += myStack.pop() # isi dalam stack di pop dan ditambahkan ke prefix
    return prefix[::-1] # me return string inputan yang di reverse

def doIt():
    print("""
Infix reference for your input
-----------------------------------
|1|A+B*C
|2|(A+B)*C
|3|A+(B*C)
|4|A*B^C-D
|5|A+(B-C)*D
-----------------------------------
Program Notes : input expression without using spaces to work properly
    """)
    string = input("Enter the expression of infix : ")
    result = infixToPrefix(string)
    print("The prefix is :",result)

def showMenu():
    print("\nINFIX TO PREFIX USING PYTHON")
    print("""
| 1 | Try Infix to Prefix Formula by Lalih
| 2 | Exit from this program
    --------------------------------------------------------------------------
    | Program Notes : input expression without using spaces to work properly |
    --------------------------------------------------------------------------
    """)
    selectMenu = input("Select menu : ")
    print("-"*60)
    if selectMenu == "1":
        doIt()
        print("-"*60)
        back = str(input("\nBack to try the formula? [y/n] > "))
        while True:
            if back == "y":
                print("-"*60)
                doIt()
                print("-"*60)
                back = str(input("\nBack to try the formula? [y/n] > "))
            elif back == "n":
                print("-"*60)
                showMenu()
                print("-"*60)
                back = str(input("\nBack to try the formula? [y/n] > "))
            else:
                print("\nMenu is not available")
                back = str(input("\nBack to try the formula? [y/n] > "))
    elif selectMenu == "2":
        sure = input("Are you sure? [y/n] > ")
        if sure == "y":
            print("""
            Competitive Programmer Contestants Data
            ---------------------------------------------------------------------
            | Developer          | : Lalih Suralih Sumalih                      |
            | Intituition        | : Harvard University                         |
            | Major              | : Computer Science                           |
            | Competition Number | : 4D1327                                     |
            ---------------------------------------------------------------------
            """)
            exit()
        elif sure == "n":
            showMenu()
    
    else:
        print("Menu is not available")
        showMenu()

showMenu()