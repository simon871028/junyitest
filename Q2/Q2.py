#依題意敘述，假設輸入皆為非負整數，會在unittest做錯誤輸入的判斷。
def totalNumberLeft(num):
    result = 0
    if num < 0 or num %1 != 0:
        return False
    else:
        for i in range(1,num + 1):
            if i % 15 == 0:
                result += 1
            elif i % 5 != 0 and i % 3 != 0:
                result += 1 
    return result

totalNumberLeft(5)