import pickle

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
                if int_inp_value in posbl_value:
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
    data =  {"Арбузы" : {"цена":"29",
                      "осталось":"132", "единица измерения":"кг"}}
    
    while True:
        task = user_menu()
        match task:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                break

if __name__ == "__main__":
    main()