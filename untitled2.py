# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 03:20:05 2020

@author: opres
"""

def stem1(s):
    count=0
    special_cases={'killing':'kill','party':'parti',}
    if len(s)>6:
        count+=1
        if s[-4::]=='ness':
            if s[-5]==s[-6]:
                s=s[:5]
            else:
                s=s[:-4]
        if s[-3::]=='ing':
            if s[-4]==s[-5]:
                s=s[:-4]
            else:
                s=s[:-3]
        if s[-1::]=='s':
            if s[-2]==s[-3]:
                s=s[:-2]
            else:
                s=s[:-1]
        if s[-2::]=='er':
            if s[-3]==s[-4]:
                s=s[:-3]
            else:
                s=s[:-2]
        
        if s[-2::]=='es':
            if s[-3]==s[-4]:
                s=s[:-3]
            else:
                s=s[:-2]   
        if s[-3::]=='ful':
            if s[-4]==s[-5]:
                s=s[:-4]
            else:
                s=s[:-3]
        if s[-3::]=='ely':
            if s[-4]==s[-5]:
                s=s[:-4]
            else:
                s=s[:-3]
        if s[-2::]=='ly':
            if s[-3]==s[-4]:
                s=s[:-3]
            else:
                s=s[:-2]     
        if s[-1::]=='y':
            if s[-2]==s[-3]:
                s=s[:-2]
            else:
                s=s[:-1]
        if s[-3::]=='ion':
            if s[-4]==s[-5]:
                s=s[:-4]
            else:
                s=s[:-3]
        if s[-4::]=='ment':
            if s[-5]==s[-6]:
                s=s[:5]
            else:
                s=s[:-4]
            
       
       
       
            
    return s