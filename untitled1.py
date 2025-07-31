# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 10:12:29 2025

@author: Lenovo
"""

for h in range (1,5):
    print("*"*h)
    
for h in range(5,0,-1):
    print("*"*h)

for row in range(1,5):
    for col in range(0,row):
        print("*",end=" ")
    print()
    
for row in range(1,6):
    for col in range(1,row+1):
        print(col,end=" ")
    print()
    
for row in range (6,0,-1):
    for col in range (1,row):
        print(col,end=" ")
    print()
    
    
for row in range (0,5):
    for col in range(0,row):
        print(5,end=" ")
    print()
    
    
#    
for row in range(1,6):
    for col in range(6,row,-1):
        print(row,end=" ")
    print()
    

for row in range(1,6):
    for col in range(row,0,-1):
        print(col,end=" ")
    print()
    
    
for row in range(7,0,-1):
    for space  in range(7,row,-1):
        print(" ",end="")   
    for col in range(row,0,-1):
        print("*",end="")
    print() 
    

for row in range(0,7): 
    for space in range (7,row,-1):
        print(" ",end=" ")
    for col in range (0,row):
        print("*",end=" ")
    print()
    

for row in range(0,6):
    for space in range (6,row,-1):
        print(" ",end=" ")
    for col in range(0,row):
        print("*",end=" ")
    print()    
for row in range(6,0,-1):
    for space in range(6,row,-1):
        print(" ",end=" ")
    for col in range(row,0,-1):
        print("*",end=" ")
    print()


name='python'
for value in range(0,len(name)+1):
    print(name[0:value])
    
    
    
    

    
    
    
    
    
    
    
    
    