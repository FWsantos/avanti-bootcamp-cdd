import math

def prime_number(num):
    for i in range(1, math.floor((num+1)/2)):
        if num%i == 0 and i != 1:
            print(num, "não é primo.")
            break;
    else:
        print(num, "é primo.")