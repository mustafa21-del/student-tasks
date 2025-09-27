import pandas as pd
import random

def generate_students(num_students=100):
    # Список імен (можна доповнити)
    names = ["Іван", "Марія", "Олег", "Андрій", "Наталя", "Віктор", "Софія", "Юлія", "Дмитро", "Оксана"]
    
    data = {
        "Ім’я": [random.choice(names) for _ in range(num_students)],
        "Вік": [random.randint(18, 25) for _ in range(num_students)],
        "Математика": [random.randint(0, 100) for _ in range(num_students)],
        "Програмування": [random.randint(0, 100) for _ in range(num_students)]
    }
    
    df = pd.DataFrame(data)
    return df

def process_students(df):
    # Додаємо колонку середнього балу
    df["Середній бал"] = df[["Математика", "Програмування"]].mean(axis=1).round(2)
    
    # Додаємо колонку статусу
    df["Status"] = df["Середній бал"].apply(lambda x: "Pass" if x >= 75 else "Fail")
    
    return df

def main():
    # Генеруємо дані
    df = generate_students()
    
    # Обробляємо таблицю
    df = process_students(df)
    
    # Вибираємо студентів з середнім балом > 80
    top_students = df[df["Середній бал"] > 80]
    
    # Рахуємо кількість Pass/Fail
    status_counts = df["Status"].value_counts()
    
    print("=== Перші 10 студентів ===")
    print(df.head(10))
    
    print("\n=== Студенти з середнім балом > 80 ===")
    print(top_students)
    
    print("\n=== Статистика по статусу ===")
    print(status_counts)
    
    # Запис у CSV
    df.to_csv("students_results.csv", index=False, encoding="utf-8-sig")
    print("\n✅ Дані збережено у файл students_results.csv")

if __name__ == "__main__":
    main()
