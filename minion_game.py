# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:54:08 2020

@author: Shivraj
"""

string = 'BANANA'
vowels = 'AIEOU'
n = len(string)
k_score, s_score = 0,0

for i in range(n):

    if string[i] in vowels:
        k_score += n-i
    else:
        s_score += n-i

if k_score > s_score:
    print('Kevin', k_score)
elif s_score > k_score:
    print('Stuart', s_score)
else:
    print('Draw')
