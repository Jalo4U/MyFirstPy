# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:11:29 2021

@author: Mr2
"""

n=input("Your Name Please: ")
print("Hi",n,"!")
print("Hope, you are doing well,",n+". Let me tell your age. According to Your given date.")
d,m,y=input("What is your date of birth [IN DD.MM.YYYY FORMAT]" ).split(".")
cd,cm,cy=input("You want your age at the date of[IN DD.MM.YYYY FORMAT]: ").split(".")

d=int(d)
m=int(m)
y=int(y)
cd=int(cd)
cm=int(cm)
cy=int(cy)
if(d>cd):
    cd=cd+30
    m=m+1
if(m>cm):
    cm=cm+12
    y=y+1
d=cd-d
m=cm-m
y=cy-y
if(y>100):
    print("You are more than 100years old \n AND ")
    print("You are",y,"years",m,"month(s) and",d,"day(s) old. Excluding given day.")
else:
    print("You are",y,"years",m,"month(s) and",d,"day(s) old. Ecluding given day.")