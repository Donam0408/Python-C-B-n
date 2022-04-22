

from cmath import sqrt
import math

def Bai1():
    print('Nhập diện tích mặt cầu')
    S = input()
    pi = 3.14
    R = math.sqrt(float(float(S) / (4*pi)))
    V = (4/3)*pi*(R**3) 
    print(f'Thể tích: {V}')
if __name__ == "__main__":
    Bai1()
    
    