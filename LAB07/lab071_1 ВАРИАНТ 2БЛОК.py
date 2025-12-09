import csv
from collections import defaultdict

def read_and_display_csv(filename):
    """Читает CSV файл и выводит его содержимое в формате 'Ключ → Значение'"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            print("СОДЕРЖИМОЕ ФАЙЛА CSV:")
            
            print("Заголовки столбцов:", reader.fieldnames)
            print()
            
            for i, row in enumerate(reader, 1):
                print(f"--- Книга {i} ---")
                for key, value in row.items():
                    print(f"  {key} → {value}")
                print()
            
            file.seek(0)  
            next(reader)   
            return list(reader)  
            
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []

def find_oldest_newest_book(books):
    """Находит самую старую и самую новую книгу по году издания"""
    if not books:
        print("Нет данных для анализа")
        return None, None
    
    valid_books = []
    for book in books:
        try:
            year = int(book['Year'])
            valid_books.append((book, year))
        except (ValueError, KeyError):
            continue
    
    if not valid_books:
        print("Нет корректных данных о годах издания")
        return None, None
    
    oldest_book, oldest_year = min(valid_books, key=lambda x: x[1])
    newest_book, newest_year = max(valid_books, key=lambda x: x[1])
    
    return oldest_book, newest_book

def calculate_total_pages(books):
    """Подсчитывает общее количество страниц во всех книгах"""
    if not books:
        return 0
    
    total_pages = 0
    for book in books:
        try:
            pages = int(book['Pages'])
            total_pages += pages
        except (ValueError, KeyError):
            continue
    
    return total_pages

def calculate_average_price(books):
    """Вычисляет среднюю цену книг"""
    if not books:
        return 0
    
    total_price = 0
    count = 0
    
    for book in books:
        try:
            price_str = book['Price'].replace('$', '').replace(',', '.').strip()
            price = float(price_str)
            total_price += price
            count += 1
        except (ValueError, KeyError, AttributeError):
            continue
    
    return total_price / count if count > 0 else 0

def count_books_by_genre(books):
    """Подсчитывает количество книг по жанрам"""
    if not books:
        return {}
    
    genre_count = defaultdict(int)
    
    for book in books:
        try:
            genre = book['Genre'].strip()
            if genre:
                genre_count[genre] += 1
        except (KeyError, AttributeError):
            continue
    
    return dict(genre_count)

def create_test_csv(filename='1.csv'):
    """Создает тестовый CSV файл с данными о книгах"""
    test_data = [
        ['Title', 'Author', 'Year', 'Genre', 'Pages', 'Price'],
        ['Война и мир', 'Лев Толстой', '1869', 'Роман', '1225', '$45.99'],
        ['Преступление и наказание', 'Федор Достоевский', '1866', 'Роман', '671', '$32.50'],
        ['1984', 'Джордж Оруэлл', '1949', 'Антиутопия', '328', '$25.99'],
        ['Мастер и Маргарита', 'Михаил Булгаков', '1967', 'Роман', '480', '$38.75'],
        ['Гарри Поттер и философский камень', 'Джоан Роулинг', '1997', 'Фэнтези', '223', '$29.99'],
        ['Маленький принц', 'Антуан де Сент-Экзюпери', '1943', 'Повесть', '96', '$18.50'],
        ['Властелин колец', 'Дж. Р. Р. Толкин', '1954', 'Фэнтези', '1178', '$49.99'],
        ['Убить пересмешника', 'Харпер Ли', '1960', 'Роман', '281', '$27.80'],
        ['Гордость и предубеждение', 'Джейн Остин', '1813', 'Роман', '432', '$31.25'],
        ['Великий Гэтсби', 'Фрэнсис Скотт Фицджеральд', '1925', 'Роман', '218', '$23.99']
    ]
    
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(test_data)
    
    print(f"Тестовый файл '{filename}' создан успешно!")
    print(f"Добавлено {len(test_data)-1} книг")

def main():
    import os
    csv_file = '1.csv'
    
    if not os.path.exists(csv_file):
        print(f"Файл '{csv_file}' не найден.")
        create = input("Создать тестовый файл с данными о книгах? (да/нет): ")
        if create.lower() in ['да', 'д', 'y', 'yes']:
            create_test_csv(csv_file)
        else:
            print("Пожалуйста, создайте файл '13.csv' вручную и запустите программу снова.")
            return
    
    print("АНАЛИЗ ФАЙЛА С КНИГАМИ")
    
    books = read_and_display_csv(csv_file)
    
    if not books:
        print("Нет данных для анализа")
        return
    
    print("АНАЛИЗ ДАННЫХ О КНИГАХ")
    
    oldest_book, newest_book = find_oldest_newest_book(books)
    
    if oldest_book and newest_book:
        print("\n1. САМАЯ СТАРАЯ КНИГА:")
        print(f"   Название: {oldest_book['Title']}")
        print(f"   Автор: {oldest_book['Author']}")
        print(f"   Год издания: {oldest_book['Year']}")
        print(f"   Жанр: {oldest_book['Genre']}")
        
        print("\n2. САМАЯ НОВАЯ КНИГА:")
        print(f"   Название: {newest_book['Title']}")
        print(f"   Автор: {newest_book['Author']}")
        print(f"   Год издания: {newest_book['Year']}")
        print(f"   Жанр: {newest_book['Genre']}")
    
    total_pages = calculate_total_pages(books)
    print(f"\n3. ОБЩЕЕ КОЛИЧЕСТВО СТРАНИЦ ВО ВСЕХ КНИГАХ:")
    print(f"   {total_pages} страниц")
    
    avg_price = calculate_average_price(books)
    print(f"\n4. СРЕДНЯЯ ЦЕНА КНИГИ:")
    print(f"   ${avg_price:.2f}")
    
    genre_stats = count_books_by_genre(books)
    print("\n5. КОЛИЧЕСТВО КНИГ ПО ЖАНРАМ:")
    
    if genre_stats:
        for genre, count in sorted(genre_stats.items()):
            print(f"   {genre}: {count} книг")
        
        most_common_genre = max(genre_stats.items(), key=lambda x: x[1])
        print(f"\n   Самый популярный жанр: '{most_common_genre[0]}' ({most_common_genre[1]} книг)")
    else:
        print("   Нет данных о жанрах")
    
    print("ДОПОЛНИТЕЛЬНАЯ СТАТИСТИКА")
    
    print(f"Общее количество книг: {len(books)}")
    
    if books:
        years = []
        for book in books:
            try:
                years.append(int(book['Year']))
            except (ValueError, KeyError):
                continue
        
        if years:
            print(f"Диапазон лет издания: {min(years)} - {max(years)}")
            print(f"Разброс лет: {max(years) - min(years)} лет")
    
    pages_data = []
    for book in books:
        try:
            pages = int(book['Pages'])
            pages_data.append((book['Title'], pages))
        except (ValueError, KeyError):
            continue
    
    if pages_data:
        thickest = max(pages_data, key=lambda x: x[1])
        thinnest = min(pages_data, key=lambda x: x[1])
        
        print(f"\nСамая толстая книга: '{thickest[0]}' ({thickest[1]} стр.)")
        print(f"Самая тонкая книга: '{thinnest[0]}' ({thinnest[1]} стр.)")

if __name__ == "__main__":
    main()