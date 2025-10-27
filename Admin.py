class User():
    def __init__(self, ID, name, access_level):
        self.__private_ID = ID
        self.__private_name = name
        self.__private_access_level = access_level


class Admin(User):
    def __init__(self, ID, name, access_level,admin_rights):
        super().__init__(ID, name, access_level)
        self.admin_rights = admin_rights
        self.users = []

    def get_users(self):
        return self.users

    def add_user(self):
        name = input("Введите имя пользователя - ")
        ID = input("Введите ID - ")
        access_level = int(input("Введите права пользотателя. От 1 до 5 - "))
        self.users.append({"ID": ID, "name": name, "access_level": access_level, "admin_rights": False})

    def remove_user(self):
        name = input("Введите имя пользователя - ")
        for t in self.users:
            if t["name"] == name:
                self.users.remove(t)
                print(f"Пользователь {name} удалён.")
                return
        print(f"Пользователь {name} не найден.")

    def print_users(self):
        for t in self.users:
            print(f"пользователь - {t['name']} доступ - {t['access_level']}")


Ad = Admin(ID = "A001", name = "Админ", access_level = 5, admin_rights = True)
Ad.add_user()
Ad.add_user()
Ad.add_user()
Ad.print_users()
Ad.remove_user()
Ad.print_users()



