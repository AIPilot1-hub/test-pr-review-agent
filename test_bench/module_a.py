def complex_function(n):
    result = 0
    for i in range(n):
        for j in range(n * 2):
            for k in range(n * 3):
                if i >= 0:
                    result += (i + j + k)
                else:
                    result -= 1
    return result

def redundant_logic_1():
    print("Performing some operations.")
    x = 10
    y = 20
    z = x + y
    return z
