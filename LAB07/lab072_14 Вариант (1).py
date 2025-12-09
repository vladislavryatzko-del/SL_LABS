def starts_with_vowel(word):
    vowels = 'аеёиоуыэюяaeiou'
    if len(word) > 0:
        return word[0].lower() in vowels
    return False

def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()
            
            results = []
            
            for line_num, line in enumerate(lines, 1):
                words = line.strip().split()
                
                vowel_count = 0
                
                for word in words:
                    clean_word = word.strip('.,!?;:"\'()[]{}')
                    
                    if clean_word: 
                        if starts_with_vowel(clean_word):
                            vowel_count += 1
                
                results.append((line_num, vowel_count))
                
                print(f"Строка {line_num}: {vowel_count} слов(а) начинается на гласную")
            
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write("Результат подсчета слов, начинающихся на гласную букву:\n")
            output_file.write("=" * 60 + "\n\n")
            
            for line_num, count in results:
                output_file.write(f"Строка {line_num}: {count} слов(а) начинается на гласную\n")
            
            total_words = sum(count for _, count in results)
            output_file.write("\n" + "=" * 60 + "\n")
            output_file.write(f"ИТОГО: {total_words} слов начинается на гласную букву\n")
            
        print(f"\nРезультаты успешно записаны в файл 'output.txt'")
        print(f"Всего найдено {total_words} слов, начинающихся на гласную")
        
    except FileNotFoundError:
        print("Ошибка: Файл 'input.txt' не найден!")
        print("Пожалуйста, создайте файл 'input.txt' с текстом для анализа.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def create_test_file():
    """Создает тестовый файл input.txt с примером текста"""
    test_text = """Это пример текста для анализа.
Здесь нужно посчитать слова, начинающиеся на гласную.
А это уже третья строка текста.
Эх, ох, ух - вот такие междометия.
Яблоко, апельсин и orange - фрукты.
В этом предложении ровно пять слов на гласную.
Последняя строка для завершения теста."""

    with open('input.txt', 'w', encoding='utf-8') as f:
        f.write(test_text)
    
    print("Тестовый файл 'input.txt' создан успешно!")
    print("Содержимое файла:")
    print(test_text)

if __name__ == "__main__":
    import os
    
    if not os.path.exists('input.txt'):
        print("Файл 'input.txt' не найден.")
        create = input("Создать тестовый файл? (да/нет): ")
        if create.lower() in ['да', 'д', 'y', 'yes']:
            create_test_file()
        else:
            print("Пожалуйста, создайте файл 'input.txt' вручную и запустите программу снова.")
    else:
        main()