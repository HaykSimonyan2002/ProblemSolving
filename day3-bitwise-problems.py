#հաշվել թվի 1 արժեքով բիթերի քանակը
def binarycounter(num):
  count = 0
  while num != 0:
    if num & 1 == 1:
      count += 1
    num >>= 1
  return count
# time: O(log(n)), space: O(1)


#ստուգել թվի 1 արժեքով բիթերի քանակը կենտ է, թե զույգ
def func(num): # Out: True -> կենտ, False -> զույգ
    if num == 0: return 0
    else: 
      bl = False
      while num != 0:
        if num & 1 == 1:
          bl = not bl
        num >>= 1
    return bl

#կատարել swap գործողություն թվի i և j բիթերը տեղափոխելու համար
def swap(num, i, j):
  


    
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
