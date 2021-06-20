class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def showList(self):
        return self.items
    def isNumber(self):
        try:
            float(self)
            return True
        except ValueError:
            return False

# No 1
def infixToPrefix(infixexpr):
    prec = {'^':3, '*':3, '/':3 , '+':2, '-':2 , '(':1} # melakukan identitasi kepada operator dengan skornya masing2
    decStack = Stack()
    prefixList = []
    tokenList = infixexpr.split()
    tokenList.reverse()
    for i in range(len(tokenList)):
         if tokenList[i] == '(':
              tokenList[i] = ')'
         elif tokenList[i] == ')':
              tokenList[i] = '('
              
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            prefixList.append(token)
        elif token == '(':
            decStack.push(token)
        elif token == ')':
            topToken = decStack.pop()
            
            while topToken != '(':
                prefixList.append(topToken)
                topToken = decStack.pop()
        else:
            while (not decStack.isEmpty()) and \
                (prec[decStack.peek()] >= prec[token]):
                prefixList.append(decStack.pop())
            decStack.push(token)

    while not decStack.isEmpty():
        prefixList.append(decStack.pop())
    prefixList = prefixList[::-1]
    return " ".join(prefixList)

print('No 1')
print("""
Referensi infix untuk inputan anda
-----------------------------------
1. A + B * C
2. (A + B) * C
3. A + (B * C)
4. A * B ^ C - D
5. A + (B - C) * D
-----------------------------------
""")
infix = input("Masukkan infix untuk diubah (menggunakan spasi ya:) : ")
prefix = infixToPrefix(infix)
print("Prefix nya adalah :",prefix)