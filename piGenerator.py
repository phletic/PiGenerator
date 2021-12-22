from types import NoneType
import numpy as np
import math
import time
import multiprocessing as mp
from gmpy2 import mpz
a = 2_00_000_000
"""
def addition(f,g, trailZeros):

def square(f, numberOfDigits): #karabutsa multiplication
    numberBreak = numberOfDigits//2 + 1
    a = f.read(numberBreak)
    with open("storage/a.txt","w") as f:
        f.write(a)
    del a 
    b = f.read().split("|")
    zeroLead = b[1]
    try:
        b= b[0]
    except: 
        b = "0"
    aZeroLead = len(b)
    
    b = int(b)
    twoB = b<<1
    del b
    with open("storage/2b.txt","w") as f:
        f.write(twoB)

    #print(a,b, aZeroLead,zeroLead)
    return ()

def divisionOp(f,numPerOperation, divisor):
    numberOfYDigits = 0
    carry = 0
    while True:  # divide the number by 2
        c = f.read(numPerOperation)
        if "|" in c:
            c = c.split("|")[0]
        if not c:
            if carry != 0: yield str(carry/divisor).split(".")[1]
            yield numberOfYDigits
            break
        numberOfYDigits += len(c)
        c = carry + int(c)
        quotient = c// divisor
        carry = c % divisor
        yield str(quotient)
"""
"""
    numPerOperation: int = 100
    y = str(y)[2:]
    yDigits = len(str(y)) + n1
    with open('storage/y.txt', 'w') as f:
        numberYDigits = 0
        f.write(str(y) + "|" + str(n1)) # Writes y
    with open('storage/y.txt', 'r') as f:
        with open('storage/yDTwoTen.txt', 'a') as p:  # Divides by 2, then divide by n0 and write
            p.truncate(0)
            p.write(str(n0-yDigits) + "|")
            for i in divisionOp(f,numPerOperation, 2):
                if type(i) == int:
                    numberYDigits = i
                    continue
                else:
                    p.write(i)
        f.seek(0)
        print(numberYDigits)
        square(f, numberYDigits)
        # 3n0 * ax^2
"""

def N0Multiple(mul,n0, q, n):
    print("hi")
    q.put((mpz(mul)*n0,n))
    print("done")

def getY(y,n1, q):
    y = str(y)[2:]
    while len(y) < 8:
        y += "0"
    q.put((mpz(y + n1*"0"),3))


def isqrt(number):
    # Quake algorithm
    y = np.float32(number)
    i = y.view(np.int32)
    i = np.int32(0x5f3759df) - np.int32(i >> 1)
    y = i.view(np.float32)  # Number of decimal places = 7
    # https://www.desmos.com/calculator/f233sanhmd
    # High accuracy Newton method
    del i  # garbage handling
    numberIteration =0
    if a < 10: numberIteration =  3*a
    elif 10<=a<20: numberIteration = a//3
    else: numberIteration = math.floor(a**0.5)

    n = a+7    
    n1 = a-1
    print("start")
    n0 = mpz(10)**mpz(n*2)
    print("done")
    q = mp.Queue()
    processes = [mp.Process(target= N0Multiple ,args= (3,n0,q,1)),
                mp.Process(target= N0Multiple ,args= (2,n0,q,2)),
                mp.Process(target= getY ,args= (y,n1,q))        
                ] 
    for i in processes:
        i.start()
    """
    threeN0 = 3*n0
    twoN0 = 2*n0
    y = int(str(y)[2:] + n1*"0",10)
    """
    threeN0 = 0
    twoN0 = 0
    y = 0
    for _ in range(3):
        p = q.get()
        match p[1]:
            case 1:
                threeN0 = p[0]
            case 2:
                twoN0 = p[0]
            case 3:
                y = p[0]
    for i in processes:
        i.join()    
    del q
    del n0
    del n
    del n1
    del processes
    del p
    del i
    del _
    #print(type(threeN0),type(twoN0),type(y))
    print("total: " + str(numberIteration))
    try:
        for i in range(numberIteration):
            y = y*(threeN0 - number * y * y)//twoN0
            print(i)
    except KeyboardInterrupt:
        print("done")
        return y
    return y


if __name__ == "__main__":
    with open("storage/3.txt","w") as f: f.write(str(isqrt(3)))
    """
    d = decimal.Decimal(1)/a
    x_1 = [d*i for i in range(1,int(a+1))]
    l = [isqrt(i*i+1) for i in x_1]
    p_x = [a * b for a, b in zip(x_1, l)]
    p_y = l
    print(list(zip(p_x,p_y)))
    """
