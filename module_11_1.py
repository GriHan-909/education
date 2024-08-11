'''requests, pandas, matplotlib'''

import requests


response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    data = response.json()
    # Вывод первых трех постов в консоль
    for post in data[:3]:
        print(f"Title: {post['title']}\nBody: {post['body']}\n")
else:
    print(f"Failed to retrieve data: {response.status_code}")



import pandas as pd

# Чтение данных из Excel-файла
'''Для работы с excel файлом требуется дополнительно установить
   библиотеку openpyxl'''
df = pd.read_excel('test1.xlsx', sheet_name='Лист1')

# Вывод первых 6 строк таблицы
print("Первоначальные данные:")
print(df.head(n=6))

# Выполним простой анализ: посчитаем среднее значение по столбцу числового типа
mean_values = df.mean(numeric_only=True)

print("\nСредние значения по столбцу age:")
print(mean_values)

# Применим фильтр: выберем строки, где значение в столбце 'age' больше 35
filtered_df = df[df['age'] > 35]

print("\nОтфильтрованные данные (age > 35):")
print(filtered_df)



import matplotlib.pyplot as plt

# Создание данных для визуализации
years = [i for i in range(2011, 2025)]
values = [3.3, 6.69, 115.455, 492.075, 248.315, 581.29, 2576.36, 6945.66, 7783.71, 9701.64, 47908.09, 23136.75, 27745.69, 63347.66]

# Построение линейного графика
plt.plot(years, values, marker='o', color='b', linestyle='--')

# Добавление заголовка и подписей к осям
plt.title('Курс биткойна (BTC)')
plt.xlabel('Year')
plt.ylabel('Value $')

# Добавление сетки
plt.grid(True)

# Показать график
plt.show()