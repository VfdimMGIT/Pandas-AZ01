import pandas as pd
#df = pd.read_csv('Mobiles Dataset (2025).csv')
#df = pd.read_csv('Mobiles Dataset (2025).csv', encoding='utf-8', errors='replace')
encodings = ['utf-8', 'latin1', 'ISO-8859-1', 'cp1252', 'utf-16']

for encoding in encodings:
    try:
        df = pd.read_csv('Mobiles Dataset (2025).csv', encoding=encoding)
        print(f"Успешно загружено с кодировкой: {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Ошибка с кодировкой: {encoding}")
print(df.head())
print(df.info())
print(df.describe())
