# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления 
# данных. Пользователь также может ввести имя или фамилию, и Вы должны 
# реализовать функционал для изменения и удаления данных.

# Задача №49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате 
# .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны 
# находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить запись в справочнике\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def read(filename):
    data=[]
    data1=["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(data1, line.strip().split(',')))
            data.append(record)
    print(data)



def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s=''
            for j in data[i].values():
                s+=j+','
            fout.write(f'{s[:-1]}\n')

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s=''
            for j in data[i].values():
                s+=j+','
            fout.write(f'{s[:-1]}\n')

def find_by_name(data: list, last_name: str)->str:
    for el in data:
        if el.get("Фамилия") == last_name:
            return el.get("Телефон")
    return "Нет данных"

def find_by_number(data: list, phone_number: str)->str:
    for el in data:
        if el.get("Телефон") == phone_number:
            return f'{el.get("Фамилия")},{el.get("Имя")}'
    return "Нет данных"

def del_line():
    filename=open('phone.txt')
    str=input('Введите данные для удаления: ')
    count=0
    lines=filename.readlines()
    str_for_del=''
    for el in lines:
        if str in el:
            str_for_del=el
            el=''
            count+=1
    if count==0:
        print('Нет данных')
    else:
        filename=open('phone.txt', 'r').read()
        filename=filename.replace(str_for_del,'')
        filename_2=open('phone.txt', 'w')
        filename_2.write(filename)
      

def work_phonebook():
    choice=show_menu()
    phone_book=read('phone.txt')
    while (choice !=7):
        if choice==1:
            read(phone_book)
        elif choice==2:
            name = input(" Введите фамилию: ")
            print(find_by_name(phone_book, name))
        elif choice==3:
            number = input("Введите телефон: ")
            print(find_by_number(phone_book, number))
        elif choice==4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_txt('phone.txt', phone_book)
        elif choice==5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        elif choice==6:
            file_name = get_file_name()
            del_line(file_name, phone_book)
        choice = show_menu()

work_phonebook()
