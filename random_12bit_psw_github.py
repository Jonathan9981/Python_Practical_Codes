# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 23:29:18 2021

@author: John.X
"""
#%%
import random

# 1.全密码字符串
txt1 = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
txt2 = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
suff1 = 'suff1_'
suff2 = 'suff2_'

# 2.字符串转列表
alpha_num_list = list(txt1)

# 3.生成10组密码
for i in range(50):
    password = suff1 + suff2 + ""  
    # 15位数
    for j in range(16):
        password += random.choice(alpha_num_list)
    # 打印该组随机密码
    print(password)

#%%
