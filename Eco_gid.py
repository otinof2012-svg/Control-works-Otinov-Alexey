import os

DATA_FILE = "eco_data.txt"

# Начальная база данных (формат: название|инструкция)
DEFAULT_DATA = [
    "батарейка|ОПАСНЫЕ ОТХОДЫ. Сдать в специальный бокс в магазине. Не выбрасывать в мусор!",
    "пластиковая бутылка|ПЛАСТИК. Снять крышку, смять. Выбросить в контейнер для пластика.",
    "стеклянная бутылка|СТЕКЛО. Промыть. Выбросить в контейнер для стекла.",
    "бумага|МАКУЛАТУРА. Удалить скрепки. Сдать в макулатуру.",
    "картон|МАКУЛАТУРА. Разрезать, сложить. Сдать в макулатуру.",
    "алюминиевая банка|МЕТАЛЛ. Промыть, смять. Выбросить в контейнер для металла.",
    "банановая кожура|ОРГАНИКА. Можно в компост или в общий мусор.",
    "лампа энергосберегающая|ОПАСНЫЕ ОТХОДЫ. Сдать в специальный пункт приёма. Не разбивать!",
    "одежда|ТЕКСТИЛЬ. Чистую одежду сдать в секонд-хенд или контейнер для одежды.",
    "чеки|ОБЩИЙ МУСОР. Чеки из термобумаги не перерабатываются."
]


def load_data():
    """Загружает данные из текстового файла"""
    data = {}

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and "|" in line:
                    name, instruction = line.split("|", 1)
                    data[name.lower()] = instruction
    else:
        # Создаём файл с начальными данными
        for item in DEFAULT_DATA:
            name, instruction = item.split("|", 1)
            data[name.lower()] = instruction
        save_data(data)

    return data


def save_data(data):
    """Сохраняет данные в текстовый файл"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for name, instruction in data.items():
            f.write(f"{name}|{instruction}\n")


def search(data):
    """Поиск предмета"""
    item = input("\nЧто хотите утилизировать? ").lower().strip()

    if not item:
        print("❌ Введите название!")
        return

    if item in data:
        print("\n" + "=" * 50)
        print(f"📦 {item.upper()}")
        print("=" * 50)
        print(data[item])
        print("=" * 50)
    else:
        print(f"\n❌ Не знаю предмет '{item}'")
        add = input("Хотите добавить его в базу? (да/нет): ").lower()
        if add == "да" or add == "yes" or add == "y":
            instruction = input("Куда и как выбрасывать? ")
            data[item] = instruction
            save_data(data)
            print(f"✅ Предмет '{item}' добавлен!")

def show_all(data):
    """Показывает все предметы в базе"""
    if not data:
        print("\n📋 База пуста!")
        return

    print("\n" + "=" * 50)
    print("📋 ВСЕ ПРЕДМЕТЫ В БАЗЕ:")
    print("=" * 50)

    for name in sorted(data.keys()):
        print(f"   • {name}")

    print("=" * 50)
    print(f"Всего: {len(data)} предметов")


def delete_item(data):
    """Удаляет предмет из базы"""
    if not data:
        print("\n📋 База пуста!")
        return

    show_all(data)
    item = input("\nВведите название для удаления: ").lower().strip()

    if item in data:
        del data[item]
        save_data(data)
        print(f"✅ Предмет '{item}' удалён!")
    else:
        print(f"❌ Предмет '{item}' не найден")


def show_help():
    """Показывает справку"""
    print("\n" + "=" * 50)
    print("📖 СПРАВКА")
    print("=" * 50)
    print("""
1. НАЙТИ ПРЕДМЕТ — введите название мусора, программа подскажет,
   куда его выбросить и как подготовить.

2. ВСЕ ПРЕДМЕТЫ — показывает список всего, что есть в базе.

3. ДОБАВИТЬ ПРЕДМЕТ — если программа не знает ваш предмет,
   вы можете добавить его сами.

4. УДАЛИТЬ ПРЕДМЕТ — удаляет предмет из базы.

5. ВЫХОД — завершает работу программы.
    """)
    print("=" * 50)


def main():
    """Главная функция"""
    data = load_data()

    print("\n" + "=" * 50)
    print("🌍 ЭКО-СПРАВОЧНИК")
    print("Помогаем планете вместе! 🌱")
    print("=" * 50)

    while True:
        print("\n" + "-" * 40)
        print("ГЛАВНОЕ МЕНЮ:")
        print("1. 🔍 Найти предмет")
        print("2. 📋 Все предметы")
        print("3. ➕ Добавить предмет")
        print("4. 🗑️ Удалить предмет")
        print("5. 📖 Справка")
        print("6. 🚪 Выход")
        print("-" * 40)

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            search(data)
        elif choice == "2":
            show_all(data)
        elif choice == "3":
            # Быстрое добавление
            name = input("\nНазвание предмета: ").lower().strip()
            if name:
                instr = input("Инструкция: ")
                data[name] = instr
                save_data(data)
                print(f"✅ Добавлено!")
            else:
                print("❌ Название не может быть пустым")
        elif choice == "4":
            delete_item(data)
        elif choice == "5":
            show_help()
        elif choice == "6":
            print("\n🌍 Спасибо, что заботитесь о планете! До свидания!")
            print("=" * 50)
            break
        else:
            print("❌ Неверный выбор. Введите число от 1 до 6.")


if __name__ == "__main__":
    main()
