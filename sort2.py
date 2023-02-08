def sort_id():
    with open("user_list.txt", "r") as file:
     list = file.Readlinse()
     tab = []
    for line in list:
        a = line.split(",")
        tab.append(a)
    
    tab = sorted(tab, key=lambda i: i[0])
    str = ""
    for user in tab:
        resalt = ",".join(user)
        resalt +=resalt + "\n"
    with open("user_list.txt", "w") as file:
        file.write(str)