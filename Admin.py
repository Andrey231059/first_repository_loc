class User():
    def __init__(self, user_id, name, access_level):
        self.user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_ID(self):
        return self.user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name, access_level,admin_rights):
        super().__init__(user_id, name, access_level)
        self._admin_rights = admin_rights
        self._users = []

    def add_user(self, user_id, name, access_level):
        new_user = User(user_id, name, access_level)
        self._users.append(new_user)

    def remove_user(self, name):
       for user in self._users:
            if user.get_name() == name:
                self._users.remove(user)
                print(f"Пользователь {name} удалён.")
       return
       print(f"Пользователь {name} не найден.")

    def print_users(self):
        for user in self._users:
            print(f"пользователь - {user.get_name()} доступ - {user.get_access_level()}")


admin = Admin(user_id = "A001", name = "Админ", access_level = 5, admin_rights = True)

admin.add_user(user_id = "U001", name = "Андрей", access_level = 2)
admin.add_user(user_id = "U002", name = "Екатерина", access_level = 3)
admin.add_user(user_id = "U003", name = "Алексей", access_level = 4)
admin.print_users()
admin.remove_user("Андрей")
admin.print_users()





