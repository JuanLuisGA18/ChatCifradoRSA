# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:04:16 2021

@author: Samy
"""

def RotWord(word):
    return word[2:]+word[:2]

numbers = {
         '0' : '0000','1' : '0001','2' : '0010','3' : '0011','4' : '0100','5' : '0101','6' : '0110',
         '7' : '0111','8' : '1000','9' : '1001','A' : '1010','B' : '1011','C' : '1100','D' : '1101',
         'E' : '1110','F' : '1111'
    }

def get_key (dict, value):
    for k, v in dict.items():
        if v == value:
            return k

def hex2Bin(key):
    return numbers.get(key[0], None)+numbers.get(key[1], None)

def hex2Bin8(key):
    str=''
    zernum=8-len(key)
    while zernum:
        key='0'+key
        zernum-=1
    for i in range(8):
        str+=numbers.get(key[i], None)
    #print(str)
    return str
    
def SubBytes(key):
    #print(key)
    key=hex2Bin(key)
    c='11000110'
    b=''
    for i in range(8):
        temp=(int(key[i])+int(key[(i+4)%8])+int(key[(i+5)%8])+int(key[(i+6)%8])+int(key[(i+7)%8])+int(c[i]))%2
       # print(temp)
        temp=str(temp)
        b+=temp
    b=b[::-1]
    #print(b)
    return get_key(numbers,b[:4])+get_key(numbers,b[4:])

def SubWord(word):
    temp=''
    i=0
    while i<len(word):
        temp+=SubBytes(word[i]+word[i+1])
        i+=2
    return temp

def KeyExpansion(m):
    RCon=['01000000','02000000','04000000','08000000','10000000','20000000','40000000','80000000','1B000000','36000000']
    i=0
    key=[]
    while i<16:
        key.append(m[i*2]+m[i*2+1])
        i+=1
    w=[]
    for i in range(0,4):
        w.append(key[4*i]+key[4*i+1]+key[4*i+2]+key[4*i+3])
        #print(w[i])
    #temp=SubWord(RotWord(w[0]))
    #temp=hex2Bin(temp)
    #temp=w[0]
    #temp=int(hex2Bin8(SubWord(RotWord(temp))),2)|int(hex2Bin8(RCon[i//4-1]),2)
    for i in range(4,44):
        temp=w[i-1]
        
        binnum=int(hex2Bin8(temp),2)
        if(i%4==0):
            binnum=int(hex2Bin8(SubWord(RotWord(temp))),2)^int(hex2Bin8(RCon[i//4-1]),2)
        wapp=hex((int(hex2Bin8(w[i-4]),2)^binnum))
        wapp=wapp[2:].upper()
        zernum=8-len(wapp)
        while zernum:
            wapp='0'+wapp
            zernum-=1
        w.append(wapp)
    return w

m='2B7E151628AED2A6ABF7158809CF4F3C3A'
key=KeyExpansion(m)
print(key)