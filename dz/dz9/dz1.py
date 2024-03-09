import pandas as pd

# Считываем данные из файла
data = pd.read_csv('california_housing_train.csv')

# Фильтруем строки по условию "количество людей от 0 до 500" и вычисляем среднюю стоимость дома
filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]
avg = filtered_data['median_house_value'].mean()

print("Средняя стоимость дома с населением от 0 до 500:", avg)