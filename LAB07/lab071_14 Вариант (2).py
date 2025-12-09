import shelve

car_sales = {
    "Toyota": {"США": 2118000, "Китай": 1620000, "Россия": 98000, "Германия": 85000, "Франция": 72000, "Япония": 1450000},
    "Volkswagen": {"США": 625000, "Китай": 3180000, "Россия": 112000, "Германия": 530000, "Франция": 210000, "Япония": 58000},
    "Hyundai": {"США": 738000, "Китай": 785000, "Россия": 153000, "Германия": 125000, "Франция": 68000, "Япония": 42000},
    "Ford": {"США": 2020000, "Китай": 480000, "Россия": 85000, "Германия": 180000, "Франция": 95000, "Япония": 35000},
    "Honda": {"США": 1468000, "Китай": 1550000, "Россия": 42000, "Германия": 75000, "Франция": 51000, "Япония": 720000},
    "BMW": {"США": 305000, "Китай": 846000, "Россия": 48000, "Германия": 265000, "Франция": 115000, "Япония": 68000},
    "Mercedes": {"США": 318000, "Китай": 775000, "Россия": 52000, "Германия": 285000, "Франция": 98000, "Япония": 62000}
}

print("Марки автомобилей и суммарный объем продаж в 6 странах:")

for car, sales in car_sales.items():
    total_sales = sum(sales.values())
    print(f"{car}: {total_sales:,} автомобилей")

print("Страны с максимальным и минимальным объемом продаж для каждой марки:")

for car, sales in car_sales.items():
    max_country = max(sales, key=sales.get)
    min_country = min(sales, key=sales.get)
    print(f"{car}:")
    print(f"  Максимум - {max_country}: {sales[max_country]:,}")
    print(f"  Минимум - {min_country}: {sales[min_country]:,}")

print("Объемы продаж автомобилей в России:")

for car, sales in car_sales.items():
    print(f"{car}: {sales['Россия']:,} автомобилей")

print("Автомобили с продажами в США > Китая более чем на 20%:")

for car, sales in car_sales.items():
    usa_sales = sales["США"]
    china_sales = sales["Китай"]
    
    if china_sales > 0:  
        percentage_diff = ((usa_sales - china_sales) / china_sales) * 100
        
        if usa_sales > china_sales * 1.2:  
            print(f"{car}:")
            print(f"  США: {usa_sales:,} | Китай: {china_sales:,}")
            print(f"  Разница: {percentage_diff:.1f}%")

print("\n" + "=" * 60)
print("Сохранение данных в файл с использованием shelve...")

with shelve.open('car_sales_data') as db:
    db['car_sales'] = car_sales
    db['metadata'] = {
        'total_brands': len(car_sales),
        'countries': list(car_sales['Toyota'].keys()),
        'description': 'Данные о продажах автомобилей по странам'
    }

print("Данные успешно сохранены в файл 'car_sales_data'")

print("Проверка чтения данных из файла shelve:")

with shelve.open('car_sales_data') as db:
    loaded_data = db['car_sales']
    metadata = db['metadata']
    
    print(f"Загружено марок автомобилей: {metadata['total_brands']}")
    print(f"Страны: {', '.join(metadata['countries'])}")
    print(f"Первая марка в базе: {list(loaded_data.keys())[0]}")