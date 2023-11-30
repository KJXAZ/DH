import random


def random_int(num):
    return random.randint(1, num - 1)

p_list = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]
g_list = [2, 5, 2, 6, 3, 3, 2, 3, 2, 2, 6, 5, 2, 5, 2, 2, 2, 19, 5, 2, 3, 2, 3, 2, 6, 3, 7, 7, 6]

def f(g, Xa,p):
    temp = 1
    while Xa > 0:
        if Xa & 1 == 1:
            temp = (temp * g)%p 
        g = (g * g) % p
        Xa >>= 1
    return temp


for p, g in zip(p_list, g_list):
    X_A = random.randint(1, p - 1)
    X_B = random.randint(1, p - 1)

    print("素数 p= ", p)
    print("本原根 g= ", g)
    print("A获取的私钥 Xa=", X_A)
    print("B获取的私钥 Xb=", X_B)

    Y_A = f(g, X_A, p)
    Y_B = f(g, X_B, p)
    print("A计算得到的公钥 Ya为：", Y_A)
    print("B计算得到的公钥 Yb为：", Y_B)

    print("------X_A与B交换公钥------")
    key_A = f(Y_B, X_A, p)
    key_B = f(Y_A, X_B, p)
    print("A计算得到的key为：", key_A)
    print("B计算得到的key为：", key_B)

    print("\n**************************")