def solution(n, k):
    if 0 <= n <= 2**31 - 1 and 1 <= k <= 31:
        binary_num = bin(n)[2:]
        bin_num_list =[]
        for i in binary_num:
            bin_num_list.append(i)
        while len(bin_num_list) < 6:
            bin_num_list.insert(0,"0")
        print(bin_num_list)
        bin_num_list[-(k)] = "0"
        bin_num_list = "".join(bin_num_list)
        item = int(bin_num_list,2)
    return item
