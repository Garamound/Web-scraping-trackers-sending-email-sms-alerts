# 0 0 1 2

def get_nth_fibbonaci_number(n):
    fbn_list = [0, 1, 1]
    if n == 1: fbn_list = [0]
    for n in range(0 , n - 3):
        fbn_list.append((fbn_list[len(fbn_list) - 1]) + fbn_list[len(fbn_list) - 2])
    print(fbn_list[-1])

get_nth_fibbonaci_number(4)