# Телефонный справочник с функцией изменения и удаления данных

phonebook = {"Иванов": {"номер": "8-911-111-11-11", "адрес": "ул. Ленина, 10"},
             "Петров": {"номер": "8-922-222-22-22", "адрес": "ул. Гагарина, 25"}}

# Функция для добавления нового контакта в телефонную книгу
def add_contact():
    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона: ")
    address = input("Введите адрес: ")
    phonebook[name] = {"номер": number, "адрес": address}
    print("Контакт успешно добавлен")

# Функция для изменения данных контакта
def edit_contact():
    name = input("Введите имя или фамилию контакта: ")
    if name in phonebook:
        number = input("Введите новый номер телефона: ")
        address = input("Введите новый адрес: ")
        phonebook[name] = {"номер": number, "адрес": address}
        print("Контакт успешно изменен")
    else:
        print("Контакт не найден")

# Функция для удаления контакта из телефонной книги
def delete_contact():
    name = input("Введите имя или фамилию контакта: ")
    if name in phonebook:
        del phonebook[name]
        print("Контакт успешно удален")
    else:
        print("Контакт не найден")

# Главная функция для работы с телефонной книгой
def phonebook_app():
    while True:
        action = input("\nВыберите действие:\n1 - Добавить контакт\n2 - Изменить контакт\n3 - Удалить контакт\n4 - Вывести список контактов\n5 - Выйти из приложения\n")
        if action == "1":
            add_contact()
        elif action == "2":
            edit_contact()
        elif action == "3":
            delete_contact()
        elif action == "4":
            for name, data in phonebook.items():
                print("{0}: {1}, {2}".format(name, data["номер"], data["адрес"]))
        elif action == "5":
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

# Запуск приложения
phonebook_app()