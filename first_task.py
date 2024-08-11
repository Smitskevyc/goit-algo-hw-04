def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            
            for line in file:
                # Розділяємо прізвище та зарплату
                name, salary = line.strip().split(',')
                # Додаємо зарплату до загальної суми
                total += int(salary)
                # Збільшуємо кількість розробників
                count += 1
            
            # Обчислюємо середню зарплату
            average = total / count if count != 0 else 0
            
            return total, average
            
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None, None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None, None

# Приклад використання функції
total, average = total_salary("path/to/salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
