def get_cats_info(path):
    try:
        cats_list = []
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на ID, ім'я та вік
                cat_id, name, age = line.strip().split(',')
                
                # Формуємо словник для кожного кота
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                
                # Додаємо словник до списку
                cats_list.append(cat_info)
        
        return cats_list
    
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []

# Приклад використання функції
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
