# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:17:34 2021

@author: Mr2
"""

ans=0
for b in range(21):
    ans=b+ans
    print("Sum of first",b,"integers is",ans)

"""
Note:- 
here we are using loop plus summition of integers upto 20, as we
know b takes values exluding 21(final or target)

if we only want the final ans the 'print' should be commanded without 
indentation(tab{   } before print).

"""
