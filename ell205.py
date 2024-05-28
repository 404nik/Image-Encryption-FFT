import numpy as np
from PIL import Image

def multr(a,z):
    x = np.zeros(len(a),dtype = complex)
    for i in range(len(a)):
        if ((i!=0) and (i!=(len(a)/2))):
            x[i] = a[i]*(z**i)
            x[-i] = a[-i]/(z**i)
        else:
            x[i] = a[i]
    x = np.array(x)
    return x

def mutate(a,o):
    x = np.zeros((len(a),len(a[0])),dtype = complex)
    for i in range(len(a)):
        ao = np.exp(-1j * 2 * np.pi * i * o /len(a[i]))
        x[i] = multr(a[i],ao)
    x = np.array(x)
    return x

def imtorgb(name):
    image = Image.open(name)
    arr = np.array(image)
    r = []
    g = []
    b = []
    for i in range(len(arr)):
        a = []
        y = []
        c = []
        for j in range(len(arr[i])):
            a.append(arr[i][j][0])
            y.append(arr[i][j][1])
            c.append(arr[i][j][2])
        r.append(a)
        g.append(y)
        b.append(c)
    r = np.array(r)
    g = np.array(g)
    b = np.array(b)
    return (r,g,b)

def rgbtoim(name,r,g,b):
    arr = []
    for i in range(len(r)):
        new = []
        for j in range(len(r[i])):
            n = [r[i][j],g[i][j],b[i][j]]
            new.append(n)
        arr.append(new)
    arr = np.array(arr)
    arr = arr.astype(np.uint8)
    data = Image.fromarray(arr,'RGB')
    data.save(name)

def mainencrypt(name,key):
    image = Image.open(name)
    ar = np.array(image)
    dim = len(np.shape(ar))
    if (dim == 2):
        res = encrypt(ar,key)
        data = Image.fromarray(res)
        data.save("./encrypt.jpeg")
    elif (dim==3):
        r,g,b = imtorgb(name)
        rr = encrypt(r,key)
        gg = encrypt(g,key)
        bb = encrypt(b,key)
        rgbtoim("./encrypt.jpeg",rr,gg,bb)

def maindecrypt(name,key):
    image = Image.open(name)
    ar = np.array(image)
    dim = len(np.shape(ar))
    if (dim == 2):
        res = decrypt(ar,key)
        data = Image.fromarray(res)
        data.save("./decrypt.jpeg")
    elif (dim==3):
        r,g,b = imtorgb(name)
        rr = decrypt(r,key)
        gg = decrypt(g,key)
        bb = decrypt(b,key)
        rgbtoim("./decrypt.jpeg",rr,gg,bb)
    
def encrypt(x,key):
    r1,r2 = key
    ar = x
    temp1 = np.fft.fft(ar,norm="ortho")
    temp2 = mutate(temp1,r1)
    temp3 = np.fft.ifft(temp2,norm = "ortho")
    temp4 = temp3.transpose()
    temp5 = np.fft.fft(temp4,norm="ortho")
    temp6 = mutate(temp5,r2)
    temp7 = np.fft.ifft(temp6,norm="ortho")
    temp8 = []
    for i in range(len(temp7)):
        r = []
        for j in range(len(temp7[i])):
            r.append(temp7[i][j].real)
        temp8.append(r)
    temp8 = np.array(temp8)
    temp8 = temp8.astype(np.uint8)
    return temp8

def decrypt(x,key):
    r1,r2 = key
    ar = x
    temp1 = np.fft.fft(ar,norm="ortho")
    temp2 = mutate(temp1,-1*r2)
    temp3 = np.fft.ifft(temp2,norm = "ortho")
    temp4 = temp3.transpose()
    temp5 = np.fft.fft(temp4,norm="ortho")
    temp6 = mutate(temp5,-1*r1)
    temp7 = np.fft.ifft(temp6,norm="ortho")
    temp8 = []
    for i in range(len(temp7)):
        r = []
        for j in range(len(temp7[i])):
            r.append(temp7[i][j].real)
        temp8.append(r)
    temp8 = np.array(temp8)
    data = Image.fromarray(temp8)
    temp8 = temp8.astype(np.uint8)
    return temp8
