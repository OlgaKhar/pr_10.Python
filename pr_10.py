'''
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
one_hot_data = pd.DataFrame()
one_hot_data['robot'] = [1 if x == 'robot' else 0 for x in data['whoAmI']]
one_hot_data['human'] = [1 if x == 'human' else 0 for x in data['whoAmI']]

print(one_hot_data.head())