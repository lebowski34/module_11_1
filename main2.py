import pandas as pd

data = pd.read_csv('data.txt', delimiter=' ')

print("Заголовки столбцов:")
print(data.columns)

print("Первые 5 строк данных:")
print(data.head())

if 'age' in data.columns:
    filtered_data = data[data['age'] > 30]
    print("Фильтрованные данные (возраст > 30):")
    print(filtered_data)

    average_age = data['age'].mean()
    print(f"Средний возраст: {average_age}")
else:
    print("Столбец 'age' не найден в данных.")
