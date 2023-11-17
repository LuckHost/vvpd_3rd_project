import pickle

def get_correct_inp(list_of_values, menu_str = "Введите значение.. "):
    """ returns correct input in list_of_values range"""
    while True:
        try:
            value = int(input(menu_str))
            if value in list_of_values:
                return value
            print("Ввод инкорректен, повторите")
            continue
        except ValueError:
            print("Ввод инкорректен, повторите")

def main():
    """ БАКА СИНДЗИ НЕ ЛЕЗЕТ В РОБОТА """
    print(" (͡° ͜ʖ ͡°)  А мне арбузы дороже комплементации человечества..")

if __name__ == "__main__":
    main()