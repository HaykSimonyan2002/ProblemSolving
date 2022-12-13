#հաշվել թվի 1 արժեքով բիթերի քանակը
def binarycounter(num):
    counter = 0 # time: O(1), space (0)
    while num >= 1: # time O(n), space ?
      if num % 2 != 0: # time O(1)
        counter += 1 # time O(1) 
      num //= 2 # time ?, space O(1)
    return counter # time O(1), space 0?
# time complexity = O(n + divide t.c.)


#ստուգել թվի 1 արժեքով բիթերի քանակը կենտ է, թե զույգ
def func(num):
    if binarycounter(num) % 2 != 0: return "կենտ" # time = binarycounter time complexity
    else: return "զույգ" # time = o(1)
#time c. = O(binarycounter time complexity + 1) = O(n + divide t.c.)

#կատարել swap գործողություն թվի i և j բիթերը տեղափոխելու համար
def swap(num, i, j):
    new_num = list(bin(num)[2:]) # slice time: O(n), bin function time: O(log(n)), string to list time = O(n) => time: O(n)
    print(new_num) # time O(1)
    elem = new_num[-i]; new_num[-i] = new_num[-j]; new_num[-j] = elem # time: O(3) = O(1) ?
    print(new_num) # time = O(1) 


    
#շրջել թվի բիթերը(reverse), օրինակ՝ 11110000 -> 00001111

def binaryreverse(num):
    print(bin(num)) # time: O(log(n)
    lst = [] # time: O(1)
    for i in range(len(bin(num)[2:])): # O(n)
      lst.append("1") # Amortize O(1)
    lst = ''.join(lst) # O(n)
    n = int(lst,2) # ?
    num = (n ^ num) # O(log(n/(2^n)))
    print(bin(num)) # O(log(n))
