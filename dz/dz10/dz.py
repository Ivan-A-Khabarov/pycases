import pandas as pd

# Исходные данные
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one hot encoding
one_hot = pd.get_dummies(data['whoAmI'])
data = pd.concat([data, one_hot], axis=1)
data.drop('whoAmI', axis=1, inplace=True)

data.head()



