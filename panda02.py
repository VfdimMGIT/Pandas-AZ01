#Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv
import pandas as pd
# Загрузка данных из CSV-файла (учитываем возможную кириллицу в данных)
try:
    df = pd.read_csv('dz.csv', encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv('dz.csv', encoding='cp1251')  # Альтернативная кодировка

# Удаление строк с пропущенными значениями в Salary (если нужно)
df = df.dropna(subset=['Salary'])

# Группировка по городам и расчёт средней зарплаты
average_salary_by_city = df.groupby('City')['Salary'].mean().reset_index()

# Вывод результата
print(average_salary_by_city)
