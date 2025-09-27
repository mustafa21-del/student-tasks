import random

def generate_grades(num_students=100, num_subjects=3):
    grades = [[random.randint(0, 100) for _ in range(num_subjects)] for _ in range(num_students)]
    return grades

def calculate_averages(grades):
    averages = [round(sum(student) / len(student), 2) for student in grades]
    return averages

def main():
    grades = generate_grades()
    print("Оцінки студентів (перші 10):")
    for i, student in enumerate(grades[:10], start=1):
        print(f"Студент {i}: {student}")

    averages = calculate_averages(grades)
    print("\nСередні бали (перші 10):")
    for i, avg in enumerate(averages[:10], start=1):
        print(f"Студент {i}: {avg}")

    group_avg = round(sum(averages) / len(averages), 2)
    best = max(averages)
    worst = min(averages)

    print("\n=== Статистика по групі ===")
    print(f"Середній бал групи: {group_avg}")
    print(f"Найвищий середній бал: {best}")
    print(f"Найнижчий середній бал: {worst}")

if __name__ == "__main__":
    main()
