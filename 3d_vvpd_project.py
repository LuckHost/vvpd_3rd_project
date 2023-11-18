import pickle
""" importing pickle 
unexpected, isn't it?"""

def first_task():
    """ get dict from the file """
    path = input("Укажите путь до файла: ")
    try:
        with open(path, "r", encoding="utf-8") as file:
            return pickle.load(file)
    except FileNotFoundError:
        print("Что-то пошло не так,",
              " проверьте указанный путь")
        return None

def second_task(data, name = ""):
    """ find dict by name """
    if name in data:
        print("Название: "+ name + "\n",
              "Цена: ", data[name]["price"]+ "\n",
              "Осталось: ", data[name]["surplus"]+ "\n",
            "Ед. измерения: ", data[name]["units"])
        return True
    print("Товара ", name, " нет в списке")
    return False

def third_task(data, number, operation):
    """ surplus count filter """
    for i in data:
        # operation = True --> ">"
        # False --> "<"
        if (int(data[i]["surplus"]) > number) == operation:
            print(i, " ", data[i])

def get_correct_input(value_type = "str",
                       posbl_value = None, usr_str = "Введите значение"):
    """ returns correct input values (int or string)"""
    while True:
        inp_value = input(usr_str)
        if value_type == "str" and \
        (inp_value in posbl_value
         or posbl_value == []):
            return inp_value
        if value_type == "int":
            try:
                int_inp_value = int(inp_value)
                if int_inp_value in posbl_value \
                    or posbl_value == []:
                    return int_inp_value
            except ValueError:
                pass
        print("Неправильный ввод,\n Повторите попытку")

def user_menu():
    """ returns a task number """
    while True:
        print("Выберете действие:\n",
              "1 - Загрузить информацию из файла\n",
              "2 - Поиск по названию\n",
              "3 - Фильтр по количеству остатка\n",
              "4 - Добавить запись\n",
              "5 - Удалить запись\n",
              "6 - Сохранить\n",
              "7 - Выход\n")
        return get_correct_input("int", [1, 2, 3, 4, 5, 6, 7],
                                "Введите номер действия: ")

def main():
    """ БАКА СИНДЗИ НЕ ЛЕЗЕТ В РОБОТА """
    print("\nВас приветствует программа по работе",
          "с файлами в python")
    print("Практическую выполнил Ходыкин Александр\n")
    data =  {"Арбузы" : {"price":"29",
                      "surplus":"132", "units":"кг"}}
    
    while True:
        task = user_menu()
        match task:
            case 1:
                data = first_task()
            case 2:
                product = \
                    get_correct_input("str", [], "Введите название товара: ")
                second_task(data, product)
            case 3:
                number = \
                    get_correct_input("int", [], "Введите число для фильтра: ")
                user_menu_str = \
                    "Введите операцию:\n0 - меньше заданного числа: \n1 - больше заданного числа: "
                operation = \
                    get_correct_input("int", [0, 1], user_menu_str)
                third_task(data, number, bool(operation))
            case 4:
                pass
            case 5:
                pass
            case 6:
                with open("data.pickle", "wb") as write_file:
                    pickle.dump(data, write_file)
            case 7:
                break

if __name__ == "__main__":
    main()