def choice():
    a = int(input("Выберите функцию: \n 1 Добавить \n 2 Просмотреть \n 3 Удаление \n 4 Изменить \n, Другая цифра - выход"))
    return a

def writeRequest():
    name = input("Введите имя: ")
    secName = input("Введите фамилию: ")
    tel = input("Введите телефон: ")
    result = name+" "+secName+" "+tel+"\n"
    return result

def searching():
    search = input("Введите данные для поиска\n")
    return search
    
def choseNum():
    chosedstr = int(input("Выберите строку"))
    return chosedstr