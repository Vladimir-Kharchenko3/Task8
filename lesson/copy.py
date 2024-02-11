# def copy_record(source_filename, destination_filename, record_number):
#     try:
#         with open(source_filename, 'r', encoding='utf-8') as source_file:
#             data = source_file.readlines()
#             record_to_copy = data[(record_number - 1) * 5:record_number * 5]

#         with open(destination_filename, 'a', encoding='utf-8') as destination_file:
#             destination_file.writelines(record_to_copy)

#         print(f'Запись {record_number} скопирована из {source_filename} в {destination_filename}.')
#     except FileNotFoundError:
#         print(f"Ошибка: Файл {source_filename} не найден.")

# def print_data(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             data = file.readlines()
#             print('Содержимое файла:')
#             print(''.join(data))
#     except FileNotFoundError:
#         print(f"Ошибка: Файл {filename} не найден.")

# def interface():
#     print('Добрый день! Это бот-помощник.\n'
#           'Что вы хотите сделать?\n'
#           '1 - Записать данные\n'
#           '2 - Вывести данные\n'
#           '3 - Скопировать запись из одного файла в другой')
    
#     command = int(input('Ваш выбор: '))

#     while command < 1 or command > 3:
#         command = int(input('Ошибка! Ваш выбор: '))

#     if command == 1:
#         input_data()
#     elif command == 2:
#         print_data('data_first_variant.csv')
#         print_data('data_second_variant.csv')
#     elif command == 3:
#         record_number = int(input('Введите номер записи, которую нужно скопировать: '))
#         copy_record('data_first_variant.csv', 'data_second_variant.csv', record_number)

# # Остальной код остается без изменений
# # ...

# # Вызов функции interface() для начала взаимодействия с пользователем
# interface()
