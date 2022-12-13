#հաշվել թվի 1 արժեքով բիթերի քանակը
def binarycounter(num):
    count = 0
    a = bin(num)[2:]
    for i in a:
      if i == "1":
        count +=1
    return count


#ստուգել թվի 1 արժեքով բիթերի քանակը կենտ է, թե զույգ
def func(num):
    if binarycounter(num) % 2 != 0: return "կենտ"
    else: return "զույգ"


#կատարել swap գործողություն թվի i և j բիթերը տեղափոխելու համար
def swap(num, i, j):
    new_num = list(bin(num)[2:])
    print(new_num)
    elem = new_num[-i]; new_num[-i] = new_num[-j]; new_num[-j] = elem
    print(new_num)  
  
#շրջել թվի բիթերը(reverse), օրինակ՝ 11110000 -> 00001111

def binaryreverse(num):
    print(bin(num))
    lst = []
    for i in range(len(bin(num)[2:])):
      lst.append("1")
    lst = ''.join(lst)
    n = int(lst,2)
    num = (n ^ num)
    print(bin(num))
