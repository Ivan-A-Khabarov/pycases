def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')
    while choice != 7:
        try:
            if choice == 1:
                print_result(phone_book)
            elif choice == 2:
                last_name = input('Введите фамилию: ')
                print(find_by_last_name(phone_book, last_name))
            elif choice == 3:
                last_name = input('Введите фамилию: ')
                new_number = input('Введите новый номер: ')
                print(change_number(phone_book, last_name, new_number))
            elif choice == 4:
                last_name = input('Введите фамилию: ')
                print(delete_by_lastname(phone_book, last_name))
            elif choice == 5:
                number = input('Введите номер: ')
                print(find_by_number(phone_book, number))
            elif choice == 6:
                user_data = input('Введите новые данные: ')
                add_user(phone_book, user_data)
                write_txt('phonebook.txt', phone_book)

        except ValueError:
            print("Введите корректное значение.")
        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменить номер абонента по фамилии\n"
          "4. Удалить абонента по фамилии\n"
          "5. Найти абонента по номеру телефона\n"
          "6. Сохранить справочник/добавить данные в текстовом формате\n"
          "7. Закончить работу.")
    choice = int(input())
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))  # Исправлено добавление записи в справочник
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def find_by_last_name(phone_book, last_name):
    found_contacts = []

    for contact in phone_book:
        if contact['Фамилия'] == last_name:
            found_contacts.append(contact)

    if not found_contacts:
        return f"Абонент с фамилией '{last_name}' не найден."
    else:
        return found_contacts

def print_result(phone_book):
    if not phone_book:
        print("Справочник пуст.")
    else:
        print("\nСправочник:")
        for contact in phone_book:
            print(f"Фамилия: {contact['Фамилия']}, Имя: {contact['Имя']}, Телефон: {contact['Телефон']}, Описание: {contact['Описание']}")

def change_number(phone_book, last_name, new_number):
    contact_found = False

    for contact in phone_book:
        if contact['Фамилия'] == last_name:
            contact['Телефон'] = new_number
            contact_found = True
            break

    if contact_found:
        return f"Номер телефона для абонента с фамилией '{last_name}' успешно изменен."
    else:
        return f"Абонент с фамилией '{last_name}' не найден."

def delete_by_lastname(phone_book, last_name):
    for contact in phone_book:
        if contact['Фамилия'] == last_name:
            phone_book.remove(contact)
            return f"Абонент с фамилией '{last_name}' успешно удален из справочника."

    return f"Абонент с фамилией '{last_name}' не найден в справочнике."

def find_by_number(phone_book, number):
    found_contacts = []

    for contact in phone_book:
        if contact['Телефон'] == number:
            found_contacts.append(contact)

    if not found_contacts:
        return f"Абонент с номером телефона '{number}' не найден."
    else:
        return found_contacts

def add_user(phone_book, user_data):
    user_data_list = user_data.split(',')
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    if len(user_data_list) != len(fields):
        print("Неверное количество полей для добавления абонента.")
        return

    new_user = dict(zip(fields, user_data_list))
    phone_book.append(new_user)
    print(f"Абонент {new_user['Фамилия']} успешно добавлен в справочник.")

work_with_phonebook()
