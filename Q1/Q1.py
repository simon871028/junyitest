def reverseString(string):
    ls = string.split(" ")
    result = []
    for item in ls:
        result.append(item[::-1])
    result = " ".join(result)
    return result
    
