# -*- coding:utf-8 -*-
from vocabulary import words_dict as dict
import random
import os


while True:
    for keys in dict.keys():
        key_list = random.sample(dict.keys(), 1)
        key = key_list[0]
        print('='*50)
        print(key, "\t", dict[key])
        os.system('pause')

