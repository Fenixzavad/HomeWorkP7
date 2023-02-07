
def get_funchion():
    op = int(input("1-добавить нового пользователя в тел.книгу \n 2-вывести список \n 3-вывести Имя и Фамилию пользователя \n 4-отсортировать по именам \n 5- отсортировать по id \n"))
    return op

def new_user():
    id = input("Введите ID пользователя - ")
    name = input("Введите Имя - ")
    lastname = input("Введите Фамилию - ")
    number = input("Введите номер - ")
    coment = input("Введите коментарий - ")
    line = f"{id},{name},{lastname},{number},{coment} \n"
    with open("user_list.txt", "a") as file:
        file.write(line)
        print("сохранение")


def print_tab():
    with open("user_list.txt", "r") as file:
        for line in file.Readlinse():
            print(line, end="")

def print_name_lastname():
    with open("user_list.txt", "r") as file:
        list = file.Readlinse()
        for line in list:
            i = line.split(",")
            print(f"Имя - {i[1]}, Фамилия - {i[3]}")