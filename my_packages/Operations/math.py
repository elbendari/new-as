def cal_average(num):
    i = 0
    for x in num:
        i +=  x           

    avg = i / len(num)
    return avg

cal_average([1,2,3,4])