import pandas as pd

#Загрузите набор данных из CSV-файла в DataFrame.
df = pd.read_csv('1990sClassicHits.csv')

# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
print("Первые 5 строк данных:")
print(df.head(5))

# Выведите информацию о данных (.info())
print("\nИнформация о данных:")
print(df.info())

# и статистическое описание (.describe()).
print("\nСтатистическое описание данных:")
print(df.describe())

#Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

# Загрузка данных из CSV файла
df = pd.read_csv('dz.csv')

# Группировка данных по городу и вычисление средней зарплаты
average_salary_by_city = df.groupby('City')['Salary'].mean().reset_index()

# Вывод результатов
print("Средняя зарплата по городам:")
print(average_salary_by_city)