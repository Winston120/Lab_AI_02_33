# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:50:46 2019

@author: Vitaliy
"""
a=[]
s=0
n=int(input())
for i in range(n):
    a.append(int(input()))
    s+=a[i]
s=s/len(a)
print(s)
print("Bilshi za seredne")
for i in range(n):
    if a[i]>s:
        print(a[i])
