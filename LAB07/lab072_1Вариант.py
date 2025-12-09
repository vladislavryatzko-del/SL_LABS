import json
from collections import Counter

def analyze_json_file():
    with open('1.json', 'r') as f:
        data = json.load(f)
    
    users = data['users']
    
    print(f"Всего пользователей: {len(users)}")
    
    def find_by_surname(prefix):
        return [u for u in users if u['surname'].lower().startswith(prefix.lower()[:3])]
    
    avg_age = sum(u['age'] for u in users) / len(users)
    
    languages = Counter(u['language'] for u in users)
    
    english_users = [u for u in users if u['language'] == 'English']
    output_data = {"users": english_users}
    
    with open('out.json', 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"\n1. Средний возраст: {avg_age:.1f}")
    print("\n2. Языки:", dict(languages))
    print(f"\n3. Англоговорящих пользователей: {len(english_users)}")
    print("   Сохранено в out.json")
    
    print("\n4. Пример поиска (фамилии на 'Smi'):")
    for user in find_by_surname('Smi'):
        print(f"   - {user['name']} {user['surname']}")

analyze_json_file()