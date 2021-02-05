# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:06:41 2021

@author: Mr2
"""

n=input("Your Name Please: ")
print("Hi",n,"!")
print("Hope, you are doing well,",n+". Let me tell your age. According to 01.01.2021")
d,m,y=input("What is your date of birth [IN DD.MM.YYYY FORMAT]" ).split(".")
d=int(d)
m=int(m)
y=int(y)
d=32-d
m=12-m
y=2020-y
if(y>100):
    print("You are more than 100years old \n AND ")
    print("You are",y,"years",m,"month(s) and",d,"day(s) old. ")
else:
    print("You are",y,"years",m,"month(s) and",d,"day(s) old. ")

    

"""
print("Mind the uses of ',' and '+'. Here if you use former you'l have a space in place of it, and if yout use latter you'l have no space instead you'l find it adjucent to the next thing or string.")
"""
